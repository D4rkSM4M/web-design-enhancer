#!/usr/bin/env python3
"""
Design Validation Script for web-design-enhancer

Valide un fichier DESIGN.md pour éviter le "AI slop":
- Vérifie les espacements (multiples de 8px)
- Valide la typographie (max 2 polices)
- Contrôle les couleurs (rôles sémantiques)
- Audit les animations (≤ 400ms)
- Détecte les antipatterns (gradients clichés, icônes génériques)

Usage:
    python3 validate_design.py DESIGN.md
    python3 validate_design.py DESIGN.md --strict
"""

import sys
import re
import json
from pathlib import Path
from typing import List, Dict, Tuple


class DesignValidator:
    """Validateur de DESIGN.md"""

    def __init__(self, filepath: str, strict: bool = False):
        self.filepath = Path(filepath)
        self.strict = strict
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.content = ""
        self.sections = {}

    def run(self) -> bool:
        """Exécute la validation complète. Retourne True si OK."""
        if not self.filepath.exists():
            print(f"❌ Erreur: Fichier {self.filepath} non trouvé")
            return False

        self.content = self.filepath.read_text(encoding="utf-8")
        self._parse_sections()

        # Validations
        self._validate_structure()
        self._validate_typography()
        self._validate_colors()
        self._validate_spacing()
        self._validate_animations()
        self._validate_components()
        self._detect_antipatterns()

        # Rapport
        self._print_report()
        return len(self.errors) == 0

    def _parse_sections(self):
        """Parse les sections principales du DESIGN.md"""
        sections = {
            "theme": r"## 1\. Thème Visuel.*?(?=##|$)",
            "colors": r"## 2\. Palette de Couleurs.*?(?=##|$)",
            "typography": r"## 3\. Typographie.*?(?=##|$)",
            "hierarchy": r"## 4\. Hiérarchie Typographique.*?(?=##|$)",
            "spacing": r"## 5\. Espacement et Grille.*?(?=##|$)",
            "components": r"## 6\. Composants et États.*?(?=##|$)",
            "animations": r"## 7\. Motion et Animations.*?(?=##|$)",
            "checklist": r"## ✅ Checklist.*?(?=##|$)",
        }

        for name, pattern in sections.items():
            match = re.search(pattern, self.content, re.DOTALL | re.IGNORECASE)
            self.sections[name] = match.group(0) if match else ""

    def _validate_structure(self):
        """Vérifie que toutes les sections obligatoires existent"""
        required = ["theme", "colors", "typography", "spacing", "components", "animations"]
        for section in required:
            if not self.sections.get(section):
                self.errors.append(f"❌ Section obligatoire manquante: {section}")

    def _validate_typography(self):
        """Valide la typographie (max 2 polices)"""
        typography_section = self.sections.get("typography", "")

        # Détecte les polices mentionnées
        font_patterns = [
            r"(?:Font|Police|Typeface):\s*([A-Za-z\s]+?)(?:\n|,|$)",
            r"\*\*([A-Za-z\s]+?)\*\*.*?(?:Display|Body|Monospace)",
        ]

        fonts = set()
        for pattern in font_patterns:
            matches = re.findall(pattern, typography_section, re.IGNORECASE)
            fonts.update(m.strip() for m in matches if m.strip())

        # Exclure les mots-clés non-polices
        exclude = {"font", "police", "typeface", "raison", "utilisation", "poids", "espacement"}
        fonts = {f for f in fonts if f.lower() not in exclude and len(f) > 2}

        if len(fonts) > 3:
            self.errors.append(f"❌ Trop de polices ({len(fonts)}): {', '.join(fonts)}. Max 2 (display + body)")
        elif len(fonts) < 2:
            self.warnings.append(f"⚠️  Polices insuffisantes ({len(fonts)}): Minimum 2 requises")

        # Vérifie les polices génériques (antipattern)
        generic_fonts = {"helvetica", "arial", "times new roman", "georgia", "verdana"}
        for font in fonts:
            if font.lower() in generic_fonts:
                self.errors.append(f"❌ Police générique détectée: {font}. Utiliser Google Fonts ou custom")

    def _validate_colors(self):
        """Valide la palette de couleurs"""
        colors_section = self.sections.get("colors", "")

        # Détecte les couleurs hex
        hex_pattern = r"#[0-9A-Fa-f]{6}"
        colors = re.findall(hex_pattern, colors_section)

        if len(colors) < 4:
            self.errors.append(f"❌ Trop peu de couleurs ({len(colors)}). Minimum 4 requises")
        elif len(colors) > 8:
            self.errors.append(f"❌ Trop de couleurs ({len(colors)}). Maximum 8 recommandé")

        # Vérifie les rôles sémantiques
        roles = ["primaire", "secondaire", "accent", "succès", "attention", "destruction"]
        found_roles = sum(1 for role in roles if role.lower() in colors_section.lower())

        if found_roles < 4:
            self.warnings.append(f"⚠️  Rôles sémantiques insuffisants ({found_roles}). Minimum 4 recommandé")

        # Détecte les gradients clichés
        cliche_gradients = [
            (r"bleu.*?violet|blue.*?purple", "bleu→violet"),
            (r"rose.*?violet|pink.*?purple", "rose→violet"),
            (r"rose.*?rouge|pink.*?red", "rose→rouge"),
            (r"cyan.*?bleu|cyan.*?blue", "cyan→bleu"),
        ]

        for pattern, name in cliche_gradients:
            if re.search(pattern, colors_section, re.IGNORECASE):
                self.warnings.append(f"⚠️  Gradient cliché détecté: {name}. Justifier par rôle sémantique")

    def _validate_spacing(self):
        """Valide que tous les espacements sont multiples de 8px"""
        spacing_section = self.sections.get("spacing", "")

        # Détecte les valeurs de spacing
        spacing_pattern = r"(\d+)\s*px"
        spacings = re.findall(spacing_pattern, spacing_section)

        invalid_spacings = []
        for spacing in spacings:
            value = int(spacing)
            if value % 8 != 0 and value != 4:  # 4px acceptable pour micro-espacements
                invalid_spacings.append(value)

        if invalid_spacings:
            self.errors.append(
                f"❌ Espacements non-multiples de 8px: {invalid_spacings}. "
                f"Utiliser: 4, 8, 16, 24, 32, 48, 64"
            )

        # Vérifie la présence de la grille 8px
        if "8px" not in spacing_section and "8 px" not in spacing_section:
            self.warnings.append("⚠️  Grille 8px non mentionnée explicitement")

    def _validate_animations(self):
        """Valide les animations (durée ≤ 400ms)"""
        animations_section = self.sections.get("animations", "")

        # Détecte les durées d'animation
        duration_pattern = r"(\d+)\s*m?s"
        durations = re.findall(duration_pattern, animations_section)

        invalid_durations = []
        for duration in durations:
            value = int(duration)
            if value > 400:
                invalid_durations.append(value)

        if invalid_durations:
            self.errors.append(
                f"❌ Animations trop longues: {invalid_durations}ms. "
                f"Maximum 400ms recommandé"
            )

        # Vérifie prefers-reduced-motion
        if "prefers-reduced-motion" not in animations_section.lower():
            self.warnings.append("⚠️  Pas de mention de prefers-reduced-motion")

    def _validate_components(self):
        """Valide les composants (max 3 variantes)"""
        components_section = self.sections.get("components", "")

        # Détecte les variantes de boutons
        button_pattern = r"### Variantes.*?(?=###|$)"
        button_section = re.search(button_pattern, components_section, re.DOTALL)

        if button_section:
            variants = re.findall(r"\d\.\s+\*\*([^*]+)\*\*", button_section.group(0))
            if len(variants) > 3:
                self.errors.append(
                    f"❌ Trop de variantes de boutons ({len(variants)}). Maximum 3 recommandé"
                )

    def _detect_antipatterns(self):
        """Détecte les antipatterns (AI slop)"""
        content_lower = self.content.lower()

        # Icônes génériques Lucide
        lucide_icons = ["sparkles", "zap", "cog", "network", "arrow", "check", "star"]
        found_icons = [icon for icon in lucide_icons if icon in content_lower]

        if found_icons:
            self.warnings.append(
                f"⚠️  Icônes Lucide génériques détectées: {', '.join(found_icons)}. "
                f"Considérer custom SVG ou pack cohérent"
            )

        # Buzzwords vagues
        buzzwords = ["premium", "moderne", "élégant", "magnifique", "incroyable"]
        found_buzzwords = [bw for bw in buzzwords if bw in content_lower]

        if found_buzzwords:
            self.warnings.append(
                f"⚠️  Buzzwords vagues: {', '.join(found_buzzwords)}. "
                f"Remplacer par descriptions précises"
            )

        # Sections template génériques
        template_sections = ["hero", "features", "cta", "testimonials", "footer"]
        found_sections = sum(1 for sec in template_sections if sec in content_lower)

        if found_sections >= 4:
            self.warnings.append(
                f"⚠️  Structure template générique détectée ({found_sections} sections). "
                f"Considérer une approche plus unique"
            )

        # Gradients uniformes
        if "gradient" in content_lower:
            gradient_count = len(re.findall(r"gradient", content_lower))
            if gradient_count > 3:
                self.warnings.append(
                    f"⚠️  Trop de gradients ({gradient_count}). "
                    f"Limiter à 2-3 gradients intentionnels"
                )

    def _print_report(self):
        """Affiche le rapport de validation"""
        print("\n" + "=" * 60)
        print("🎨 DESIGN VALIDATION REPORT")
        print("=" * 60)

        if self.errors:
            print(f"\n❌ ERREURS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  {error}")

        if self.warnings:
            print(f"\n⚠️  AVERTISSEMENTS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  {warning}")

        if not self.errors and not self.warnings:
            print("\n✅ VALIDATION RÉUSSIE - Aucune erreur détectée!")

        print("\n" + "=" * 60)
        if self.errors:
            print(f"❌ RÉSULTAT: ÉCHOUÉ ({len(self.errors)} erreurs)")
        elif self.warnings:
            print(f"⚠️  RÉSULTAT: RÉUSSI AVEC AVERTISSEMENTS ({len(self.warnings)} avertissements)")
        else:
            print("✅ RÉSULTAT: RÉUSSI - Prêt pour le codage!")
        print("=" * 60 + "\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_design.py DESIGN.md [--strict]")
        sys.exit(1)

    filepath = sys.argv[1]
    strict = "--strict" in sys.argv

    validator = DesignValidator(filepath, strict)
    success = validator.run()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
