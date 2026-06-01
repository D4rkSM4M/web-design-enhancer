# Spécifications DESIGN.md (Format shadcn/ui)

Le fichier `DESIGN.md` est un système de design sémantique écrit en Markdown, conçu pour être lu par des agents IA afin de garantir une cohérence visuelle absolue et configurer les primitives d'interface.

## Structure Recommandée

### 1. Thème Visuel et Atmosphère
Décrit la philosophie derrière l'esthétique pour donner l'intention.
- **Exemple** : "Minimalisme brutaliste : interfaces axées sur la performance, contrastes élevés, aucune fioriture inutile."

### 2. Variables Sémantiques shadcn/ui (Palette & Rôles)
Chaque couleur et propriété structurelle doit être associée à sa variable CSS shadcn correspondante.
- **Format** : `Variable CSS`, **Valeur**, **Rôle/Usage**.
- **Exemple** :
  - `--background` : `#09090b` (Fond principal sombre)
  - `--primary` : `#ffffff` (Texte principal et boutons d'action critiques)
  - `--muted` : `#71717a` (Texte secondaire, aide et états désactivés)
  - `--border` : `#27272a` (Lignes de séparation et contours de cartes)
  - `--radius` : `0.3rem` (Rayon de courbure discret pour les boutons et cartes)

### 3. Règles Typographiques
Définit la police système moderne à utiliser et les ratios d'échelle.
- **Directives** : Forcer l'utilisation de polices épurées (`Inter`, `Geist`, `SF Pro`) et imposer un interlignage (`line-height`) proportionnel (serré pour les titres, aéré pour le texte).

### 4. Structure des Composants (shadcn/ui & Radix)
Spécifier l'usage des composants :
- "Interdiction de modifier les fichiers sources des composants installés. Toute modification esthétique doit se propager via les variables CSS sémantiques ou l'utilisation stricte des variants natifs (`variant="outline"`, `variant="ghost"`)."

### 5. Motion et Orchestration (GSAP)
Décrire le comportement dynamique lié aux animations GSAP.
- Associer les classes d'animation (ex: `.animate-fade-in`, `.animate-stagger-card`) aux règles de timing de `gsap-best-practices.md`.

## Utilisation
Placer `DESIGN.md` à la racine du projet. L'agent doit impérativement lire ce fichier et mapper ses valeurs aux fichiers de configuration (Tailwind, globals.css) avant toute implémentation.
