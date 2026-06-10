#!/usr/bin/env python3
"""
audit_accessibility.py — WCAG 2.1 AA compliance check for AI-generated HTML

Detects the accessibility violations that AI models produce most systematically:
  - C1  img without alt attribute
  - C2  button without type attribute
  - C3  input without label or aria-label
  - C4  div/span with onclick but no role=button + tabIndex
  - C7  font-size in px on html/body/:root (WCAG 1.4.4 Text Resize)
  - C8  Missing lang attribute on <html>
  - C9  Empty <a> links (no text, no aria-label)
  - C10 Missing <title> in <head>
  - H1  Missing <meta name='viewport'> in <head>

Usage:
    python3 scripts/audit_accessibility.py --path ./src
    python3 scripts/audit_accessibility.py --file index.html
    python3 scripts/audit_accessibility.py --path ./src --json
    python3 scripts/audit_accessibility.py --path ./src --strict

Exit codes:
    0 = no issues
    1 = issues found
"""

import sys
import re
import json
import argparse
from pathlib import Path
from typing import List, Dict
from collections import defaultdict

# ── Terminal colors ──────────────────────────────────────────────────────────

GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"

def ok(msg):    print(f"  {GREEN}[OK]    {msg}{RESET}")
def fail(msg):  print(f"  {RED}[ERROR] {msg}{RESET}")
def warn(msg):  print(f"  {YELLOW}[WARN]  {msg}{RESET}")
def info(msg):  print(f"  {CYAN}        {msg}{RESET}")


# ── Issue registry ───────────────────────────────────────────────────────────

