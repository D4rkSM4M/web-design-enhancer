# "AI Slop" Antipatterns Guide - Concrete Examples

This guide shows the common antipatterns of AI-generated design and how to avoid them.

---

## 1. Generic Lucide Icons

### ❌ BAD - AI Slop

```tsx
import { Sparkles, Zap, Cog, Network, ArrowRight } from 'lucide-react';

export function Features() {
  return (
    <>
      <div>
        <Sparkles className="w-6 h-6" />
        <h3>General Intelligence</h3>
      </div>
      <div>
        <Zap className="w-6 h-6" />
        <h3>Automation</h3>
      </div>
      <div>
        <Cog className="w-6 h-6" />
        <h3>Integrations</h3>
      </div>
    </>
  );
}
```

**Why it's bad:**
- Generic Lucide icons = "obviously AI"
- No visual consistency
- No semantic justification
- Same style as 10,000 other sites

### ✅ GOOD - Custom SVG or Consistent Pack

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

**Option 2: Consistent icon pack**
```tsx
// Use a unified pack: Feather, Heroicons, Tabler
import { Brain, Zap, Link2 } from 'feather-icons-react';

// Or build a custom pack:
// icons/index.ts with all project SVGs
```

**Benefits:**
- ✅ Unique and memorable
- ✅ Consistent with the design
- ✅ Not "obviously AI"
- ✅ Controllable (colors, sizes, styles)

---

## 2. Cliché Gradients

### ❌ BAD - AI Slop

```css
/* Stereotypical "tech" gradients */
.hero {
  background: linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%);
  /* Blue → Purple: seen 10,000 times */
}

.accent {
  background: linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%);
  /* Pink → Purple: seen 10,000 times */
}

.secondary {
  background: linear-gradient(135deg, #06B6D4 0%, #3B82F6 100%);
  /* Cyan → Blue: seen 10,000 times */
}
```

**Why it's bad:**
- Cliché gradients = "obviously AI"
- No semantic justification
- Visual overload
- No consistency with the palette

### ✅ GOOD - Intentional Gradients

```css
/* Gradients justified by semantic role */

/* Hero gradient: Primary background → Secondary accent */
.hero {
  background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
  /* Deep Navy → Slate: creates depth without distraction */
}

/* CTA gradient: Primary → Secondary (action) */
.cta-section {
  background: linear-gradient(135deg, #3B82F6 0%, #06B6D4 100%);
  /* Electric Blue → Cyan: indicates an action, justified */
}

/* Accent Glow: Primary with opacity */
.glow {
  background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, transparent 70%);
  /* Subtle halo, not cliché */
}
```

**Benefits:**
- ✅ Each gradient has a role
- ✅ No visual overload
- ✅ Consistent with the palette
- ✅ Semantically justified

---

## 3. Poorly Paired Fonts

### ❌ BAD - AI Slop

```html
<!-- 3+ fonts = chaos -->
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Inter:wght@400;500&family=JetBrains+Mono:wght@400&family=Playfair+Display:wght@700&family=Poppins:wght@600&display=swap" rel="stylesheet">

<style>
  h1 { font-family: 'Playfair Display'; } /* Elegant serif */
  h2 { font-family: 'Poppins'; } /* Rounded geometric */
  h3 { font-family: 'Sora'; } /* Modern geometric */
  p { font-family: 'Inter'; } /* Neutral */
  code { font-family: 'JetBrains Mono'; } /* Monospace */
</style>
```

**Why it's bad:**
- 5 fonts = "obviously AI"
- No visual consistency
- Confusing hierarchy
- Slow loading

### ✅ GOOD - 2 Intentional Fonts

```html
<!-- Exactly 2 fonts -->
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

<style>
  /* Display: Sora (modern, geometric) */
  h1, h2, h3 { font-family: 'Sora'; font-weight: 600; }
  
  /* Body: Inter (neutral, readable) */
  p, span, label { font-family: 'Inter'; font-weight: 400; }
  
  /* Code: Monospace (optional) */
  code { font-family: 'Courier New'; } /* Or JetBrains Mono only if really needed */
</style>
```

**Benefits:**
- ✅ Consistent and professional
- ✅ Fast loading
- ✅ Clear hierarchy
- ✅ Not "obviously AI"

---

## 4. Inconsistent Spacing

### ❌ BAD - AI Slop

