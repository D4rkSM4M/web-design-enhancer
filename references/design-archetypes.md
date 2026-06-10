# Design Archetypes Reference
> **Critical Reference Document for web-design-enhancer-pro**
> Version 1.0 — Last updated 2026-06-10

---

## Why This Document Exists

Every AI model has a gravitational pull toward the same design output: a dark hero section with a blue-to-purple gradient, a headline in Inter Bold, three white cards with box-shadows and 8px border-radius, and a purple CTA button. It is the statistical average of every SaaS landing page the model was trained on.

This template is not _bad_. It is worse: it is **invisible**. It communicates nothing about the brand, the product, or the audience. It looks like every competitor and signals to users that no design decision was made at all.

**The purpose of design archetypes is to give AI models a concrete vocabulary for making real design choices.** Each archetype in this document is:

- Visually distinctive from all others (you cannot confuse them)
- Grounded in real design history and living design systems
- Expressed in concrete CSS tokens, not vague adjectives
- Equipped with a "what destroys this style" list to prevent drift

When generating or enhancing a web design, a model MUST consult this document and select one archetype. Mixing archetypes produces the same generic output we are trying to avoid. **Commit to one. Execute it fully.**

---

## Table of Contents

1. [How to Choose an Archetype](#how-to-choose)
2. [The 10 Archetypes](#the-10-archetypes)
   - [01 — Swiss / International Typographic](#01--swiss--international-typographic)
   - [02 — Editorial / Magazine](#02--editorial--magazine)
   - [03 — Luxury / Restrained](#03--luxury--restrained)
   - [04 — Brutalist / Raw](#04--brutalist--raw)
   - [05 — Organic / Hand-crafted](#05--organic--hand-crafted)
   - [06 — Technical / Monochrome](#06--technical--monochrome)
   - [07 — Playful / Expressive](#07--playful--expressive)
   - [08 — Data / Dashboard](#08--data--dashboard)
   - [09 — Retro / Nostalgic](#09--retro--nostalgic)
   - [10 — Material / Tactile](#10--material--tactile)
3. [Forbidden Combinations](#forbidden-combinations)
4. [DESIGN.md Integration](#designmd-integration)
5. [Quick Reference Table](#quick-reference-table)

---

## How to Choose

Use the decision tree below. Answer each question in order. Stop at the first match.

```
START
│
├── Is the primary audience professionals buying expensive things (luxury goods,
│   high-end services, premium finance)?
│   └── YES → Archetype 03: Luxury / Restrained
│
├── Is the site primarily about displaying written content (news, blog, long-form)?
│   └── YES → Archetype 02: Editorial / Magazine
│
├── Is the brand explicitly 'anti-corporate', experimental, or art-adjacent?
│   └── YES → Archetype 04: Brutalist / Raw
│
├── Is the product developer-facing (CLI tools, APIs, code editors, infra)?
│   └── YES → Archetype 06: Technical / Monochrome
│
├── Is the primary deliverable data visualization or a live dashboard?
│   └── YES → Archetype 08: Data / Dashboard
│
├── Is the brand in wellness, food, artisan crafts, or 'slow living'?
│   └── YES → Archetype 05: Organic / Hand-crafted
│
├── Is the brand targeting Gen Z, creative communities, or education (fun)?
│   └── YES → Archetype 07: Playful / Expressive
│
├── Is the brand nostalgic, retro-themed, or explicitly referencing a past era?
│   └── YES → Archetype 09: Retro / Nostalgic
│
├── Is the brand a traditional institution, cultural, or values graphic design?
│   └── YES → Archetype 01: Swiss / International Typographic
│
└── DEFAULT (product/SaaS/tool with neutral positioning)
    └── Archetype 10: Material / Tactile
    ← NOTE: Even the default is NOT the dark gradient template.
```

### Secondary Modifiers

After choosing a primary archetype, apply these modifiers if relevant:

| Condition | Modifier |
|-----------|----------|
| Product is B2B enterprise | Reduce radius by 2px; increase font weight for headings |
| Product is consumer-facing | Increase whitespace; soften color palette |
| Brand has strong illustration | Ensure archetype allows illustration (05, 07 do; 06, 08 do not) |
| Brand is international / multilingual | Prefer archetypes with generous line-height (02, 03, 10) |
| Dark mode is required | Archetypes 04, 06, 08 have natural dark variants; others need adaptation |

---

## The 10 Archetypes

---

### 01 — Swiss / International Typographic

> *"The grid is not a cage. It is a skeleton."* — Josef Müller-Brockmann

#### Overview

The Swiss International Style emerged in the 1950s from Zurich and Basel. It champions mathematical grid systems, objective photography, and typographic hierarchy as the primary (often only) visual tool. It is the opposite of decoration: every element earns its place by communicating, not by looking nice.

Modern digital applications: Helvetica Now website, Swiss government digital services, some financial institutions (Julius Baer), architecture firms.

#### Visual Signature

- **Grid:** strict 12-column with visible (or implied) column gutters
- **Typography:** massive weight contrast — headlines at 900 weight dominate; body is regular weight at comfortable reading size
- **Color:** maximum 2 neutrals + 1 pure primary accent. No tints. No shades. The accent is either `#FF0000` (red), `#FFDD00` (yellow), or `#0033CC` (blue)
- **Layout:** asymmetric compositions within a symmetric grid; text can bleed into image areas
- **Imagery:** either photographic (not illustrated) or diagrammatic. No stock photos of people smiling.
- **Motion:** none, or purely functional (page transitions only)

#### CSS Tokens

```css
:root {
  /* Colors */
  --color-bg:       #FFFFFF;
  --color-surface:  #F5F5F5;
  --color-text:     #000000;
  --color-muted:    #4A4A4A;
  --color-accent:   #FF0000;   /* OR #FFDD00 OR #0033CC — pick ONE, never all three */

  /* Typography */
  --font-display:   'Inter', 'Helvetica Neue', Arial, sans-serif;
  --font-body:      'Inter', 'Helvetica Neue', Arial, sans-serif;
  --font-weight-display: 900;
  --font-weight-body:    400;
  --font-size-hero: clamp(4rem, 10vw, 9rem);
  --font-size-h2:   clamp(2rem, 5vw, 4rem);
  --font-size-body: 1rem;
  --line-height-display: 0.95;
  --line-height-body:    1.6;
  --letter-spacing-display: -0.04em;
  --letter-spacing-caps:     0.12em;

  /* Spacing */
  --space-unit:   8px;
  --section-gap:  clamp(80px, 12vw, 160px);
  --column-gutter: 24px;

  /* Shape */
  --radius:      0px;
  --radius-sm:   0px;
  --radius-lg:   0px;

  /* Effects */
  --shadow-none: none;
}
```

#### Layout Patterns

```
[HERO]
┌─────────────────────────────────────────────────────────┐
│  ░░░░░░░░░░░░░░░  MASSIVE HEADLINE TEXT                 │
│                    IN 900 WEIGHT THAT                   │
│                    COMMANDS ATTENTION     [■ ACCENT]    │
├─────────────────────────────────────────────────────────┤
│  Subhead in regular weight ·  Date or category label    │
└─────────────────────────────────────────────────────────┘

[CONTENT BLOCK — asymmetric 7/5 split]
┌────────────────────────┬────────────────────────────────┐
│  ████████████████████  │  Section header in 900         │
│  ████████████████████  │                                │
│  ██████ (image)        │  Body text in regular weight   │
│  ████████████████████  │  with generous line-height.    │
│                        │  No decorative elements.       │
└────────────────────────┴────────────────────────────────┘
```

#### Forbidden Patterns

- ❌ Gradients of any kind (linear, radial, mesh)
- ❌ Glassmorphism (`backdrop-filter: blur`)
- ❌ `box-shadow` on cards or buttons
- ❌ `border-radius` > 0px on any structural element
- ❌ Emojis in headings or body copy
- ❌ Illustrations or icons (use photography or nothing)
- ❌ More than one accent color
- ❌ Tints or shades of the accent (pure color only)
- ❌ Centered hero text layouts
- ❌ Testimonial cards with avatar photos

#### Real-World References

- [Neue Grafik magazine archives](https://www.lars-mueller-publishers.com/)
- Swiss Federal Design Awards website
- [Helvetica (2007) documentary visual language](https://www.hustwit.com/helvetica)
- Knoll furniture brand website
- [Swiss typefaces foundry](https://www.swisstypefaces.com/)

---

### 02 — Editorial / Magazine

> *"A great publication gives you the sense that someone intelligent curated it for you."*

#### Overview

Editorial design treats the web like a page in a premium print publication. Hierarchy is expressed through typography, not color. Whitespace is not empty — it is the breathing room that gives each element its weight. The reader trusts this design because it respects their intelligence.

Modern digital applications: The Guardian, The New York Times, MIT Technology Review, Rest of World, Monocle.

#### Visual Signature

- **Typography as UI:** column spans, pull quotes, drop caps, running heads
- **Photograph:** large, full-bleed editorial photography (not stock, not illustrated)
- **Rhythm:** consistent vertical rhythm based on line-height multiples
- **Color:** near-neutral palette; accents are muted (deep red, navy, forest) not bright
- **Whitespace:** generous — margins wider than most sites, section gaps taller
- **Cards:** do not exist. Content is laid out in columns and rows, not card containers.

#### CSS Tokens

```css
:root {
  /* Colors */
  --color-bg:        #FFFDF7;   /* warm cream */
  --color-surface:   #F5F2EC;
  --color-text:      #1A1A1A;   /* near-black, not pure */
  --color-muted:     #6B6B6B;
  --color-rule:      #D4CFC7;   /* for hr and dividers */
  --color-accent:    #B5271F;   /* deep editorial red — OR #1B3A6B navy OR #2D5016 forest */

  /* Typography */
  --font-display:    'Playfair Display', 'Lora', Georgia, serif;
  --font-body:       'Inter', 'Source Serif 4', sans-serif;
  --font-caption:    'Inter', sans-serif;
  --font-weight-display: 700;
  --font-weight-body:    400;
  --font-size-hero:  clamp(2.5rem, 6vw, 5rem);
  --font-size-h2:    clamp(1.75rem, 3.5vw, 2.75rem);
  --font-size-body:  1.0625rem;  /* 17px */
  --font-size-caption: 0.8125rem;
  --line-height-display: 1.1;
  --line-height-body:    1.75;
  --letter-spacing-display: -0.02em;
  --letter-spacing-caption:  0.06em;

  /* Spacing */
  --space-unit:      8px;
  --section-gap:     clamp(64px, 10vw, 128px);
  --reading-width:   720px;    /* max prose column width */
  --column-gutter:   32px;

  /* Shape */
  --radius:    2px;
  --radius-sm: 0px;
  --radius-lg: 4px;

  /* Effects */
  --shadow-card: none;         /* editorial layouts don't use card shadows */
  --border-rule: 1px solid var(--color-rule);
}
```

#### Layout Patterns

```
[HERO — full-bleed editorial]
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  ████████████████████████████████ (full-bleed image)   │
│                                                         │
│  CATEGORY LABEL  ·  Date                               │
│                                                         │
│  Headline in Serif Display,                             │
│  Set Across 8 of 12 Columns                             │
│                                                         │
│  Byline / subhead in regular weight sans                │
└─────────────────────────────────────────────────────────┘

[ARTICLE LIST — no cards, just typography]
SECTION HEADER ──────────────────────────────
│
├── Story headline in serif / Date / Tag
│   First paragraph as teaser...
│   [read more →]
│
├── ────────────────── (rule)
│
├── Story headline in serif / Date / Tag
│   First paragraph as teaser...
```

#### Forbidden Patterns

- ❌ Dark hero sections (hero is always light/cream)
- ❌ Cards with `box-shadow` and `border-radius`
- ❌ Blue/purple gradient CTAs
- ❌ Tech-style typography (monospace, geometric sans for display)
- ❌ Grid of identical 3-column cards
- ❌ Emoji in headlines or body
- ❌ Stock photography of diverse teams smiling
- ❌ Floating UI mockup images
- ❌ Testimonial carousel widgets
- ❌ Sticky animated headers with blur

#### Real-World References

- [The Guardian](https://www.theguardian.com/)
- [MIT Technology Review](https://www.technologyreview.com/)
- [Rest of World](https://restofworld.org/)
- [Monocle](https://www.monocle.com/)
- [The Intercept](https://theintercept.com/)

---

### 03 — Luxury / Restrained

> *"Elegance is refusal."* — Coco Chanel

#### Overview

Luxury design communicates value through absence. The whitespace is expensive. The typography is quiet. There are no urgent CTAs, no flashing badges, no countdown timers. The brand assumes you will come to it — not the other way around. Every pixel of decoration removed is a signal of confidence.

Modern digital applications: Chanel, Bottega Veneta, Aesop cosmetics, The Row, Brunello Cucinelli, Patek Philippe.

#### Visual Signature

- **Extreme whitespace:** margins of 15–20% of viewport width
- **Minimal type scale:** body text smaller than most sites (14–15px); headings restrained
- **No above-fold CTA:** the first viewport has no button, no form, no urgency
- **Uppercase with tracking:** labels and categories in small caps with generous letter-spacing
- **Material photography:** product photography on clean backgrounds, or atmospheric lifestyle
- **Animation:** none, or fade-in at near-imperceptible speed (2–4 seconds)

#### CSS Tokens

```css
:root {
  /* Colors */
  --color-bg:          #FAF8F4;   /* warm parchment */
  --color-surface:     #F0EDE6;
  --color-text:        #2C2C2C;   /* charcoal, not pure black */
  --color-muted:       #8A8279;
  --color-accent:      #B8945F;   /* warm gold — OR #8C7355 bronze OR #6B5B4E deep sand */
  --color-border:      #E0DBD3;

  /* Typography */
  --font-display:      'Cormorant Garamond', 'EB Garamond', 'Playfair Display', serif;
  --font-body:         'Jost', 'Raleway', 'Inter', sans-serif;
  --font-weight-display: 300;     /* thin/light for luxury */
  --font-weight-body:    300;
  --font-weight-label:   400;
  --font-size-hero:    clamp(2rem, 4vw, 3.5rem);   /* intentionally small for hero */
  --font-size-h2:      clamp(1.25rem, 2.5vw, 2rem);
  --font-size-body:    0.9375rem;  /* 15px */
  --font-size-label:   0.6875rem;  /* 11px */
  --line-height-display: 1.2;
  --line-height-body:    1.85;
  --letter-spacing-display: 0.04em;
  --letter-spacing-label:   0.18em;   /* wide tracking for uppercase labels */

  /* Spacing */
  --section-gap:       clamp(120px, 18vw, 240px);
  --content-margin:    clamp(60px, 15vw, 200px);   /* generous side margins */
  --element-gap:       40px;

  /* Shape */
  --radius:    0px;
  --radius-sm: 0px;
  --radius-lg: 2px;   /* only on images */

  /* Effects */
  --shadow-none:       none;
  --transition-slow:   all 0.4s ease;
}
```

#### Layout Patterns

```
[HERO — no CTA, just brand statement]
                                                    
          ┌──────────────────────────────┐          
          │                              │          
          │   ████████████████████████  │          
          │   ████████ (portrait image) │          
          │   ████████████████████████  │          
          │                              │          
          └──────────────────────────────┘          
                                                    
              BRAND COLLECTION · SEASON              
                                                    
              A single restraining line              
              of refined typographic thought.        
                                                    

[PRODUCT — centered, generous negative space]

   ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  

              THE OBJECT                            
              ──────────────────                    
              Brief description in                  
              light weight type.                    
                                                    
              EXPLORE →                             
                                                    
   ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  
```

#### Forbidden Patterns

- ❌ Bright colors or saturated hues
- ❌ Large, bold, attention-grabbing headlines
- ❌ Gradient backgrounds or buttons
- ❌ Animations (especially entrance animations, parallax, particle effects)
- ❌ Emojis anywhere
- ❌ Testimonial sections with star ratings
- ❌ Countdown timers, sale badges, urgency copy
- ❌ Newsletter popups
- ❌ Social proof numbers ("Join 50,000 users")
- ❌ Feature lists in bullet form
- ❌ Chatbot widgets
- ❌ Cookie consent banners that break the layout

#### Real-World References

- [Aesop](https://www.aesop.com/)
- [Bottega Veneta](https://www.bottegaveneta.com/)
- [The Row](https://www.therow.com/)
- [Brunello Cucinelli](https://www.brunellocucinelli.com/)
- [Patek Philippe](https://www.patek.com/)

---

### 04 — Brutalist / Raw

> *"The building should be the machine for living."* — Le Corbusier (adapted for web)

#### Overview

Brutalism in web design exposes structure rather than hiding it. Navigation is functional, not decorative. Borders replace shadows. Monospace type references the terminal. The aesthetic is honest about being a website made of code — it does not pretend to be a polished magazine or a physical object. It is deliberately anti-trend.

Modern digital applications: Bloomberg (editorial pages), Balenciaga, Are.na, Cargo Collective, many independent studios and artists.

#### Visual Signature

- **Visible grid:** column borders, grid lines, structural outlines
- **Monospace or grotesque type:** the type choice signals code, not luxury
- **Borders not shadows:** `border: 1px solid #000` instead of `box-shadow`
- **Collage-like layouts:** elements overlap, stack, or crowd each other
- **Raw cursor interactions:** links underlined, hover states are visible and functional
- **One electric accent:** not a gradient, but a single sharp color used sparingly

#### CSS Tokens

```css
:root {
  /* Colors */
  --color-bg:       #FFFFFF;
  --color-surface:  #F0F0F0;
  --color-text:     #000000;
  --color-muted:    #555555;
  --color-accent:   #FF4500;   /* electric orange — OR #00FF41 terminal green OR #FFE600 warning yellow */
  --color-border:   #000000;

  /* Typography */
  --font-display:   'Space Mono', 'Courier New', 'IBM Plex Mono', monospace;
  --font-body:      'Space Grotesk', 'Aktiv Grotesk', 'Arial', sans-serif;
  --font-weight-display: 700;
  --font-weight-body:    400;
  --font-size-hero:  clamp(2.5rem, 7vw, 6rem);
  --font-size-h2:    clamp(1.5rem, 3vw, 2.5rem);
  --font-size-body:  0.9375rem;
  --line-height-display: 1.0;
  --line-height-body:    1.55;
  --letter-spacing-display: -0.02em;

  /* Spacing */
  --section-gap:    clamp(40px, 6vw, 80px);   /* tighter than editorial */
  --column-gutter:  16px;
  --border-width:   1px;
  --border-heavy:   3px;

  /* Shape */
  --radius:    0px;
  --radius-sm: 0px;
  --radius-lg: 0px;

  /* Effects */
  --shadow-none:  none;
  --border-ui:    var(--border-width) solid var(--color-border);
  --border-ui-heavy: var(--border-heavy) solid var(--color-border);
}
```

#### Layout Patterns

```
[NAVIGATION — exposed, functional]
┌────────────────────────────────────────────────────────┐
│ SITE.NAME       WORK  ABOUT  WRITING  CONTACT          │
└────────────────────────────────────────────────────────┘
 ← border separates, not shadow →

[HERO — asymmetric, type-heavy]
┌──────────────────────────┬───────────────────────────┐
│ INDEX_001                │ ████████ image or void ██ │
│                          │                           │
│ RAW_HEADLINE_TEXT        │                           │
│ SPANS_HERE               │ 001 / Ongoing             │
│                          │ Project description       │
│ [VIEW WORK ↗]            │ in grotesque type         │
└──────────────────────────┴───────────────────────────┘

[GRID — bordered cells, no cards]
┌──────────────┬──────────────┬──────────────┐
│ [01]         │ [02]         │ [03]         │
│ ████████████ │ ████████████ │ ████████████ │
│ Title        │ Title        │ Title        │
│ Date · Tag   │ Date · Tag   │ Date · Tag   │
└──────────────┴──────────────┴──────────────┘
```

#### Forbidden Patterns

- ❌ Rounded corners (`border-radius` > 0px)
- ❌ `box-shadow` on any element
- ❌ Glassmorphism or frosted glass
- ❌ Gradient backgrounds or gradient buttons
- ❌ Emojis in content
- ❌ Smooth, polished animations (slide-in, fade cards)
- ❌ Stock illustrations or icon packs
- ❌ Testimonials with circular avatar photos
- ❌ Section background alternating patterns (white/gray/white)

#### Real-World References

- [Are.na](https://www.are.na/)
- [Cargo Collective](https://cargo.site/)
- [Bloomberg Businessweek design](https://www.bloomberg.com/businessweek)
- [Balenciaga](https://www.balenciaga.com/)
- [HORT studio](https://www.hort.org.uk/)

---

### 05 — Organic / Hand-crafted

> *"Imperfection is beauty."*

#### Overview

This archetype reacts against the cold precision of tech design. It embraces warmth, imperfection, and the analog. Shapes are organic (blobs, brush strokes, wavy dividers), typography is expressive, colors are earthy and warm. The design feels like something a human made with care — not a template a machine generated.

Modern digital applications: Mailchimp (pre-2022), Notion (adjacent), Oat the Goat, wellness brands, artisan food producers, Patagonia.

#### Visual Signature

- **Warm neutral palette:** sand, terracotta, sage, cream — no pure black
- **Organic shapes:** SVG blob dividers, wavy section transitions, irregular masks
- **Expressive typography:** variable fonts with personality; headlines have soul
- **Imperfect grid:** intentional asymmetry; elements slightly off-grid
- **Illustration:** hand-drawn or brush-textured elements encouraged
- **Texture:** paper grain, linen, or subtle noise overlay on backgrounds

#### CSS Tokens

```css
:root {
  /* Colors */
  --color-bg:         #F5EFE0;   /* warm sand */
  --color-surface:    #EDE4CE;
  --color-surface-alt: #FDFAF5;
  --color-text:       #2A2217;   /* warm near-black */
  --color-muted:      #7A6E5F;
  --color-accent-1:   #C4614A;   /* terracotta */
  --color-accent-2:   #3D5A44;   /* forest green */
  --color-accent-3:   #E8C87A;   /* golden yellow */
  --color-border:     #D4C9B0;

  /* Typography */
  --font-display:   'Fraunces', 'Cormorant', 'Playfair Display', serif;
  --font-body:      'Cabinet Grotesk', 'DM Sans', 'Inter', sans-serif;
  --font-weight-display: 600;    /* semi-bold, not aggressive */
  --font-weight-body:    400;
  --font-size-hero:  clamp(2.5rem, 6vw, 5rem);
  --font-size-h2:    clamp(1.75rem, 3.5vw, 3rem);
  --font-size-body:  1.0625rem;
  --line-height-display: 1.15;
  --line-height-body:    1.75;
  --letter-spacing-display: -0.01em;

  /* Spacing */
  --section-gap:    clamp(80px, 10vw, 160px);
  --element-gap:    32px;
  --column-gutter:  28px;

  /* Shape */
  --radius:    16px;
  --radius-sm: 8px;
  --radius-lg: 24px;
  --radius-pill: 999px;

  /* Effects */
  --shadow-soft: 0 2px 20px rgba(42, 34, 23, 0.08);
  --texture-overlay: url("data:image/svg+xml,...");  /* subtle noise */
}
```

#### Layout Patterns

```
[HERO — warm, inviting, not tech]
┌─────────────────────────────────────────────────────────┐
│   ╭─────────────────────────────────────╮               │
│   │  Illustrated or photography area    │  Headline     │
│   │  with organic mask / blob shape     │  in serif     │
│   │                                     │  display      │
│   ╰─────────────────────────────────────╯               │
│                                                         │
│   Short, warm copy in body font.                        │
│   [Explore →]  ← text link, no hard button             │
└─────────────────────────────────────────────────────────┘

[WAVY DIVIDER between sections]
≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
```

#### Forbidden Patterns

- ❌ Dark backgrounds (especially pure black or #09090B)
- ❌ Neon or electric colors
- ❌ Sharp geometric shapes (hard rectangles as decorative elements)
- ❌ Particle animations or WebGL effects
- ❌ Tech iconography (code brackets, terminal, circuit boards)
- ❌ Monospace fonts as display type
- ❌ Cold/blue color palette
- ❌ "3 features, each with an icon" grid
- ❌ Generic tech SaaS copy ("Scale your workflow")

#### Real-World References

- [Oat the Goat](https://www.oatthegoat.co.nz/)
- [Patagonia](https://www.patagonia.com/)
- [Mailchimp (2018–2021 era)](https://mailchimp.com/)
- [Graza olive oil](https://www.graza.co/)
- [Omsom](https://www.omsom.com/)

---

### 06 — Technical / Monochrome

> *"If you can measure it, you can make it better. If you can't measure it, don't decorate it."*

#### Overview

Technical design for developers, engineers, and makers. The palette is strictly monochrome — no color unless it carries meaning (green = success, red = error). Typography is tight, information-dense, and respects the user's intelligence. Every decorative element is a cost. This archetype borrows visual language from code editors and CLIs.

Modern digital applications: Vercel, Linear, Raycast, GitHub (dark mode), Zed editor.

#### Visual Signature

- **True monochrome:** `#09090B` through `#FAFAFA` with zinc scale mid-tones
- **Dense information:** higher content-to-whitespace ratio than editorial or luxury
- **Code aesthetics:** occasional monospace type for labels, code blocks, version numbers
- **Subtle borders:** `1px solid rgba(255,255,255,0.08)` (dark) or `rgba(0,0,0,0.08)` (light)
- **No icons from icon packs:** use simple geometric symbols or nothing
- **Micro-typography:** careful attention to tabular numbers, tracking on monospace

#### CSS Tokens

```css
:root {
  /* Dark theme (primary for this archetype) */
  --color-bg:         #09090B;   /* zinc-950 */
  --color-surface-1:  #18181B;   /* zinc-900 */
  --color-surface-2:  #27272A;   /* zinc-800 */
  --color-surface-3:  #3F3F46;   /* zinc-700 */
  --color-border:     #27272A;
  --color-border-subtle: rgba(255,255,255,0.06);
  --color-text:       #FAFAFA;   /* zinc-50 */
  --color-text-muted: #A1A1AA;   /* zinc-400 */
  --color-text-dim:   #71717A;   /* zinc-500 */
  /* Semantic only — not decorative */
  --color-success:    #22C55E;   /* green-500 */
  --color-error:      #EF4444;   /* red-500 */
  --color-warning:    #F59E0B;   /* amber-500 */
  --color-info:       #3B82F6;   /* blue-500 */

  /* Typography */
  --font-display:  'Geist', 'Inter', system-ui, sans-serif;
  --font-body:     'Geist', 'Inter', system-ui, sans-serif;
  --font-mono:     'Geist Mono', 'JetBrains Mono', 'SF Mono', monospace;
  --font-weight-display: 600;
  --font-weight-body:    400;
  --font-size-hero:  clamp(2rem, 5vw, 4rem);
  --font-size-h2:    clamp(1.25rem, 2.5vw, 2rem);
  --font-size-body:  0.9375rem;   /* 15px — slightly tighter */
  --font-size-code:  0.875rem;
  --font-size-label: 0.75rem;
  --line-height-display: 1.1;
  --line-height-body:    1.6;
  --letter-spacing-label: 0.04em;

  /* Spacing */
  --section-gap:    clamp(48px, 8vw, 96px);
  --element-gap:    16px;
  --column-gutter:  20px;

  /* Shape */
  --radius:    4px;
  --radius-sm: 3px;
  --radius-lg: 6px;

  /* Effects */
  --shadow-subtle: 0 0 0 1px var(--color-border-subtle);
  --glow-none: none;   /* No glow effects */
}
```

#### Layout Patterns

```
[HERO — product-forward, no lifestyle photography]
┌─────────────────────────────────────────────────────────┐
│  v2.4.1 — What's new →                                 │
│                                                         │
│  Build faster.                                          │
│  Deploy anywhere.                                       │
│                                                         │
│  One line description that is specific and honest.      │
│                                                         │
│  [Get Started]  [Documentation]                         │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │  > run command --flag value                      │  │
│  │  ✓ Process completed in 0.42s                    │  │
│  │  ✓ 3 outputs generated                          │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

#### Forbidden Patterns

- ❌ Colorful gradients (only monochrome gradients: black to zinc-900, etc.)
- ❌ Emojis in product copy (use semantic icons only if necessary)
- ❌ Stock photography (especially lifestyle, people, office scenes)
- ❌ Illustrated mascots or characters
- ❌ Decorative elements (shapes, blobs, sparkles)
- ❌ Testimonials with profile photos
- ❌ Flashy entrance animations
- ❌ Color used purely decoratively (color = meaning only)

#### Real-World References

- [Vercel](https://vercel.com/)
- [Linear](https://linear.app/)
- [Raycast](https://www.raycast.com/)
- [Zed Editor](https://zed.dev/)
- [GitHub](https://github.com/)

---

### 07 — Playful / Expressive

> *"Design should never say 'look how clever I am.' It should always say 'look how clever you are.'"*

#### Overview

Playful design is not immature — it is high-energy, bold, and genuinely joyful. It breaks the monotony of uniform card grids with varied layouts, unexpected color combinations, and kinetic typography. This archetype is NOT blue/purple SaaS. It chooses colors deliberately, uses scale dramatically, and treats layout as creative expression.

Modern digital applications: Duolingo, Figma (community/marketing), Framer marketing site, Pitch, Superhuman onboarding, Lego.

#### Visual Signature

- **Bold color combinations:** NOT blue+purple. Think orange+mint, yellow+navy, hot pink+forest
- **Layout variation:** sections don't all look the same; width, alignment, and depth vary
- **Scale contrast:** one element is enormous, another is tiny — for tension
- **Kinetic type:** headings that rotate, marquee banners, subtle character animations
- **Shape vocabulary:** mix of circle, pill, and rectangle — intentionally varied
- **Micro-interactions:** hover states that delight, not just darken

#### CSS Tokens

```css
:root {
  /* Colors — these are EXAMPLES; pick 2-3 saturated hues + neutrals */
  --color-bg:        #FAFAFA;
  --color-surface:   #FFFFFF;
  --color-text:      #111111;
  --color-muted:     #666666;

  /* Primary palette — one bold combination, not random rainbow */
  --color-primary:   #FF5733;    /* vivid orange */
  --color-secondary: #1B4332;    /* deep forest */
  --color-tertiary:  #FFD166;    /* golden yellow */
  --color-pop:       #EF233C;    /* accent pop */

  /* Typography */
  --font-display:  'Syne', 'Clash Display', 'Cabinet Grotesk', sans-serif;
  --font-body:     'DM Sans', 'Plus Jakarta Sans', 'Inter', sans-serif;
  --font-weight-display: 800;
  --font-weight-body:    400;
  --font-size-hero:  clamp(3rem, 9vw, 8rem);    /* LARGE */
  --font-size-h2:    clamp(2rem, 5vw, 4.5rem);
  --font-size-body:  1.0625rem;
  --line-height-display: 0.9;   /* tight for impact */
  --line-height-body:    1.65;
  --letter-spacing-display: -0.03em;

  /* Spacing */
  --section-gap:    clamp(80px, 12vw, 160px);
  --element-gap:    24px;
  --column-gutter:  24px;

  /* Shape — intentionally varied */
  --radius-none:   0px;
  --radius-sm:     8px;
  --radius-md:     16px;
  --radius-lg:     24px;
  --radius-pill:   999px;

  /* Effects */
  --shadow-lifted: 0 8px 32px rgba(0,0,0,0.12);
  --transition-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

#### Layout Patterns

```
[HERO — kinetic, off-grid energy]
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  ████ ENORMOUS TEXT THAT ████████████████████████████   │
│  BLEEDS AND WRAPS ACROSS THE FULL VIEWPORT WIDTH        │
│                                                         │
│                              ┌──────────────────────┐  │
│   Short subhead here         │  Product UI or image  │  │
│   in body type.              │  in a bold shape     │  │
│                              └──────────────────────┘  │
│   [Get Started]  →                                      │
│   ╰── pill button with color fill                       │
└─────────────────────────────────────────────────────────┘

[FEATURE — alternating, varied sizes]
  ════════════════════════════════════════════════
  ● FEATURE 01                  [LARGE IMAGE]
  BOLD HEADLINE
  Description text...
  ════════════════════════════════════════════════
               [LARGE IMAGE]   ● FEATURE 02
                               BOLD HEADLINE
                               Description...
```

#### Forbidden Patterns

- ❌ Monochrome or near-monochrome palette
- ❌ Uniform 3-column card grid with identical card sizes
- ❌ Corporate stock photography (people in office, hands shaking)
- ❌ Conservative font weights (thin, light) for display
- ❌ Muted or desaturated accent colors
- ❌ Every section having the same layout rhythm
- ❌ Blue/purple gradient as primary brand palette
- ❌ "Professional seriousness" tone in copy or design

#### Real-World References

- [Duolingo](https://www.duolingo.com/)
- [Framer](https://www.framer.com/) (marketing pages)
- [Pitch](https://www.pitch.com/)
- [Superhuman](https://superhuman.com/)
- [Monzo](https://www.monzo.com/)

---

### 08 — Data / Dashboard

> *"The purpose of visualization is insight, not pictures."* — Ben Shneiderman

#### Overview

Dashboard design optimizes for information density, at-a-glance status recognition, and efficient navigation. It is not decorative — it is functional. Color is semantic (green=good, amber=warning, red=error), not brand. Whitespace is used to separate data regions, not for aesthetic breathing room. The user is an expert who returns daily.

Modern digital applications: Grafana, Amplitude, Mixpanel, Datadog, Retool, Metabase.

#### Visual Signature

- **Dark background as default:** dark surfaces reduce eye fatigue during long sessions
- **Semantic color only:** every color use has explicit meaning
- **Information density:** more data per pixel than any other archetype
- **Tabular numbers:** font-variant-numeric: tabular-nums for all numerical data
- **Chart-first layout:** visualization components occupy primary visual weight
- **Status indicators:** green/amber/red dot indicators, not icon illustrations

#### CSS Tokens

```css
:root {
  /* Background layers */
  --color-bg:          #0F1117;   /* deepest background */
  --color-surface-1:   #1A1D27;   /* primary surface */
  --color-surface-2:   #242736;   /* elevated surface */
  --color-surface-3:   #2E3347;   /* modal / popover */
  --color-border:      rgba(255, 255, 255, 0.08);
  --color-border-focus: rgba(255, 255, 255, 0.24);

  /* Text */
  --color-text:        #F0F2F5;
  --color-text-muted:  #8B91A7;
  --color-text-dim:    #5A6070;

  /* Semantic (data meaning — DO NOT USE DECORATIVELY) */
  --color-success:     #22C55E;
  --color-success-bg:  rgba(34, 197, 94, 0.12);
  --color-warning:     #F59E0B;
  --color-warning-bg:  rgba(245, 158, 11, 0.12);
  --color-error:       #EF4444;
  --color-error-bg:    rgba(239, 68, 68, 0.12);
  --color-info:        #3B82F6;
  --color-info-bg:     rgba(59, 130, 246, 0.12);
  --color-neutral:     #8B91A7;

  /* Chart palette — distinct enough for colorblind users */
  --chart-1: #3B82F6;  /* blue */
  --chart-2: #10B981;  /* emerald */
  --chart-3: #F59E0B;  /* amber */
  --chart-4: #8B5CF6;  /* violet */
  --chart-5: #EC4899;  /* pink */
  --chart-6: #06B6D4;  /* cyan */

  /* Typography */
  --font-display:  'Inter', system-ui, sans-serif;
  --font-body:     'Inter', system-ui, sans-serif;
  --font-mono:     'JetBrains Mono', 'SF Mono', monospace;
  --font-weight-display: 600;
  --font-weight-body:    400;
  --font-size-hero:  1.5rem;      /* No giant hero text in dashboards */
  --font-size-h2:    1.125rem;
  --font-size-body:  0.875rem;    /* 14px — denser */
  --font-size-code:  0.8125rem;
  --font-size-label: 0.75rem;
  --line-height-body:    1.5;
  --tabular-nums:   font-variant-numeric: tabular-nums;

  /* Spacing — tighter than other archetypes */
  --section-gap:    24px;
  --element-gap:    12px;
  --card-padding:   16px;
  --column-gutter:  12px;

  /* Shape */
  --radius:    6px;
  --radius-sm: 4px;
  --radius-lg: 8px;

  /* Effects */
  --shadow-card: 0 1px 3px rgba(0,0,0,0.3), 0 0 0 1px var(--color-border);
}
```

#### Layout Patterns

```
[SIDEBAR + MAIN — persistent navigation]
┌────────┬────────────────────────────────────────────┐
│        │  ┌─────────┐ ┌─────────┐ ┌─────────┐      │
│  NAV   │  │ KPI     │ │ KPI     │ │ KPI     │      │
│        │  │ 99.9%   │ │ 1.2ms   │ │ 2.4K    │      │
│  Home  │  │ uptime  │ │ p99     │ │ req/s   │      │
│  Dash  │  └─────────┘ └─────────┘ └─────────┘      │
│  Logs  │                                             │
│  Alerts│  ┌──────────────────────┬──────────────┐   │
│  Config│  │ Time series chart    │ Table data   │   │
│        │  │ ─────────────────    │ ID  Val  Δ%  │   │
│        │  │                      │ 01  42   +2  │   │
│        │  └──────────────────────┴──────────────┘   │
└────────┴────────────────────────────────────────────┘
```

#### Forbidden Patterns

- ❌ Decorative elements (illustrations, blob shapes, sparkles)
- ❌ Marketing copy or testimonials
- ❌ Emojis in data labels or headers
- ❌ Color used for decoration (not semantic meaning)
- ❌ Large hero sections with taglines
- ❌ Card shadows that don't indicate elevation
- ❌ Testimonial sections
- ❌ Animated entrance effects on charts (delayed data display)
- ❌ Stock photography

#### Real-World References

- [Grafana](https://grafana.com/)
- [Datadog](https://www.datadoghq.com/)
- [Amplitude](https://amplitude.com/)
- [Retool](https://retool.com/)
- [Metabase](https://www.metabase.com/)

---

### 09 — Retro / Nostalgic

> *"The future will always remember the past."*

#### Overview

Retro design is not random nostalgia — it is a precise, disciplined reference to a specific era's aesthetic vocabulary. The most effective retro design commits deeply to its reference (pixel art, 80s gradient machines, 90s web, 70s printing) and executes it with modern browser capabilities. The discipline is in what you DON'T add — modern flourishes break the spell instantly.

Modern digital applications: Poolside FM, Binge (some screens), certain indie games, specific music releases, food/beverage brands.

#### Visual Signature

- **Era commitment:** choose ONE era, execute it faithfully
- **Limited palette:** 2-3 colors maximum (like print constraints of the era)
- **Pixel influence:** if 8-bit, use pixel-perfect borders and shapes
- **Specific typography:** VT323, Press Start 2P for retro digital; or vintage serif for older eras
- **Pattern fills:** halftone, dither patterns, scan lines — textural not photographic
- **Intentional limitation:** the constraint IS the design

#### CSS Tokens (Pixel/90s variant — adjust for chosen era)

```css
:root {
  /* Colors — strictly limited (choose ONE era palette, max 3 hues) */
  /* Example: 90s arcade */
  --color-bg:       #000000;
  --color-surface:  #1A0A2E;   /* deep purple */
  --color-text:     #00FF41;   /* phosphor green */
  --color-accent-1: #FF00FF;   /* magenta */
  --color-accent-2: #00FFFF;   /* cyan */
  /* NOTE: Do NOT add more colors. The palette is the constraint. */

  /* Alternative: 70s print era */
  /* --color-bg:     #F4E4C1; (aged paper) */
  /* --color-text:   #3D2B1F; (brown-black) */
  /* --color-accent: #C8430B; (burnt orange) */

  /* Typography — era-specific */
  --font-display:  'VT323', 'Press Start 2P', 'Courier New', monospace;
  --font-body:     'VT323', monospace;   /* only monospace for pixel era */
  /* Alternative for 70s: --font-display: 'Bebas Neue', sans-serif; */
  --font-size-hero:  clamp(3rem, 8vw, 7rem);
  --font-size-body:  1.125rem;   /* larger for VT323 readability */
  --line-height-body: 1.6;

  /* Spacing */
  --section-gap:   48px;
  --element-gap:   16px;
  --grid-unit:     8px;    /* pixel-grid alignment */

  /* Shape — era-specific */
  --radius:    0px;          /* pixel era: sharp */
  --radius-pill: 999px;     /* or pill only — no in-between */

  /* Era-specific effects */
  --scanlines: repeating-linear-gradient(
    transparent, transparent 2px,
    rgba(0,0,0,0.3) 2px, rgba(0,0,0,0.3) 4px
  );
  --crt-glow: 0 0 10px currentColor;
}
```

#### Forbidden Patterns

- ❌ Modern glassmorphism (completely breaks the era illusion)
- ❌ Generic gradients (not era-specific gradients)
- ❌ Modern sans-serif body text at small sizes
- ❌ Contemporary icon styles (Lucide, HeroIcons)
- ❌ Mixing eras (pixel art + skeuomorphism + flat design)
- ❌ Adding "modern" flourishes to make it more polished
- ❌ Smooth cubic-bezier transitions (use step functions or none)
- ❌ Stock photography (era photography or none)

#### Real-World References

- [Poolside FM](https://poolside.fm/)
- [Winamp (classic)](https://webamp.org/)
- [CSS Tricks early archives](https://css-tricks.com/)
- [Space Jam 1996 site](https://www.spacejam.com/1996/)
- Various retro indie game websites

---

### 10 — Material / Tactile

> *"Good design makes a product useful."* — Dieter Rams

#### Overview

Material design draws metaphors from physical surfaces — paper layers, elevation, the way light falls on objects. It creates depth through subtle shadows (not glow), layers surfaces realistically, and uses color to convey meaning. This is the most "neutral" archetype but is still a distinct design system — it is specifically NOT the dark gradient template, and NOT flat no-depth minimalism. It occupies the middle ground.

This is the appropriate DEFAULT for product/SaaS with no strong brand direction.

Modern digital applications: Apple (current), Material Design 3, Stripe, Notion, Linear (light mode).

#### Visual Signature

- **Surface elevation:** `box-shadow` values that simulate light from above
- **Color accent that works:** one functional color that appears on interactive elements
- **Consistent radius:** one radius value applied uniformly (not mixed)
- **Whitespace as surface:** the background is a surface, not void
- **Subtle texture:** optional 1-2% noise for depth without kitsch
- **Interactive feedback:** shadows grow on hover (card lifts, not glows)

#### CSS Tokens

```css
:root {
  /* Surface layers — light sources from above */
  --color-bg:          #F8F8F8;   /* level 0 — page background */
  --color-surface-1:   #FFFFFF;   /* level 1 — card */
  --color-surface-2:   #FEFEFE;   /* level 2 — elevated card */
  --color-surface-3:   #FCFCFC;   /* level 3 — modal */
  --color-text:        #111827;   /* gray-900 */
  --color-text-muted:  #6B7280;   /* gray-500 */
  --color-text-dim:    #9CA3AF;   /* gray-400 */
  --color-border:      #E5E7EB;   /* gray-200 */
  --color-border-focus: #D1D5DB;  /* gray-300 */
  --color-accent:      #2563EB;   /* blue-600 — functional, not decorative */
  --color-accent-hover: #1D4ED8;  /* blue-700 */
  --color-accent-muted: #DBEAFE;  /* blue-100 */

  /* Typography */
  --font-display:  'Inter', system-ui, -apple-system, sans-serif;
  --font-body:     'Inter', system-ui, -apple-system, sans-serif;
  --font-weight-display: 700;
  --font-weight-semibold: 600;
  --font-weight-body:    400;
  --font-size-hero:  clamp(2.25rem, 5vw, 3.75rem);
  --font-size-h2:    clamp(1.5rem, 3vw, 2.25rem);
  --font-size-body:  1rem;
  --font-size-small: 0.875rem;
  --line-height-display: 1.15;
  --line-height-body:    1.7;
  --letter-spacing-display: -0.025em;

  /* Spacing */
  --section-gap:    clamp(64px, 10vw, 120px);
  --element-gap:    24px;
  --card-padding:   24px;
  --column-gutter:  24px;

  /* Shape — CONSISTENT single radius */
  --radius:    10px;
  --radius-sm: 6px;
  --radius-lg: 14px;
  --radius-xl: 20px;

  /* Effects — elevation system */
  --shadow-1: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-2: 0 1px 3px rgba(0,0,0,0.07), 0 1px 2px rgba(0,0,0,0.05);
  --shadow-3: 0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.05);
  --shadow-4: 0 10px 15px rgba(0,0,0,0.07), 0 4px 6px rgba(0,0,0,0.05);
  --shadow-5: 0 20px 25px rgba(0,0,0,0.07), 0 10px 10px rgba(0,0,0,0.04);
  /* Note: shadows simulate light, never glow */

  --transition-default: all 0.15s ease;
  --transition-lift: box-shadow 0.2s ease, transform 0.2s ease;
}
```

#### Layout Patterns

```
[HERO — product-forward, clear value proposition]
┌─────────────────────────────────────────────────────────┐
│                                                         │
│         Clear, specific headline about the              │
│         exact value the product delivers.               │
│                                                         │
│    One supporting sentence. No jargon. No buzzwords.    │
│                                                         │
│    [Primary CTA]    [Secondary — text link]             │
│                                                         │
│    ┌────────────────────────────────────────────────┐  │
│    │  ████████████████████████████████████████████  │  │
│    │  ██  Product screenshot or live demo UI  ████  │  │
│    │  ████████████████████████████████████████████  │  │
│    └────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘

[FEATURES — surface elevation communicates grouping]
 ┌──────────────────────┐  ┌──────────────────────┐
 │ shadow-2 (card)      │  │ shadow-2 (card)      │
 │                      │  │                      │
 │ Icon (functional)    │  │ Icon (functional)    │
 │ Feature Title        │  │ Feature Title        │
 │ Specific description │  │ Specific description │
 │ that isn't vague.    │  │ that isn't vague.    │
 └──────────────────────┘  └──────────────────────┘
```

#### Forbidden Patterns

- ❌ Neon glow effects (`box-shadow: 0 0 30px #7C3AED`)
- ❌ Cyberpunk or dark gradient aesthetic
- ❌ Flat with zero depth (no shadows at all)
- ❌ Particle backgrounds or WebGL canvas effects
- ❌ Mixed border-radius values (use the system consistently)
- ❌ Gradients on the primary CTA button (solid color only)
- ❌ Background sections that alternate between gradient colors

#### Real-World References

- [Stripe](https://www.stripe.com/) (dashboard)
- [Notion](https://www.notion.so/)
- [Apple](https://www.apple.com/) (current)
- [Linear](https://linear.app/) (light mode)
- [Craft](https://www.craft.do/)

---

## Forbidden Combinations

The following combinations produce the "default AI template" and must never appear together:

| Element A | Element B | Why It's Generic |
|-----------|-----------|-----------------|
| Dark hero (`#0A0A0A` bg) | Blue-to-purple gradient text | Every SaaS from 2021–2024 |
| Three equal-width feature cards | Each with an icon + shadow + 8px radius | Default Bootstrap pattern |
| "Join 50,000+" social proof | Placed directly below hero | Growth hacking template |
| Glassmorphism card | Particle.js background | "Premium AI tool" cliché |
| Inter Bold headline | Inter Regular body | 100% generic, no personality |
| Purple CTA button | White text on hero | Framework default |
| "Trusted by leading companies" | Five grey logo SVGs | The trust strip |
| Floating macbook mockup | Diagonal gradient background | SaaS product show |
| Star rating testimonials | Circular avatar photos | Every Webflow template |
| Countdown timer | Gradient border | Urgency + tech aesthetic |

**If your design has 3 or more of these combinations, restart with an archetype.**

---

## Generic AI Output Tells

Watch for these signals that a design is statistically averaged, not intentionally designed:

1. **The Gradient Drift:** Hero background transitions from `#1a1a2e` to `#16213e` to `#0f3460`. No decision was made.
2. **The Icon Triplet:** Three sections, each with a 24px icon (usually blue), a bold heading, and 2 sentences. Exact same height.
3. **The Glow Button:** `box-shadow: 0 0 30px rgba(124, 58, 237, 0.4)` on the primary CTA.
4. **The Trust Strip:** "As seen in" + blurred, grayscale logo row.
5. **The Floating Device:** A laptop or phone mockup, floating at an angle, on a gradient.
6. **The Testimonial Carousel:** Three testimonial cards with star ratings and circular avatars.
7. **The Stats Row:** Four KPIs in a horizontal row: "99.9% uptime · 50K users · 24/7 support · 5-star rated"
8. **The Section Stripe:** Content sections alternating white and light gray backgrounds.
9. **The FAQ Accordion:** At the bottom of every page, regardless of whether FAQs are useful.
10. **The Footer Grid:** Logo + tagline | Product links | Company links | Legal links — identical to every site.

---

## DESIGN.md Integration

When converting an archetype selection into a `DESIGN.md` file, use the following structure for each archetype. This enables consistent token generation across the system.

### Template Structure

```markdown
# DESIGN.md

## Archetype
**Selected:** [Archetype Name and Number]
**Rationale:** [Why this archetype fits the project]

## Design Tokens

### Color
\`\`\`
background:    [value from archetype]
surface:       [value from archetype]
text-primary:  [value from archetype]
text-muted:    [value from archetype]
accent:        [value from archetype]
border:        [value from archetype]
\`\`\`

### Typography
\`\`\`
font-display:  [family from archetype]
font-body:     [family from archetype]
size-hero:     [value]
size-h2:       [value]
size-body:     [value]
weight-display:[value]
weight-body:   [value]
\`\`\`

### Spacing & Shape
\`\`\`
section-gap:   [value]
element-gap:   [value]
radius:        [value from archetype]
\`\`\`

### Effects
\`\`\`
shadow-card:   [value — or "none" for archetypes 01, 04]
gradient:      FORBIDDEN / [specific value if archetype allows]
\`\`\`

## Forbidden (from archetype)
- [Item 1 from archetype's forbidden list]
- [Item 2]
- ...
```

### Archetype → DESIGN.md Quick Map

| Archetype | bg | accent | radius | shadow | gradient |
|-----------|-----|--------|--------|--------|----------|
| 01 Swiss | `#FFFFFF` | `#FF0000` | `0px` | none | FORBIDDEN |
| 02 Editorial | `#FFFDF7` | `#B5271F` | `0-4px` | none | FORBIDDEN |
| 03 Luxury | `#FAF8F4` | `#B8945F` | `0-2px` | none | FORBIDDEN |
| 04 Brutalist | `#FFFFFF` | `#FF4500` | `0px` | none | FORBIDDEN |
| 05 Organic | `#F5EFE0` | `#C4614A` | `12-24px` | soft | FORBIDDEN |
| 06 Technical | `#09090B` | semantic only | `4-6px` | subtle | monochrome only |
| 07 Playful | `#FAFAFA` | bold multi-hue | `0-999px` | lifted | selective |
| 08 Dashboard | `#0F1117` | semantic only | `4-8px` | card | FORBIDDEN (decorative) |
| 09 Retro | era-specific | era-specific | `0px` or pill | era-specific | era-specific |
| 10 Material | `#F8F8F8` | `#2563EB` | `10px` | elevation | FORBIDDEN on CTA |

---

## Quick Reference Table

| # | Name | Primary Bg | Accent | Font Style | Radius | Shadows | Gradients |
|---|------|-----------|--------|------------|--------|---------|-----------|
| 01 | Swiss / Intl | White | Pure primary | Grotesque 900 | 0px | None | Forbidden |
| 02 | Editorial | Cream | Deep editorial | Serif display | 0-4px | None | Forbidden |
| 03 | Luxury | Warm parchment | Warm gold | Thin serif | 0-2px | None | Forbidden |
| 04 | Brutalist | White | Electric | Monospace | 0px | None | Forbidden |
| 05 | Organic | Warm sand | Terracotta | Expressive serif | 12-24px | Soft | Forbidden |
| 06 | Technical | Near-black | Semantic | Geometric sans | 4-6px | Subtle | Mono only |
| 07 | Playful | Light | Bold multi-hue | Display sans | Mixed | Lifted | Selective |
| 08 | Dashboard | Deep dark | Semantic | Compact sans | 4-8px | Card | Forbidden |
| 09 | Retro | Era-specific | Era-specific | Era-specific | 0 or pill | Era | Era-specific |
| 10 | Material | Off-white | Functional blue | System sans | 10px | Elevation | Forbidden CTA |

---

*This document is a living reference. When a new design archetype becomes culturally relevant (e.g., a new major aesthetic movement), it should be added as Archetype 11+. The 10 current archetypes cover the major distinct visual territories as of 2026.*

*Maintained as part of the web-design-enhancer-pro skill.*