class A11yAuditor:
    """
    Accessibility auditor for HTML files produced by AI models.

    Each check is labelled with the WCAG 2.1 criterion it covers and the
    §0b code from the skill that forbids the pattern.
    """

    SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", "__pycache__", ".cache"}

    def __init__(self, path: str = None, file: str = None, strict: bool = False):
        self.root   = Path(path) if path else None
        self.file   = Path(file) if file else None
        self.strict = strict
        self.issues: List[Dict] = []
        self.stats  = defaultdict(int)

    # ── Public entry point ───────────────────────────────────────────────────

    def run(self) -> bool:
        if self.file:
            self._audit_file(self.file)
        elif self.root:
            self._audit_directory(self.root)
        else:
            print("[ERROR] Specify --path or --file")
            return False
        return len(self.issues) == 0

    # ── Directory walker ─────────────────────────────────────────────────────

    def _audit_directory(self, directory: Path):
        for fp in directory.rglob("*"):
            if any(part in self.SKIP_DIRS for part in fp.parts):
                continue
            if fp.suffix in {".html", ".htm"}:
                self._audit_file(fp)
            elif self.strict and fp.suffix in {".jsx", ".tsx"}:
                # In strict mode also scan JSX/TSX for onClick on divs
                self._audit_jsx_file(fp)

    # ── HTML audit ───────────────────────────────────────────────────────────

    def _audit_file(self, fp: Path):
        if not fp.exists():
            print(f"[ERROR] File not found: {fp}")
            return
        content = fp.read_text(encoding="utf-8", errors="ignore")
        ctx = str(fp)

        self._check_html_lang(content, ctx)
        self._check_viewport_meta(content, ctx)
        self._check_title(content, ctx)
        self._check_img_alt(content, ctx)
        self._check_button_type(content, ctx)
        self._check_input_labels(content, ctx)
        self._check_div_onclick(content, ctx)
        self._check_empty_links(content, ctx)
        if fp.suffix == '.css':
            self._check_font_size_px(content, ctx)

    def _audit_jsx_file(self, fp: Path):
        content = fp.read_text(encoding="utf-8", errors="ignore")
        ctx = str(fp)
        self._check_div_onclick_jsx(content, ctx)
        self._check_img_alt_jsx(content, ctx)

    # ── Individual checks ────────────────────────────────────────────────────

    def _check_html_lang(self, content: str, ctx: str):
        """C8 — <html> must have a lang attribute."""
        if re.search(r'<html\b', content, re.IGNORECASE):
            if not re.search(r'<html[^>]*\blang=', content, re.IGNORECASE):
                self._add("C8", ctx, 0,
                    "<html> is missing lang attribute",
                    "Add lang attribute to <html> element: <html lang=\"fr\"> or <html lang=\"en\">. "
                    "Screen readers use lang to select the correct voice/pronunciation engine."
                )

    def _check_viewport_meta(self, content: str, ctx: str):
        """H1 — <head> must contain <meta name='viewport'> for mobile."""
        if re.search(r'<head\b', content, re.IGNORECASE):
            has_viewport = re.search(
                r'<meta[^>]*name=["\'\']viewport["\'\'][^>]*/?>',
                content, re.IGNORECASE
            )
            if not has_viewport:
                self._add("H1", ctx, 0,
                    "<head> missing <meta name='viewport'>",
                    "Add inside <head>: "
                    "<meta name='viewport' content='width=device-width, initial-scale=1'>. "
                    "Without this, mobile browsers render at 980px width — layout completely broken."
                )
                self.stats['no_viewport'] += 1

    def _check_font_size_px(self, content: str, ctx: str):
        """C7 — font-size in px on html/body breaks browser text zoom (WCAG 1.4.4)."""
        # Only meaningful in CSS files
        for m in re.finditer(
            r'(?:html|body|:root)\s*\{([^}]*)\}',
            content, re.IGNORECASE | re.DOTALL
        ):
            block = m.group(1)
            line = content[:m.start()].count("\n") + 1
            if re.search(r'\bfont-size\s*:\s*\d+px', block, re.IGNORECASE):
                self._add("C7", ctx, line,
                    "font-size in px on html/body/:root — WCAG 1.4.4 Text Resize",
                    "Replace 'font-size: 16px' with 'font-size: 100%' or 'font-size: 1rem'. "
                    "Fixed px on the root element prevents browser text zoom from working. "
                    "WCAG 1.4.4 requires text to be resizable up to 200%."
                )
                self.stats['font_size_px'] += 1

    def _check_title(self, content: str, ctx: str):
        """C10 — <head> must contain a non-empty <title>."""
        if re.search(r'<head\b', content, re.IGNORECASE):
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if not title_match:
                self._add("C10", ctx, 0,
                    "<title> element is missing",
                    "Add a descriptive <title> to <head>. "
                    "WCAG 2.4.2 requires page titles that describe topic or purpose."
                )
            elif not title_match.group(1).strip():
                self._add("C10", ctx, 0,
                    "<title> element is empty",
                    "Provide a descriptive title: <title>Page Name — Product Name</title>. "
                    "An empty title is equivalent to having none."
                )

    def _check_img_alt(self, content: str, ctx: str):
        """C1 — Every <img> must have an alt attribute (WCAG 2.1 §1.1.1)."""
        for m in re.finditer(r'<img\b[^>]*/?>',  content, re.IGNORECASE):
            tag = m.group(0)
            line = content[:m.start()].count("\n") + 1
            if not re.search(r'\balt=', tag, re.IGNORECASE):
                self._add("C1", ctx, line,
                    f"<img> without alt attribute: {tag[:80]}",
                    "Add alt='Descriptive text' for informative images. "
                    "For purely decorative images use alt='' (empty, not omitted). "
                    "WCAG 2.1 §1.1.1 — Text Alternatives."
                )
                self.stats["img_no_alt"] += 1

    def _check_img_alt_jsx(self, content: str, ctx: str):
        """C1 — Same check for JSX <img> elements."""
        for m in re.finditer(r'<img\b[^/]*(?:/>|>)', content, re.IGNORECASE):
            tag = m.group(0)
            line = content[:m.start()].count("\n") + 1
            if not re.search(r'\balt(?:\s*=|\s*{)', tag, re.IGNORECASE):
                self._add("C1", ctx, line,
                    f"JSX <img> without alt: {tag[:80]}",
                    "Add alt='...' or alt={description} to every JSX <img>. "
                    "For decorative images: alt=''."
                )
                self.stats["img_no_alt"] += 1

    def _check_button_type(self, content: str, ctx: str):
        """C2 — Every <button> must declare type (WCAG 4.1.2)."""
        for m in re.finditer(r'<button\b[^>]*>', content, re.IGNORECASE):
            tag = m.group(0)
            line = content[:m.start()].count("\n") + 1
            if not re.search(r'\btype=', tag, re.IGNORECASE):
                self._add("C2", ctx, line,
                    f"<button> without type: {tag[:80]}",
                    "Add type='button' for standalone actions, type='submit' for forms. "
                    "Missing type defaults to 'submit' — breaks non-form buttons in forms."
                )
                self.stats["button_no_type"] += 1

    def _check_input_labels(self, content: str, ctx: str):
        """C3 — Every interactive input must have an accessible label."""
        # Collect label[for] targets
        label_fors = set(re.findall(r'<label\b[^>]*\bfor=["\']([^"\']+)["\']', content, re.IGNORECASE))
        # Also collect aria-labelledby targets (simplified)
        labelled_by = set(re.findall(r'\baria-labelledby=["\']([^"\']+)["\']', content, re.IGNORECASE))

        for m in re.finditer(r'<input\b[^>]*/?>|<textarea\b[^>]*>|<select\b[^>]*>', content, re.IGNORECASE):
            tag  = m.group(0)
            line = content[:m.start()].count("\n") + 1

            # Skip hidden inputs and submit/button/reset types
            if re.search(r'\btype=["\'](?:hidden|submit|button|reset|image)["\']', tag, re.IGNORECASE):
                continue

            has_aria_label    = bool(re.search(r'\baria-label=', tag, re.IGNORECASE))
            has_aria_labelled = bool(re.search(r'\baria-labelledby=', tag, re.IGNORECASE))

            # Check if this input's id is referenced by a <label for="...">
            id_match = re.search(r'\bid=["\']([^"\']+)["\']', tag, re.IGNORECASE)
            has_label_for = bool(id_match and id_match.group(1) in label_fors)

            if not (has_aria_label or has_aria_labelled or has_label_for):
                self._add("C3", ctx, line,
                    f"Input without accessible label: {tag[:80]}",
                    "Associate a label: <label for='inputId'>Label</label><input id='inputId'> "
                    "or add aria-label='Label text' directly on the input. "
                    "Placeholder text is NOT a substitute for a label."
                )
                self.stats["input_no_label"] += 1

    def _check_div_onclick(self, content: str, ctx: str):
        """C4 — div/span with onclick must have role=button + tabindex."""
        for m in re.finditer(r'<(?:div|span)\b[^>]*\bonclick=[^>]*>', content, re.IGNORECASE):
            tag  = m.group(0)
            line = content[:m.start()].count("\n") + 1
            has_role     = bool(re.search(r'\brole=["\']button["\']', tag, re.IGNORECASE))
            has_tabindex = bool(re.search(r'\btabindex=', tag, re.IGNORECASE))

            if not (has_role and has_tabindex):
                missing = []
                if not has_role:     missing.append("role=\"button\"")
                if not has_tabindex: missing.append("tabIndex=\"0\"")
                self._add("C4", ctx, line,
                    f"div/span with onclick missing {' and '.join(missing)}: {tag[:80]}",
                    f"Either replace with <button type='button'> or add {', '.join(missing)} "
                    "and an onKeyDown handler for Enter and Space keys. "
                    "Interactive divs are invisible to keyboard users and screen readers."
                )
                self.stats["div_onclick"] += 1

    def _check_div_onclick_jsx(self, content: str, ctx: str):
        """C4 — Same check for JSX."""
        for m in re.finditer(r'<(?:div|span)\b[^>]*\bonClick=', content, re.IGNORECASE):
            tag  = m.group(0)
            line = content[:m.start()].count("\n") + 1
            has_role     = bool(re.search(r'\brole=["\'{]', tag, re.IGNORECASE))
            has_tabindex = bool(re.search(r'\btabIndex=', tag, re.IGNORECASE))

            if not (has_role and has_tabindex):
                self._add("C4", ctx, line,
                    f"JSX div/span with onClick is not keyboard-accessible: {tag[:80]}",
                    "Replace with <button type='button' onClick={...}> or add "
                    "role='button' tabIndex={0} and onKeyDown handler."
                )
                self.stats["div_onclick"] += 1

    def _check_empty_links(self, content: str, ctx: str):
        """C9 — <a> must have text content or aria-label."""
        # Match opening <a> and its text content up to closing </a>
        for m in re.finditer(r'<a\b([^>]*)>(.*?)</a>', content, re.IGNORECASE | re.DOTALL):
            attrs       = m.group(1)
            inner       = m.group(2)
            line        = content[:m.start()].count("\n") + 1

            has_aria_label = bool(re.search(r'\baria-label=', attrs, re.IGNORECASE))
            has_aria_labelled = bool(re.search(r'\baria-labelledby=', attrs, re.IGNORECASE))
            # Strip inner HTML tags to get text content
            text_content = re.sub(r'<[^>]+>', '', inner).strip()
            # Check for meaningful img with alt inside the link
            has_img_alt  = bool(re.search(r'<img[^>]*\balt=["\'][^"\']+["\']', inner, re.IGNORECASE))

            if not (text_content or has_aria_label or has_aria_labelled or has_img_alt):
                self._add("C9", ctx, line,
                    f"Empty <a> link (no text, no aria-label): {m.group(0)[:80]}",
                    "Add descriptive text inside the <a> or add aria-label='Description'. "
                    "Screen readers announce link text — empty links are unusable. "
                    "WCAG 2.4.4 — Link Purpose."
                )
                self.stats["empty_links"] += 1

    # ── Issue builder ────────────────────────────────────────────────────────

    def _add(self, code: str, file: str, line: int, message: str, fix: str):
        self.issues.append({
            "code":    code,
            "file":    file,
            "line":    line,
            "message": message,
            "fix":     fix,
        })

    # ── Reports ──────────────────────────────────────────────────────────────

    def print_report(self):
        print(f"\n{BOLD}{'='*70}{RESET}")
        print(f"{BOLD}  ACCESSIBILITY AUDIT REPORT (WCAG 2.1 AA){RESET}")
        print(f"{BOLD}{'='*70}{RESET}\n")

        if not self.issues:
            ok("AUDIT PASSED — No accessibility violations detected!")
        else:
            fail(f"{len(self.issues)} accessibility violation(s) found:\n")

            by_file = defaultdict(list)
            for issue in self.issues:
                by_file[issue["file"]].append(issue)

            for fp in sorted(by_file.keys()):
                print(f"  {BOLD}{fp}{RESET}")
                for issue in by_file[fp]:
                    loc = f"Line {issue['line']}: " if issue["line"] else ""
                    fail(f"  [{issue['code']}] {loc}{issue['message']}")
                    info(f"  Fix: {issue['fix']}")
                    print()

        # Statistics
        print(f"{DIM}{'─'*70}{RESET}")
        print("  STATISTICS:")
        print(f"    img without alt:    {self.stats['img_no_alt']}")
        print(f"    button without type:{self.stats['button_no_type']}")
        print(f"    input without label:{self.stats['input_no_label']}")
        print(f"    div onclick:        {self.stats['div_onclick']}")
        print(f"    empty links:        {self.stats['empty_links']}")
        print(f"    missing viewport:   {self.stats['no_viewport']}")
        print(f"    font-size in px:    {self.stats['font_size_px']}")
        print(f"    TOTAL:              {len(self.issues)}")
        print(f"{BOLD}{'='*70}{RESET}\n")

    def print_json(self):
        output = {
            "total": len(self.issues),
            "passed": len(self.issues) == 0,
            "stats": dict(self.stats),
            "violations": [
                {
                    "code":    i["code"],
                    "file":    i["file"],
                    "line":    i["line"],
                    "message": i["message"],
                    "fix_instruction": i["fix"],
                }
                for i in self.issues
            ]
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))


