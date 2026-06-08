---
name: web-design-enhancer
description: Validator and enforcer of the DESIGN.md contract. Pillar 3 of the design ecosystem alongside getdesign.md (real visual references) and UI/UX Pro Max (sectoral design intelligence). Eliminates AI visual improvisation through 4 automated validation scripts, GSAP, and a Playwright audit on 4 breakpoints.
---

# Web Design Enhancer

This skill is the **validator and enforcer** of the design ecosystem. It guarantees that implemented code respects the `DESIGN.md` contract established upstream by the two other pillars.

---

## The Ecosystem — 3 Pillars

```
┌─────────────────────────────────────────────────────────────────────┐
│  PILLAR 1 — getdesign.md           PILLAR 2 — UI/UX Pro Max         │
│                                                                     │
│  Real visual references            Per-industry design intelligence │
│  "What should my project          "Which decisions for my product   │
│   look like?"                       type?"                          │
│  (72 sites: Stripe, Vercel,        (161 rules, 67 styles,           │
│  Linear, Nike, Tesla...)            161 palettes, 57 typos)         │
│                    ↘                      ↙                         │
│                                                                     │
│              DESIGN.md  ←  the project's design contract            │
│                                                                     │
│                              ↓                                      │
│                                                                     │
│  PILLAR 3 — this skill  +  shadcn/ui  +  GSAP                       │
│  Implementation  →  Automated validation  →  Delivery               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Complete Workflow

### ⚡ Phase 0 — Design Anchoring (mandatory, before any code)

**Never create a DESIGN.md from scratch. Feed its creation from the two sources.**

#### 0a. Visual reference — getdesign.md

Pick the site whose aesthetic is closest to the project. Download its DESIGN.md:

```bash
npx getdesign@latest add <brand>
```

Examples by project type:

| Project type | Recommended reference | Command |
|---|---|---|
| Fintech, payments | Stripe | `npx getdesign@latest add stripe` |
| Dev tool, infra | Vercel | `npx getdesign@latest add vercel` |
| Minimalist SaaS | Linear | `npx getdesign@latest add linear` |
| Workspace, docs | Notion | `npx getdesign@latest add notion` |
| Open-source, API | Supabase | `npx getdesign@latest add supabase` |
| Luxury e-commerce | Ferrari | `npx getdesign@latest add ferrari` |
| Crypto, trading | Binance | `npx getdesign@latest add binance` |
| AI, chatbot | Cursor | `npx getdesign@latest add cursor` |

The reference `DESIGN.md` is dropped at the project root. **It is inspiration, not copy-paste.** Extract the relevant tokens (colors, type, radii, shadows) that match the project.

#### 0b. Design intelligence — UI/UX Pro Max

Generate the design system adapted to the product type:

```bash
python3 scripts/search.py \
  "product description" --design-system -p "Project Name"
```

Examples:

```bash
# Banking app
python3 scripts/search.py \
  "fintech banking app" --design-system -p "MyBank"

# Wellness platform
python3 scripts/search.py \
  "beauty spa wellness booking" --design-system -p "Serenity"

# SaaS analytics dashboard
python3 scripts/search.py \
  "saas analytics dashboard" --design-system -p "DataFlow"
