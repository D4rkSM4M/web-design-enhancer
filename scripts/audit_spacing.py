#!/usr/bin/env python3
"""
Spacing Audit Script - Vérifie que tous les espacements sont multiples de 8px

Analyse les fichiers CSS/TSX/JSX pour détecter:
- Padding/margin non-multiples de 8px
- Tailles de rayon non-multiples de 4px
- Espacements incohérents

Usage:
    python3 audit_spacing.py --path ./client/src --output report.json
    python3 audit_spacing.py --file client/src/index.css
"""

import sys
import re
import json
from pathlib import Path
from typing import List, Dict, Tuple
from collections import defaultdict


class SpacingAuditor:
    """Audit des espacements dans le code"""

    def __init__(self, path: str = None, file: str = None):
        self.path = Path(path) if path else None
        self.file = Path(file) if file else None
        self.issues: List[Dict] = []
        self.stats = defaultdict(int)

    def run(self) -> bool:
        """Exécute l'audit"""
        if self.file:
            self._audit_file(self.file)
        elif self.path:
            self._audit_directory(self.path)
        else:
            print("❌ Erreur: Spécifier --path ou --file")
            return False

        self._print_report()
        return len(self.issues) == 0

    def _audit_directory(self, directory: Path):
        """Audit tous les fichiers CSS/TSX/JSX du répertoire"""
        extensions = {".css", ".tsx", ".jsx", ".ts", ".js"}

        for file_path in directory.rglob("*"):
            if file_path.suffix in extensions:
                self._audit_file(file_path)

    def _audit_file(self, file_path: Path):
        """Audit un fichier spécifique"""
        if not file_path.exists():
            print(f"❌ Fichier non trouvé: {file_path}")
            return

        content = file_path.read_text(encoding="utf-8", errors="ignore")

        # Propriétés de layout soumises à la grille 8px
        # Note : box-shadow, transform, border-width, outline sont EXCLUS —
        # ces propriétés de décoration/effet n'appartiennent pas à la grille de layout.
        LAYOUT_PROPS = {
            "padding": r"padding(?:-(?:top|right|bottom|left|block|inline))?:\s*([^;}\n]+)",
            "margin":  r"margin(?:-(?:top|right|bottom|left|block|inline))?:\s*([^;}\n]+)",
            "gap":     r"(?:gap|row-gap|column-gap):\s*([^;}\n]+)",
            "top|right|bottom|left": r"(?<!box-shadow:\s)(?:^|\s)(?:top|right|bottom|left):\s*([^;}\n]+)",
        }

        # Propriétés de rayon — grille 4px
        RADIUS_PROPS = {
            "border-radius": r"border-radius(?:-(?:top|bottom)-(?:left|right))?:\s*([^;}\n]+)",
        }

        # Propriétés NON soumises à la grille (effets, décorations) :
        # box-shadow, transform (translateY, scale...), border-width, outline,
        # width/height (peuvent être libres : 1px hairline, 2px cursor, etc.)

        all_prop_patterns = {**LAYOUT_PROPS, **RADIUS_PROPS}

        for prop, pattern in all_prop_patterns.items():
            matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                value = match.group(1).strip()

                # Ignorer les variables CSS (--var) et calc()
                if "--" in value or "calc(" in value or "var(" in value:
                    continue

                line_num = content[:match.start()].count("\n") + 1
                px_values = re.findall(r"(\d+)px", value)

                for px_val in px_values:
                    num = int(px_val)

                    if prop == "border-radius":
                        # Grille 4px pour les rayons, 0 et 9999 toujours autorisés
                        if num != 0 and num != 9999 and num % 4 != 0:
                            self.issues.append({
                                "file": str(file_path),
                                "line": line_num,
                                "property": prop,
                                "value": value,
                                "issue": f"Rayon {num}px non-multiple de 4px",
                                "severity": "warning"
                            })
                            self.stats["invalid_radius"] += 1
                    else:
                        # Grille 8px pour le layout, 4px toléré (micro-espacement)
                        # 2px toléré pour margin-left/right (curseurs typographiques, micro-détails)
                        is_micro_margin = (prop == "margin" and
                                          re.search(r"margin-(?:left|right)", match.group(0).split(":")[0], re.IGNORECASE)
                                          and num == 2)
                        if num != 0 and num % 8 != 0 and num != 4 and not is_micro_margin:
                            self.issues.append({
                                "file": str(file_path),
                                "line": line_num,
                                "property": prop,
                                "value": value,
                                "issue": f"Espacement {num}px non-multiple de 8px",
                                "severity": "warning"
                            })
                            self.stats["invalid_spacing"] += 1

    def _print_report(self):
        """Affiche le rapport d'audit"""
        print("\n" + "=" * 70)
        print("📏 SPACING AUDIT REPORT")
        print("=" * 70)

        if not self.issues:
            print("\n✅ AUDIT RÉUSSI - Tous les espacements sont valides!")
        else:
            print(f"\n❌ {len(self.issues)} problèmes d'espacement détectés:\n")

            # Groupe par fichier
            by_file = defaultdict(list)
            for issue in self.issues:
                by_file[issue["file"]].append(issue)

            for file_path in sorted(by_file.keys()):
                print(f"\n📄 {file_path}")
                for issue in by_file[file_path]:
                    print(f"  Ligne {issue['line']}: {issue['property']}")
                    print(f"    Valeur: {issue['value']}")
                    print(f"    ⚠️  {issue['issue']}")

        # Statistiques
        print("\n" + "-" * 70)
        print("📊 STATISTIQUES:")
        print(f"  Espacements invalides: {self.stats['invalid_spacing']}")
        print(f"  Rayons invalides: {self.stats['invalid_radius']}")
        print("=" * 70 + "\n")

        return len(self.issues) == 0


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Audit des espacements CSS")
    parser.add_argument("--path", help="Répertoire à auditer")
    parser.add_argument("--file", help="Fichier spécifique à auditer")
    parser.add_argument("--output", help="Fichier de sortie JSON")

    args = parser.parse_args()

    auditor = SpacingAuditor(path=args.path, file=args.file)
    success = auditor.run()

    if args.output:
        with open(args.output, "w") as f:
            json.dump(auditor.issues, f, indent=2)
        print(f"📄 Rapport sauvegardé: {args.output}")

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
