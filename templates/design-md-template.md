# DESIGN.md - Contrat de Design du Projet

Ce document définit les règles strictes de design pour le projet. Toute implémentation doit respecter ces spécifications pour éviter le "AI slop" et garantir une qualité professionnelle.

---

## 1. Thème Visuel & Concept
*Décrivez l'ambiance visuelle en termes techniques (ex: "Néomorphisme doux", "Minimalisme brutaliste", "Dark mode haute fidélité"). Évitez les buzzwords comme "moderne" ou "premium". Référez-vous aux styles UI de UI/UX Pro Max pour l'inspiration.*

- **Concept**: [Ex: Minimalisme Tech Haute Précision, Esthétique Industrielle]
- **Mots-clés**: [Ex: Géométrique, Contrasté, Fonctionnel, Brutaliste, Épuré]
- **Inspiration UI/UX Pro Max**: [Ex: Style "Neo-Brutalism", "Clean Tech", "Glassmorphism"]

## 2. Palette de Couleurs
*Utilisez des rôles sémantiques. Maximum 8 couleurs principales. Référez-vous aux palettes de couleurs de UI/UX Pro Max ou aux exemples de `getdesign.md` pour des combinaisons éprouvées.*

| Rôle | Hex | Utilisation |
| :--- | :--- | :--- |
| Primaire | # | [Ex: Boutons d'action, éléments clés] |
| Secondaire | # | [Ex: Éléments secondaires, accents] |
| Fond | # | [Ex: Arrière-plan principal] |
| Texte | # | [Ex: Texte principal] |
| Accent | # | [Ex: Éléments interactifs, mises en avant] |
| Succès | # | [Ex: Messages de succès] |
| Attention | # | [Ex: Alertes, avertissements] |
| Danger | # | [Ex: Actions destructives] |

## 3. Typographie
*Maximum 2 polices (une pour les titres/display, une pour le corps de texte). Référez-vous aux paires de polices de UI/UX Pro Max ou aux exemples de `getdesign.md`.*

- **Display (Titres)**: [Nom de la police] (Source: Google Fonts, Adobe Fonts, etc.)
- **Body (Corps de texte)**: [Nom de la police] (Source: Google Fonts, Adobe Fonts, etc.)
- **Monospace (Code/Données)**: [Nom de la police] (Optionnel, si nécessaire)

## 4. Hiérarchie Typographique
*Toutes les tailles doivent suivre une échelle harmonique. Définissez les tailles, poids et interlignes pour chaque niveau.*

- **H1**: [Taille] / [Poids] / [Interligne]
- **H2**: [Taille] / [Poids] / [Interligne]
- **H3**: [Taille] / [Poids] / [Interligne]
- **P (Paragraphe)**: [Taille] / [Poids] / [Interligne]
- **Small (Texte secondaire)**: [Taille] / [Poids] / [Interligne]

## 5. Espacement et Grille
*Base: 8px. Tous les multiples sont autorisés (8, 16, 24, 32, 48, 64, etc.). Référez-vous aux systèmes d'espacement de `getdesign.md`.*

- **Base de la grille**: 8px
- **Gouttière (Colonnes)**: [Ex: 24px, 32px]
- **Padding Section Vertical**: [Ex: 64px, 96px]
- **Padding Section Horizontal**: [Ex: 32px, 48px]
- **Radius (Arrondis)**: [Ex: 0px, 4px, 8px, 12px] (Multiples de 4px acceptés)

## 6. Composants et États
*Définissez les interactions et les variations des composants clés. Utilisez `shadcn/ui` comme base et personnalisez selon ces spécifications. Référez-vous aux directives UX de UI/UX Pro Max.*

### Boutons
- **Primaire (Normal)**: [Description visuelle: couleur de fond, texte, bordure]
- **Primaire (Hover)**: [Description visuelle: changement de couleur, ombre]
- **Secondaire (Normal)**: [Description visuelle]
- **Secondaire (Hover)**: [Description visuelle]
- **Ghost/Link (Normal)**: [Description visuelle]

### Cartes (Cards)
- **Structure**: [Ex: Fond `surface-card`, bordure `hairline`]
- **Padding Interne**: [Ex: 24px]
- **Ombre**: [Ex: `0px 4px 12px rgba(0,0,0,0.1)`]

## 7. Motion et Animations
*Timings stricts (≤ 400ms). Référez-vous aux bonnes pratiques GSAP et aux directives de UI/UX Pro Max pour des animations fluides et intentionnelles.*

- **Transitions Générales**: [Ex: 200ms ease-out]
- **Entrées d'éléments (Stagger)**: [Ex: Stagger 50ms, Duration 300ms]
- **Interactions (Hover/Click)**: [Ex: 150ms ease-in-out]
- **Accessibilité**: `prefers-reduced-motion` obligatoire.

---

## ✅ Checklist de Validation Anti-Slop

Avant livraison, vérifier:

- [ ] **DESIGN.md** : Complet et respecte toutes les sections définies.
- [ ] **Polices** : Maximum 2 polices principales, issues de paires intentionnelles.
- [ ] **Espacements** : Tous les espacements (padding, margin, gap) sont des multiples de 8px.
- [ ] **Rayons** : Tous les rayons (border-radius) sont des multiples de 4px.
- [ ] **Icônes** : Utilisation de Custom SVG ou d'un pack cohérent (pas d'icônes Lucide génériques non justifiées).
- [ ] **Gradients** : Justifiés par un rôle sémantique clair, maximum 2-3 gradients distincts.
- [ ] **Artefacts Visuels** : Absence d'emojis, stickers, ou éléments décoratifs non demandés.
- [ ] **Logos/Noms** : Pas de placeholders génériques ("your-logo", "brandname"). Utiliser du texte stylisé si aucun logo n'est fourni.
- [ ] **Structure** : Layout unique et intentionnel, pas une structure de template générique (Hero, Features, Testimonials, CTA, Pricing, FAQ, Footer).
- [ ] **Texte** : Descriptions précises, pas de buzzwords vagues ("premium", "moderne", "incroyable").
- [ ] **Boutons** : Hiérarchie claire (Primaire, Secondaire, Ghost, Destructive) avec des styles distincts.
- [ ] **Couleurs** : Palette de 4-8 couleurs avec des rôles sémantiques clairs, définies dans le DESIGN.md.
- [ ] **Animations** : Toutes les animations sont ≤ 400ms et respectent `prefers-reduced-motion`.
- [ ] **Shadcn/ui** : Composants personnalisés et non laissés par défaut.

**Exécuter l'audit automatique:**
```bash
python3 scripts/detect_ai_slop.py --design DESIGN.md --code ./client/src
python3 scripts/visual_audit.py --url http://localhost:3000 --output ./audit-results
```

Score de qualité attendu ≥ 80/100 pour la livraison.