```css
/* Random spacing values */
.card {
  padding: 16px; /* Not a multiple of 8 */
  margin-bottom: 13px; /* Not a multiple of 8 */
  border-radius: 6px; /* Not a multiple of 4 */
}

.button {
  padding: 11px 18px; /* Not multiples of 8 */
  border-radius: 7px; /* Not a multiple of 4 */
  margin-right: 15px; /* Not a multiple of 8 */
}

.section {
  padding: 42px 0; /* Not a multiple of 8 */
  margin-top: 25px; /* Not a multiple of 8 */
}
```

**Why it's bad:**
- Random spacing = "obviously AI"
- No visual consistency
- Hard to maintain
- No mathematical harmony

### ✅ GOOD - Strict 8px Grid

```css
/* All spacing values = multiples of 8px */
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

**Benefits:**
- ✅ Mathematical harmony
- ✅ Easy to maintain
- ✅ Consistent everywhere
- ✅ Not "obviously AI"

---

## 5. Generic Template Structure

### ❌ BAD - AI Slop

```tsx
// Classic template structure = "obviously AI"
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

**Why it's bad:**
- Identical structure to 10,000 other sites
- No unique identity
- "Clearly generated"
- No creative intent

### ✅ GOOD - Unique and Intentional Structure

```tsx
// Structure tailored to the project
export default function Home() {
  return (
    <>
      {/* Hero: Unique presentation */}
      <HeroWithAnimatedBackground />
      
      {/* Capabilities: Asymmetric layout */}
      <CapabilitiesWithScrollReveal />
      
      {/* Social Proof: Integrated testimonials */}
      <IntegratedSocialProof />
      
      {/* CTA: Customized */}
      <CustomCTAExperience />
      
      {/* Footer: Minimal and intentional */}
      <MinimalFooter />
    </>
  );
}
```

**Benefits:**
- ✅ Unique and memorable
- ✅ Intentional and thoughtful
- ✅ Not "obviously AI"
- ✅ Distinct identity

---

## 6. Vague Buzzwords

### ❌ BAD - AI Slop

```markdown
# Manus: The Premium and Modern AI

Discover an **elegant** and **innovative** experience.

## Beautiful Capabilities
- **Incredible** general intelligence
- **Unique** automation
- **Futuristic** integrations

Join **satisfied** users for a **premium** experience.
```

**Why it's bad:**
- Vague buzzwords = "obviously AI"
- No concrete information
- No differentiation
- Lack of credibility

### ✅ GOOD - Precise Descriptions

```markdown
# Manus: Accessible General Intelligence

Automate your tasks with an AI capable of performing any action on your computer.

## Concrete Capabilities
- **Complex problem solving**: Data analysis, code generation, deep research
- **Workflow automation**: Task orchestration, tool synchronization, API integrations
- **Content creation**: Writing, editing, SEO optimization

Used by professionals to **save 10+ hours per week** through automation.
```

**Benefits:**
- ✅ Precise descriptions
- ✅ Concrete benefits
- ✅ Credibility
- ✅ Not "obviously AI"

---

## 7. Uniform Buttons

### ❌ BAD - AI Slop

```tsx
// All buttons identical
<button className="btn-primary">Click</button>
<button className="btn-primary">Send</button>
<button className="btn-primary">Confirm</button>
<button className="btn-primary">Continue</button>
```

**Why it's bad:**
- No visual hierarchy
- No intentional variation
- "Clearly designed by AI"

### ✅ GOOD - Intentional Hierarchy

```tsx
{/* Primary button: Important action */}
<button className="btn-primary">Try for Free</button>

{/* Secondary button: Alternative action */}
<button className="btn-secondary">Watch the Demo</button>

{/* Ghost button: Tertiary action */}
<button className="btn-ghost">Documentation</button>

{/* Destructive button: Dangerous action */}
<button className="btn-destructive">Delete</button>
```

**Benefits:**
- ✅ Clear hierarchy
- ✅ Intentional
- ✅ Not "obviously AI"

---

## 8. Emojis in UI Chrome (A1)

### ❌ BAD - AI Slop

```html
<!-- Emojis in headings and buttons = immediately recognizable as AI -->
<h2>✨ Nos fonctionnalités</h2>
<button>🚀 Démarrer maintenant</button>
<li>📊 Tableau de bord</li>
<span class="badge">⚡ Premium</span>
```

