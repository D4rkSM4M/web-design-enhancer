# Référence Technique - Web Design Enhancer

Ce document détaille les spécifications techniques des scripts et des formats utilisés dans ce skill.

## 1. Scripts de Validation

### `validate_design.py`
Valide le fichier `DESIGN.md` selon les règles de design.
- **Entrée**: Chemin vers `DESIGN.md`
- **Règles**: 
  - Max 2 polices.
  - Espacements multiples de 8px.
  - Couleurs sémantiques présentes.

### `audit_spacing.py`
Analyse les fichiers CSS/TSX pour trouver des valeurs d'espacement non conformes.
- **Entrée**: Répertoire source
- **Regex**: Recherche `px` et vérifie si `% 8 == 0`.

### `detect_ai_slop.py`
Détecte les patterns typiques des IA (emojis, icônes génériques, buzzwords).
- **Score**: Démarre à 100, pénalités par infraction.
- **Seuil**: ≥ 80 pour validation.

### `visual_audit.py` (Nouveau)
Utilise Playwright pour auditer le rendu final.
- **Fonction**: Vérifie les styles calculés (Computed Styles) dans le navigateur.
- **Sortie**: Screenshots + Rapport JSON.

## 2. Format DESIGN.md (v2)
Le format `DESIGN.md` est le contrat de vérité. Il doit être placé à la racine du projet.
Sections obligatoires:
1. Thème Visuel
2. Palette de Couleurs
3. Typographie
4. Hiérarchie Typographique
5. Espacement et Grille
6. Composants et États
7. Motion et Animations