```

The output contains: recommended page pattern, priority style, palette, typography, key effects, and sectoral antipatterns to avoid at all costs.

#### 0c. Merge → project DESIGN.md

Create the project's `DESIGN.md` by combining both sources:

- **UI/UX Pro Max → structural decisions**: semantic palette, typography, page pattern, sectoral antipatterns
- **getdesign.md → stylistic refinement**: precise tokens, radii, shadows, density, visual micro-details

**Conflict rule**: UI/UX Pro Max wins (sectoral fit), getdesign.md refines visual texture.

Use `templates/design-md-template.md` as the skeleton.

#### 0d. Self-validation against AI clichés (mandatory before submitting DESIGN.md)

Before submitting the DESIGN.md, ask this question for **every theme decision**:

> *"Have I seen this concept on the last 1000 AI-generated portfolios/landing pages?"*

If the answer is yes → replace it with something specific to the real project.

**Themes and concepts strictly forbidden in DESIGN.md:**

| Forbidden concept | Why | Alternative |
|---|---|---|
| `dark cyberpunk` / `cybernetic` | AI cliché #1 for tech portfolios | Describe the real texture: "matte carbon surfaces with monospace type" |
| `glow cursor` | Overused effect, never requested | Remove — no equivalent needed |
| `grid background` | Present in 90% of AI dev portfolios | Solid background or very subtle radial gradient only if justified |
| `glassmorphism` | Exhausted trend, strong AI signal | `backdrop-filter` only on functional elements (modals, dropdowns) |
| `neon glow` / `neon accents` | Immediate AI cyberpunk signal | High-contrast colors without luminous `box-shadow` |
| `particle background` / `particles.js` | Overdone since 2018 | Static background or subtle CSS pattern |
| `typewriter effect` / `typed.js` | Dev portfolio cliché #1 | Static title — content speaks, not animation |
| `SYS_STATUS: ONLINE` / system badges | Unrequested AI injection | Remove — or justify functionally in the brief |
| Decorative `hero badge` ("SecOps & Admin") | Info is already in H1/H2 | Remove — badge info must live in copy |
| Lucide icons on **every** element | Generic, interchangeable icons | Custom SVG or icons limited to functional elements |
| `monitoring style (Grafana/Datadog)` as theme | Generic AI choice for sysadmin profiles | Identify what's unique to the project, not the sector |

**Golden rule:** if an element is not in the original brief, it does not belong in DESIGN.md.

Validate DESIGN.md before any code:

```bash
python3 scripts/check.py --gate 0   # Verify Phase 0 was executed
python3 scripts/check.py --gate 1   # Validate DESIGN.md
```

**If either command returns an error → do not move to Phase 1. Fix and rerun.**

`validate_design.py` automatically detects forbidden themes and blocks progress.

---

### Phase 1 — Design Contract (the "Brain")

The final `DESIGN.md` must be complete before any code. Minimum requirements:

- **§2 Palette**: 4–8 colors with semantic roles (`Primary`, `Background`, `Text`, `Accent`, `Success`, `Danger`) — WCAG AA contrast auto-verified
- **§3 Typography**: max 2 fonts (display + body), Google Fonts only
- **§4 Type hierarchy**: sizes in ranges auto-checked by `validate_design.py` — **H1 28–80px**, H2 22–60px, H3 18–36px, **P 13–18px**, Small 11–14px
- **§5 Spacing**: all multiples of 8px
- **§6 Components**: max 3 variants per type
- **§7 Animations**: ≤ 400ms, mandatory `prefers-reduced-motion` mention
- **§8 Dark Mode**: mandatory if main background is dark — surface, secondary-text, dark-border documented
- **§9 Mobile** *(optional — mandatory if a native app is in scope)*: touch targets ≥ 44pt iOS / 48dp Android, safe areas, native units
- **§10 Three.js** *(optional — mandatory if a WebGL scene is in scope)*: pixel ratio cap, dispose strategy, WebGL fallback — see `references/threejs-best-practices.md`

Validate before continuing:

```bash
python3 scripts/check.py --gate 1
```

**`check.py --gate 1` is the canonical command.** It invokes `validate_design.py` (WCAG AA, §4 ranges, §8/§9/§10) and persists the DESIGN.md SHA-256 hash to `.phase-log.json` — the gate auto-invalidates if DESIGN.md is modified.

**If the command returns an error → fix DESIGN.md. Do not write a single line of code until this gate is green.**

---

### Phase 2 — Structural Implementation (the "Body")

- **Primitives**: exclusively **shadcn/ui** components (Button, Card, Dialog, Input, Table...). Recreating these blocks from raw `div`s is forbidden.
- **Variables**: configure `globals.css` only via CSS variables defined in DESIGN.md (`--primary`, `--background`, `--radius`...).
- **Grid**: Tailwind classes in multiples of 8 only (`p-2`, `p-4`, `p-8`, `gap-4`, `gap-8`). Arbitrary values (`p-[11px]`, `mt-[13px]`) are strictly forbidden.

---

### Phase 3 — Dynamism with GSAP (the "Soul")

See `references/gsap-best-practices.md`.

- **shadcn/ui + Tailwind** handle native states (hover, focus, disabled).
- **GSAP** only for orchestration: staggered entries, scroll effects (ScrollTrigger).
- All durations respect the timings in DESIGN.md (≤ 400ms).

---

### Phase 4 — Visual Inspection (the "Eyes" via MCP Playwright) — CRITICAL

A task is never done until it has been visually inspected.

```bash
python3 scripts/visual_audit.py --url http://localhost:3000 --output ./audit-results
```

Inspects on **4 breakpoints** (375 / 768 / 1280 / 1920px). Fix immediately if:

- **AI artifacts**: emojis, stickers, decorative icons that weren't requested
- **Invented logos**: graphic placeholders (`logo-placeholder`, `your-logo`, `brandname`)
- **Wonky geometry**: spacings that aren't multiples of 8px

Validation loop: fix → rerun audit → repeat until zero defect.

---

### Phase 5 — Automated Validation (mandatory before delivery)

Run the final gate — it orchestrates `detect_ai_slop` → `audit_spacing` → `validate_design` → `diff_design_vs_code` in sequence:

```bash
python3 scripts/check.py --final --code ./src
```

If the gate fails → fix immediately by consulting `references/antipatterns-guide.md` → rerun. **Any output not validated by the full gate is rejected.**

---

## Visual Hygiene Rules (non-negotiable)

- **Less but better**: any visual element without a clear function (border, shadow, gradient) is removed.
- **Strict 8px grid**: `p-2` `p-4` `p-6` `p-8` `gap-4` `gap-8`. Never `p-[11px]`.
- **Text logo**: if no logo asset is provided → styled text only (`font-bold tracking-tight uppercase`). Never an improvised graphic placeholder.
- **WCAG AA contrast**: text/background minimum **4.5:1**. UI elements minimum **3.0:1**.

---

## Resources

| File | Role |
|---|---|
| `templates/design-md-template.md` | DESIGN.md skeleton to fill |
| `templates/design-system.css` | Ready-to-customize CSS variables |
| `references/design-md-spec-v2.md` | Full DESIGN.md format spec |
| `references/antipatterns-guide.md` | Concrete ❌ vs ✅ examples |
| `references/gsap-best-practices.md` | GSAP guide |
| `references/threejs-best-practices.md` | Three.js guide — critical WebGL antipatterns (§10) |
| `scripts/validate_design.py` | DESIGN.md validation + WCAG AA + §4 ranges + §10 Three.js |
| `scripts/detect_ai_slop.py` | Antipattern detection in code |
| `scripts/audit_spacing.py` | 8px grid audit |
| `scripts/visual_audit.py` | Playwright visual audit (4 breakpoints) |
| `scripts/diff_design_vs_code.py` | Diff DESIGN.md ↔ code (colors, fonts, animations) |
| `.slop-ignore` | Whitelist against false positives for detect_ai_slop.py |