**Why it's bad:**
- Emojis render differently across OS, browser, font
- Cannot be styled (color, size independent of text)
- Universally recognized AI signature
- Breaks screen reader pronunciation

### ✅ GOOD - Inline SVG or No Icon

```html
<!-- Inline SVG: controllable, accessible, consistent -->
<h2>
  <svg aria-hidden="true" width="20" height="20">...</svg>
  Nos fonctionnalités
</h2>
<button type="button">Démarrer</button>
<li>Tableau de bord</li>
```

---

## 9. Hardcoded Fake Statistics (A2)

### ❌ BAD - AI Slop

```html
<!-- Numbers invented by the model — unverifiable, liability -->
<div class="stat">10,000+ utilisateurs satisfaits</div>
<div class="stat">99.9% de disponibilité garantie</div>
<div class="stat">500ms temps de réponse moyen</div>
```

**Why it's bad:**
- Numbers are invented — legal liability
- Will be wrong the moment real data exists
- Screams "AI wrote this"

### ✅ GOOD - Real data or no stats

```html
<!-- Loaded from API/CMS -->
<div class="stat" data-stat-key="user_count">Chargement...</div>
<!-- Or: simply remove stats section until real data is available -->
```

---

## 10. Invented Trusted-By / Testimonial Sections (A3-A4)

### ❌ BAD - AI Slop

```html
<!-- Section invented entirely, no real data -->
<section class="trusted-by">
  <img src="/logos/google.svg" alt="Google" />
  <img src="/logos/microsoft.svg" alt="Microsoft" />
</section>

<blockquote>
  "Ce produit a changé notre façon de travailler."
  <cite>— Sarah Dupont, CEO de TechCorp</cite>
</blockquote>
```

**Why it's bad:**
- Fictitious social proof = misleading and potentially illegal
- Sarah Dupont does not exist
- AI hallucinated a business you don't have

### ✅ GOOD - Real data only, or omit entirely

```html
<!-- Only render when real data is provided by CMS/API -->
<!-- If no real testimonials exist: remove the section entirely -->
<!-- Note in structural-lock.md: "Testimonials: stub ready, awaiting real data" -->
```

---

## 11. `!important` Abuse and Arbitrary z-index (B4-B5)

### ❌ BAD - AI Slop

```css
/* Patching cascade failures with !important instead of fixing specificity */
.card {
  margin: 0 !important;
  display: flex !important;
}

/* Arbitrary z-index with no documented rationale */
.modal    { z-index: 9999; }
.overlay  { z-index: 9998; }
.tooltip  { z-index: 999999; }
```

**Why it's bad:**
- `!important` signals the cascade is broken, not fixed
- Arbitrary z-index values are unmanageable at scale

### ✅ GOOD - Fixed cascade, documented z-index scale

```css
/* Fix: increase specificity correctly */
.surface .card { margin: 0; display: flex; }

/* DESIGN.md §5 — z-index scale */
:root {
  --z-base:    1;
  --z-raised:  10;
  --z-overlay: 100;
  --z-modal:   200;
  --z-toast:   300;
}
.modal   { z-index: var(--z-modal); }
.overlay { z-index: var(--z-overlay); }
```

---

## 12. Accessibility Violations (C1-C4)

### ❌ BAD - AI Slop

```html
<!-- C1: img without alt -->
<img src="/hero.jpg" />

<!-- C2: button without type -->
<button>Envoyer</button>

<!-- C3: input without label -->
<input type="email" placeholder="Votre email" />

<!-- C4: div with click but not keyboard accessible -->
<div class="card" onclick="openModal()">Voir détails</div>
```

**Why it's bad:**
- Screen readers cannot describe unlabelled images
- `<button>` without `type` defaults to `submit` — breaks non-form buttons
- Placeholder is not a label — disappears on input
- `<div onclick>` is invisible to keyboard and assistive technology

### ✅ GOOD - Fully accessible markup

```html
<!-- C1: descriptive alt -->
<img src="/hero.jpg" alt="Équipe au travail dans un bureau lumineux" />
<!-- Decorative: empty alt string, NOT omitted -->
<img src="/decoration.svg" alt="" />

<!-- C2: explicit type -->
<button type="submit">Envoyer</button>
<button type="button" onclick="reset()">Réinitialiser</button>

<!-- C3: associated label -->
<label for="email">Adresse email</label>
<input type="email" id="email" placeholder="nom@exemple.com" />

<!-- C4: real button -->
<button type="button" onclick="openModal()">Voir détails</button>
```

