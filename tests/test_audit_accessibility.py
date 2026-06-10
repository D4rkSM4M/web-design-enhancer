#!/usr/bin/env python3
"""
tests/test_audit_accessibility.py
Unit tests for scripts/audit_accessibility.py

Each test:
  1. Builds a minimal HTML string that contains the violation
  2. Passes it to the relevant A11yAuditor check method
  3. Asserts the issue is reported (or NOT reported for the clean case)

No browser, no network, no Playwright needed.
"""

import sys
import os
import pytest

# Make the scripts package importable regardless of cwd
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scripts.audit_accessibility import A11yAuditor


# ── Helper ────────────────────────────────────────────────────────────────────

def auditor_for(html: str) -> A11yAuditor:
    """Return an A11yAuditor instance pre-populated by running checks on html."""
    a = A11yAuditor()
    a._audit_file_from_string(html, ctx="test.html")
    return a


def issue_codes(a: A11yAuditor):
    return [i["code"] for i in a.issues]


# ── Patch A11yAuditor to accept a raw string ──────────────────────────────────
# The production code reads files; we inject a helper for unit testing.

def _audit_file_from_string(self, content: str, ctx: str = "test.html"):
    """Helper method injected into A11yAuditor for testing."""
    self._check_html_lang(content, ctx)
    self._check_viewport_meta(content, ctx)
    self._check_title(content, ctx)
    self._check_img_alt(content, ctx)
    self._check_button_type(content, ctx)
    self._check_input_labels(content, ctx)
    self._check_div_onclick(content, ctx)
    self._check_empty_links(content, ctx)
    # CSS checks — only run when ctx ends with .css
    if ctx.endswith('.css'):
        self._check_font_size_px(content, ctx)


A11yAuditor._audit_file_from_string = _audit_file_from_string


# ── C1: img without alt ───────────────────────────────────────────────────────

class TestC1ImgAlt:
    def test_img_missing_alt_reported(self):
        html = '<img src="/hero.jpg" />'
        a = auditor_for(html)
        assert "C1" in issue_codes(a)

    def test_img_with_alt_ok(self):
        html = '<img src="/hero.jpg" alt="Hero image" />'
        a = auditor_for(html)
        assert "C1" not in issue_codes(a)

    def test_img_with_empty_alt_ok(self):
        """Empty alt is valid for decorative images."""
        html = '<img src="/decoration.svg" alt="" />'
        a = auditor_for(html)
        assert "C1" not in issue_codes(a)

    def test_multiple_imgs_one_missing(self):
        html = '<img src="/a.jpg" alt="A" /><img src="/b.jpg" />'
        a = auditor_for(html)
        assert "C1" in issue_codes(a)
        # Only one violation
        assert sum(1 for c in issue_codes(a) if c == "C1") == 1


# ── C2: button without type ───────────────────────────────────────────────────

class TestC2ButtonType:
    def test_button_missing_type_reported(self):
        html = '<button>Envoyer</button>'
        a = auditor_for(html)
        assert "C2" in issue_codes(a)

    def test_button_type_submit_ok(self):
        html = '<button type="submit">Envoyer</button>'
        a = auditor_for(html)
        assert "C2" not in issue_codes(a)

    def test_button_type_button_ok(self):
        html = '<button type="button">Annuler</button>'
        a = auditor_for(html)
        assert "C2" not in issue_codes(a)

    def test_button_type_reset_ok(self):
        html = '<button type="reset">Réinitialiser</button>'
        a = auditor_for(html)
        assert "C2" not in issue_codes(a)


# ── C3: input without label ───────────────────────────────────────────────────

class TestC3InputLabel:
    def test_input_no_label_reported(self):
        html = '<input type="text" placeholder="Votre nom" />'
        a = auditor_for(html)
        assert "C3" in issue_codes(a)

    def test_input_with_label_for_ok(self):
        html = '<label for="name">Nom</label><input type="text" id="name" />'
        a = auditor_for(html)
        assert "C3" not in issue_codes(a)

    def test_input_with_aria_label_ok(self):
        html = '<input type="text" aria-label="Nom complet" />'
        a = auditor_for(html)
        assert "C3" not in issue_codes(a)

    def test_input_with_aria_labelledby_ok(self):
        html = '<span id="lbl">Nom</span><input type="text" aria-labelledby="lbl" />'
        a = auditor_for(html)
        assert "C3" not in issue_codes(a)

    def test_hidden_input_skipped(self):
        """Hidden inputs don't need labels."""
        html = '<input type="hidden" name="token" value="abc" />'
        a = auditor_for(html)
        assert "C3" not in issue_codes(a)

    def test_submit_input_skipped(self):
        html = '<input type="submit" value="Envoyer" />'
        a = auditor_for(html)
        assert "C3" not in issue_codes(a)

    def test_textarea_no_label_reported(self):
        html = '<textarea placeholder="Votre message"></textarea>'
        a = auditor_for(html)
        assert "C3" in issue_codes(a)

    def test_select_no_label_reported(self):
        html = '<select><option>Option 1</option></select>'
        a = auditor_for(html)
        assert "C3" in issue_codes(a)


