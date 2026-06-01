# Guide des Antipatterns "AI Slop" - Exemples Concrets

Ce guide montre les antipatterns courants du design généré par IA et comment les éviter.

---

## 1. Icônes Génériques Lucide

### ❌ MAUVAIS - AI Slop

```tsx
import { Sparkles, Zap, Cog, Network, ArrowRight } from 'lucide-react';

export function Features() {
  return (
    <>
      <div>
        <Sparkles className="w-6 h-6" />
        <h3>Intelligence Générale</h3>
      </div>
      <div>
        <Zap className="w-6 h-6" />
        <h3>Automatisation</h3>
      </div>
      <div>
        <Cog className="w-6 h-6" />
        <h3>Intégrations</h3>
      </div>
    </>
  );
}
```

**Pourquoi c'est mauvais:**
- Icônes génériques Lucide = "obviously AI"
- Pas de cohérence visuelle
- Aucune justification sémantique
- Même style que 10,000 autres sites

### ✅ BON - Custom SVG ou Pack Cohérent

**Option 1: Custom SVG**
```tsx
// icons/BrainIcon.tsx
export function BrainIcon() {
  return (
    <svg viewBox="0 0 24 24" className="w-6 h-6">
      <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm3.5-9c.83 0 1.5-.67 1.5-1.5S16.33 8 15.5 8 14 8.67 14 9.5s.67 1.5 1.5 1.5zm-7 0c.83 0 1.5-.67 1.5-1.5S9.33 8 8.5 8 7 8.67 7 9.5 7.67 11 8.5 11zm3.5 6.5c2.33 0 4.31-1.46 5.11-3.5H6.89c.8 2.04 2.78 3.5 5.11 3.5z" />
    </svg>
  );
}
```

**Option 2: Pack d'icônes cohérent**
```tsx
// Utiliser un pack unifié: Feather, Heroicons, Tabler
import { Brain, Zap, Link2 } from 'feather-icons-react';

// Ou créer un pack custom:
// icons/index.ts avec tous les SVG du projet
```

**Avantages:**
- ✅ Unique et mémorable
- ✅ Cohérent avec le design
- ✅ Pas "obviously AI"
- ✅ Contrôlable (couleurs, tailles, styles)

---

## 2. Gradients Clichés

### ❌ MAUVAIS - AI Slop

```css
/* Gradients "tech" stéréotypés */
.hero {
  background: linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%);
  /* Bleu → Violet: vu 10,000 fois */
}

.accent {
  background: linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%);
  /* Rose → Violet: vu 10,000 fois */
}

.secondary {
  background: linear-gradient(135deg, #06B6D4 0%, #3B82F6 100%);
  /* Cyan → Bleu: vu 10,000 fois */
}
```

**Pourquoi c'est mauvais:**
- Gradients clichés = "obviously AI"
- Pas de justification sémantique
- Surcharge visuelle
- Pas de cohérence avec la palette

### ✅ BON - Gradients Intentionnels

```css
/* Gradients justifiés par rôle sémantique */

/* Gradient Hero: Fond primaire → Accent secondaire */
.hero {
  background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
  /* Deep Navy → Slate: Crée de la profondeur sans distraction */
}

/* Gradient CTA: Primaire → Secondaire (action) */
.cta-section {
  background: linear-gradient(135deg, #3B82F6 0%, #06B6D4 100%);
  /* Electric Blue → Cyan: Indique une action, justifié */
}

/* Accent Glow: Primaire avec opacité */
.glow {
  background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, transparent 70%);
  /* Halo subtil, pas cliché */
}
```

**Avantages:**
- ✅ Chaque gradient a un rôle
- ✅ Pas de surcharge visuelle
- ✅ Cohérent avec la palette
- ✅ Justifié sémantiquement

---

## 3. Polices Mal Appariées

### ❌ MAUVAIS - AI Slop