---

## 13. Scope Creep (D1)

### ❌ BAD - AI Slop

```
Brief: "Create a product landing page with hero, features, and contact form."

AI generates:
- /index.html         ← requested
- /dashboard.html     ← NOT requested
- /admin.html         ← NOT requested
- /analytics.html     ← NOT requested
```

**Why it's bad:**
- Unrequested code must be reviewed, tested, maintained
- May conflict with existing architecture decisions
- Reveals the model "imagined" a product instead of reading the brief

### ✅ GOOD - Strict brief adherence

```
Brief: "Create a product landing page with hero, features, and contact form."

Generates:
- /index.html   ← hero + features + contact form (exactly what was asked)

Note in structural-lock.md:
"Scope: single-page landing. Dashboard, admin = out of scope."
```

---

## ✅ Antipatterns Checklist

Before delivery, verify:

**G-group — Visual/UI signatures**
- [ ] **Icons**: Custom SVG or consistent pack (not random Lucide)
- [ ] **Gradients**: Justified by role, max 2-3 gradients
- [ ] **Fonts**: Exactly 2 (display + body)
- [ ] **Spacing**: All multiples of 8px
- [ ] **Radii**: All multiples of 4px
- [ ] **Structure**: Unique and intentional (not a template)
- [ ] **Text**: Precise descriptions (no buzzwords, no emojis in headings)
- [ ] **Buttons**: Clear hierarchy (max 3 variants), always `type` attribute
- [ ] **Colors**: 4-8 with semantic roles
- [ ] **Animations**: All ≤ 400ms, none unsolicited
- [ ] **Status badges**: No OPTIMAL/STABLE/OFFLINE pills unless in spec
- [ ] **Monospace fonts**: Only on `<code>`, `<pre>`, `<kbd>` elements

**A-group — Content authenticity**
- [ ] **Emojis**: None in headings, buttons, nav or status labels
- [ ] **Fake stats**: No `10,000+ users`, `99.9% uptime` unless from real data source
- [ ] **Trusted-by section**: Not present unless real partner logos supplied
- [ ] **Testimonials**: Not present unless real CMS/API data supplied
- [ ] **Lorem ipsum**: No placeholder text in any delivered file
- [ ] **Placeholder images**: No `picsum.photos`, `via.placeholder.com`, `dummyimage.com`

**B-group — CSS quality**
- [ ] **`!important`**: Not used on layout properties — cascade fixed instead
- [ ] **z-index**: Only values documented in DESIGN.md §5, no 9999/99999
- [ ] **Inline styles**: None on structural/layout properties

**C-group — Accessibility (WCAG 2.1 AA)**
- [ ] **`<img>` alt**: Every `<img>` has `alt` (empty string `alt=""` acceptable for decorative)
- [ ] **`<button>` type**: Every `<button>` has `type="button"` or `type="submit"`
- [ ] **Input labels**: Every `<input>`, `<textarea>`, `<select>` has `<label for>` or `aria-label`
- [ ] **div onclick**: No `<div onClick>` without `role="button"` + `tabIndex={0}` + `onKeyDown`
- [ ] **`<html lang>`**: Present on every page
- [ ] **`<title>`**: Present and non-empty on every page
- [ ] **Empty links**: No `<a>` without text content or `aria-label`
- [ ] **`console.log`**: None in delivered files (remove or guard with `NODE_ENV`)
- [ ] **TODO/FIXME**: No unresolved comments in delivered files

**D-group — Behavioural discipline**
- [ ] **Scope creep**: Only pages/components explicitly in the brief
- [ ] **Naming**: Component and file names unchanged from the brief
- [ ] **Mock data**: No hardcoded URLs, no `MOCK_DATA` constants in production code
- [ ] **Responsive**: Minimum 375px mobile + 1280px desktop declared and tested

**Run (full validation suite):**
```bash
python3 scripts/check.py --final --code ./src
python3 scripts/check.py --final --code ./src --verbose   # show fix instructions on failure
```

**Run (individual tools):**
```bash
python3 scripts/detect_ai_slop.py --design DESIGN.md --code ./src
python3 scripts/detect_ai_slop.py --design DESIGN.md --code ./src --json   # machine-readable
python3 scripts/audit_accessibility.py --path ./src
python3 scripts/audit_spacing.py --path ./src
```

All tools exit 0 = ✅ Delivery authorized