# ── C4: div/span with onclick but not keyboard accessible ─────────────────────

class TestC4DivOnclick:
    def test_div_onclick_no_role_reported(self):
        html = '<div onclick="doSomething()">Cliquez ici</div>'
        a = auditor_for(html)
        assert "C4" in issue_codes(a)

    def test_div_onclick_role_no_tabindex_reported(self):
        html = '<div role="button" onclick="doSomething()">Cliquez</div>'
        a = auditor_for(html)
        assert "C4" in issue_codes(a)

    def test_div_onclick_full_aria_ok(self):
        html = '<div role="button" tabindex="0" onclick="doSomething()">Cliquez</div>'
        a = auditor_for(html)
        assert "C4" not in issue_codes(a)

    def test_span_onclick_reported(self):
        html = '<span onclick="toggle()">Toggle</span>'
        a = auditor_for(html)
        assert "C4" in issue_codes(a)


# ── C8: html without lang ─────────────────────────────────────────────────────

class TestC8HtmlLang:
    def test_html_without_lang_reported(self):
        html = '<!DOCTYPE html><html><head><title>Test</title></head><body></body></html>'
        a = auditor_for(html)
        assert "C8" in issue_codes(a)

    def test_html_with_lang_ok(self):
        html = '<!DOCTYPE html><html lang="fr"><head><title>Test</title></head></html>'
        a = auditor_for(html)
        assert "C8" not in issue_codes(a)

    def test_no_html_tag_skipped(self):
        """Fragments without <html> should not trigger C8."""
        html = '<div><p>Contenu</p></div>'
        a = auditor_for(html)
        assert "C8" not in issue_codes(a)


# ── C9: empty link ────────────────────────────────────────────────────────────

class TestC9EmptyLink:
    def test_empty_link_reported(self):
        html = '<a href="/page"></a>'
        a = auditor_for(html)
        assert "C9" in issue_codes(a)

    def test_link_with_text_ok(self):
        html = '<a href="/page">Accueil</a>'
        a = auditor_for(html)
        assert "C9" not in issue_codes(a)

    def test_link_with_aria_label_ok(self):
        html = '<a href="/page" aria-label="Accueil"></a>'
        a = auditor_for(html)
        assert "C9" not in issue_codes(a)

    def test_link_with_img_alt_ok(self):
        html = '<a href="/page"><img src="/logo.svg" alt="Logo" /></a>'
        a = auditor_for(html)
        assert "C9" not in issue_codes(a)

    def test_link_with_img_no_alt_still_empty(self):
        """Link containing <img> without alt is still an empty link."""
        html = '<a href="/page"><img src="/logo.svg" /></a>'
        a = auditor_for(html)
        assert "C9" in issue_codes(a)


# ── C10: missing title ────────────────────────────────────────────────────────

class TestC10Title:
    def test_missing_title_reported(self):
        html = '<html lang="fr"><head></head><body></body></html>'
        a = auditor_for(html)
        assert "C10" in issue_codes(a)

    def test_empty_title_reported(self):
        html = '<html lang="fr"><head><title></title></head></html>'
        a = auditor_for(html)
        assert "C10" in issue_codes(a)

    def test_whitespace_only_title_reported(self):
        html = '<html lang="fr"><head><title>   </title></head></html>'
        a = auditor_for(html)
        assert "C10" in issue_codes(a)

    def test_valid_title_ok(self):
        html = '<html lang="fr"><head><title>Accueil — Mon Projet</title></head></html>'
        a = auditor_for(html)
        assert "C10" not in issue_codes(a)


# ── Clean HTML: no false positives ───────────────────────────────────────────

class TestCleanHTML:
    CLEAN_HTML = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Accueil — Mon Projet</title>
</head>
<body>
  <main>
    <h1>Titre principal</h1>
    <img src="/hero.jpg" alt="Illustration principale" />
    <img src="/decoration.svg" alt="" />

    <form>
      <label for="email">Adresse email</label>
      <input type="email" id="email" placeholder="nom@exemple.com" />
      <button type="submit">Envoyer</button>
    </form>

    <button type="button" onclick="toggle()">Afficher</button>

    <nav>
      <a href="/">Accueil</a>
      <a href="/a-propos">À propos</a>
      <a href="/" aria-label="Logo — accueil"><img src="/logo.svg" alt="Logo" /></a>
    </nav>
  </main>
</body>
</html>"""

    def test_clean_html_zero_violations(self):
        a = auditor_for(self.CLEAN_HTML)
        assert a.issues == [], (
            f"Expected 0 violations but got {len(a.issues)}: "
            + ", ".join(f"[{i['code']}] {i['message']}" for i in a.issues)
        )