# ── CLI entry point ──────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="WCAG 2.1 AA accessibility audit for AI-generated HTML",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scripts/audit_accessibility.py --path ./src
  python3 scripts/audit_accessibility.py --file index.html --json
  python3 scripts/audit_accessibility.py --path ./src --strict

Violation codes:
  C1  img without alt
  C2  button without type
  C3  input without label
  C4  div/span onclick without role=button
  C7  font-size in px on html/body/:root
  C8  html without lang
  C9  empty link
  C10 missing page title
  H1  missing <meta name='viewport'>
"""
    )
    parser.add_argument("--path",   help="Directory to scan (recursive, .html files)")
    parser.add_argument("--file",   help="Single HTML file to audit")
    parser.add_argument("--json",   action="store_true", help="Output JSON for agent consumption")
    parser.add_argument("--strict", action="store_true", help="Also scan .jsx/.tsx files")
    parser.add_argument("--output", help="Write JSON report to file")
    args = parser.parse_args()

    if not args.path and not args.file:
        parser.print_help()
        sys.exit(1)

    auditor = A11yAuditor(path=args.path, file=args.file, strict=args.strict)
    passed  = auditor.run()

    if args.json or args.output:
        if args.output:
            report = {
                "total": len(auditor.issues),
                "passed": passed,
                "stats": dict(auditor.stats),
                "violations": auditor.issues,
            }
            Path(args.output).write_text(
                json.dumps(report, indent=2, ensure_ascii=False),
                encoding="utf-8"
            )
            print(f"Report saved to {args.output}")
        if args.json:
            auditor.print_json()
    else:
        auditor.print_report()

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