```html
<!-- 3+ polices = chaos -->
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Inter:wght@400;500&family=JetBrains+Mono:wght@400&family=Playfair+Display:wght@700&family=Poppins:wght@600&display=swap" rel="stylesheet">

<style>
  h1 { font-family: 'Playfair Display'; } /* Serif élégant */
  h2 { font-family: 'Poppins'; } /* Géométrique rond */
  h3 { font-family: 'Sora'; } /* Géométrique moderne */
  p { font-family: 'Inter'; } /* Neutre */
  code { font-family: 'JetBrains Mono'; } /* Monospace */
</style>
```

**Pourquoi c'est mauvais:**
- 5 polices = "obviously AI"
- Pas de cohérence visuelle
- Hiérarchie confuse
- Chargement lent

### ✅ BON - 2 Polices Intentionnelles

```html
<!-- Exactement 2 polices -->
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

<style>
  /* Display: Sora (moderne, géométrique) */
  h1, h2, h3 { font-family: 'Sora'; font-weight: 600; }
  
  /* Body: Inter (neutre, lisible) */
  p, span, label { font-family: 'Inter'; font-weight: 400; }
  
  /* Code: Monospace (optionnel) */
  code { font-family: 'Courier New'; } /* Ou JetBrains Mono si vraiment nécessaire */
</style>
```

**Avantages:**
- ✅ Cohérent et professionnel
- ✅ Chargement rapide
- ✅ Hiérarchie claire
- ✅ Pas "obviously AI"

---

## 4. Espacements Incohérents

### ❌ MAUVAIS - AI Slop

```css
/* Espacements aléatoires */
.card {
  padding: 16px; /* Pas multiple de 8 */
  margin-bottom: 13px; /* Pas multiple de 8 */
  border-radius: 6px; /* Pas multiple de 4 */
}

.button {
  padding: 11px 18px; /* Pas multiples de 8 */
  border-radius: 7px; /* Pas multiple de 4 */
  margin-right: 15px; /* Pas multiple de 8 */
}

.section {
  padding: 42px 0; /* Pas multiple de 8 */
  margin-top: 25px; /* Pas multiple de 8 */
}
```

**Pourquoi c'est mauvais:**
- Espacements aléatoires = "obviously AI"
- Pas de cohérence visuelle
- Difficile à maintenir
- Pas d'harmonie mathématique

### ✅ BON - Grille 8px Stricte

```css
/* Tous les espacements = multiples de 8px */
:root {
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-2xl: 48px;
  
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
}

.card {
  padding: var(--spacing-lg); /* 24px */
  margin-bottom: var(--spacing-lg); /* 24px */
  border-radius: var(--radius-lg); /* 12px */
}

.button {
  padding: var(--spacing-sm) var(--spacing-md); /* 8px 16px */
  border-radius: var(--radius-md); /* 8px */
  margin-right: var(--spacing-md); /* 16px */
}

.section {
  padding: var(--spacing-3xl) 0; /* 64px 0 */
  margin-top: var(--spacing-2xl); /* 48px */
}
```

**Avantages:**
- ✅ Harmonie mathématique
- ✅ Facile à maintenir
- ✅ Cohérent partout
- ✅ Pas "obviously AI"

---

## 5. Structure Template Générique

### ❌ MAUVAIS - AI Slop

```tsx
// Structure template classique = "obviously AI"
export default function Home() {
  return (
    <>
      <HeroSection />
      <FeaturesGrid />
      <TestimonialsSection />
      <CTASection />
      <PricingSection />
      <FAQSection />
      <Footer />
    </>
  );
}
```

**Pourquoi c'est mauvais:**
- Structure identique à 10,000 autres sites
- Pas d'identité unique
- "Clearly generated"
- Pas d'intention créative

### ✅ BON - Structure Unique et Intentionnelle

```tsx
// Structure adaptée au projet
export default function Home() {
  return (
    <>
      {/* Hero: Présentation unique */}
      <HeroWithAnimatedBackground />
      
      {/* Capacités: Layout asymétrique */}
      <CapabilitiesWithScrollReveal />
      
      {/* Social Proof: Testimonials intégrés */}
      <IntegratedSocialProof />
      
      {/* CTA: Personnalisé */}
      <CustomCTAExperience />
      
      {/* Footer: Minimal et intentionnel */}
      <MinimalFooter />
    </>
  );
}
```

**Avantages:**
- ✅ Unique et mémorable
- ✅ Intentionnel et réfléchi
- ✅ Pas "obviously AI"
- ✅ Identité propre

---

## 6. Buzzwords Vagues

### ❌ MAUVAIS - AI Slop

```markdown
# Manus: L'IA Premium et Moderne

Découvrez une expérience **élégante** et **innovante**.

## Capacités Magnifiques
- Intelligence générale **incroyable**
- Automatisation **unique**
- Intégrations **futuristes**

Rejoignez des utilisateurs **satisfaits** pour une expérience **premium**.
```

**Pourquoi c'est mauvais:**
- Buzzwords vagues = "obviously AI"
- Aucune information concrète
- Pas de différenciation
- Manque de crédibilité

### ✅ BON - Descriptions Précises

```markdown
# Manus: Intelligence Générale Accessible

Automatisez vos tâches avec une IA capable d'accomplir n'importe quelle action sur votre ordinateur.

## Capacités Concrètes
- **Résolution de problèmes complexes**: Analyse de données, génération de code, recherche approfondie
- **Automatisation de workflows**: Orchestration de tâches, synchronisation d'outils, intégrations API
- **Création de contenu**: Rédaction, édition, optimisation pour SEO

Utilisé par des professionnels pour **économiser 10+ heures par semaine** en automatisation.
```

**Avantages:**
- ✅ Descriptions précises
- ✅ Bénéfices concrets
- ✅ Crédibilité
- ✅ Pas "obviously AI"

---

## 7. Boutons Uniformes

### ❌ MAUVAIS - AI Slop

```tsx
// Tous les boutons identiques
<button className="btn-primary">Cliquer</button>
<button className="btn-primary">Envoyer</button>
<button className="btn-primary">Valider</button>
<button className="btn-primary">Continuer</button>
```

**Pourquoi c'est mauvais:**
- Pas de hiérarchie visuelle
- Pas de variation intentionnelle
- "Clearly designed by AI"

### ✅ BON - Hiérarchie Intentionnelle

```tsx
{/* Bouton principal: Action importante */}
<button className="btn-primary">Essayer Gratuitement</button>

{/* Bouton secondaire: Action alternative */}
<button className="btn-secondary">Voir la Démo</button>

{/* Bouton ghost: Action tertiaire */}
<button className="btn-ghost">Documentation</button>

{/* Bouton destructif: Action dangereuse */}
<button className="btn-destructive">Supprimer</button>
```

**Avantages:**
- ✅ Hiérarchie claire
- ✅ Intentionnel
- ✅ Pas "obviously AI"

---

## ✅ Checklist Antipatterns

Avant livraison, vérifier:

- [ ] **Icônes**: Custom SVG ou pack cohérent (pas Lucide random)
- [ ] **Gradients**: Justifiés par rôle, max 2-3 gradients
- [ ] **Polices**: Exactement 2 (display + body)
- [ ] **Espacements**: Tous multiples de 8px
- [ ] **Rayons**: Tous multiples de 4px
- [ ] **Structure**: Unique et intentionnelle (pas template)
- [ ] **Texte**: Descriptions précises (pas buzzwords)
- [ ] **Boutons**: Hiérarchie claire (3 variantes max)
- [ ] **Couleurs**: 4-8 avec rôles sémantiques
- [ ] **Animations**: Toutes ≤ 400ms

**Exécuter:**
```bash
python3 scripts/detect_ai_slop.py --design DESIGN.md --code ./client/src
```

Score ≥ 80/100 = ✅ Prêt pour livraison

