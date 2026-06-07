# Web Design Enhancer Pro

**Eradicate AI visual improvisation — deliver clean, precise, and professional interfaces.**

---

## Philosophy: Anti-"AI Slop"

This skill transforms any AI-generated interface into a professional-grade result. It enforces a mechanical rigor that makes producing "AI slop" patterns impossible — even with an unsupervised agent.

**3 core principles:**
- **Contract before code** — the `DESIGN.md` is mechanically validated before a single line of code is written.
- **Verifiable > subjective** — every design decision is testable via a Python script.
- **Real references > training data** — Phase 0 forces anchoring on existing designs (Stripe, Linear, Vercel...).

---

## Architecture: 3 Pillars

```
Pillar 1 — getdesign.md           Pillar 2 — UI/UX Pro Max
(real visual references)          (industry intelligence, 161 rules, 67 styles)
           ↓                                    ↓
                      DESIGN.md
                  (design contract)
                         ↓
           Pillar 3 — web-design-enhancer-pro
           (validation + implementation + audit)
```

---

## 5-Phase Workflow

### Phase 0 — Anchoring (mandatory, blocking)
```bash
# 1. Fetch real visual references
npx getdesign@latest add stripe

# 2. Query the UI/UX Pro Max database
python3 scripts/search.py "saas analytics dashboard" --design-system -p "MyProject"

# 3. Verify that Phase 0 is proven
python3 scripts/check.py --gate 0
```

### Phase 1 — DESIGN.md Contract
Fill out `DESIGN.md` with sections §0 to §8 (template: `templates/design-md-template.md`).
```bash
python3 scripts/validate_design.py DESIGN.md
python3 scripts/check.py --gate 1
```

### Phase 2 — CSS/HTML Implementation
Map the `DESIGN.md` tokens into `globals.css` or CSS variables.

### Phase 3 — GSAP Animations
Orchestrate entries and scroll effects according to `references/gsap-best-practices.md`.

### Phase 4 — Playwright Visual Audit
```bash
python3 scripts/visual_audit.py --url http://localhost:3000 --output ./audit-results
```

### Phase 5 — Final Validation (blocking gate)
```bash
python3 scripts/check.py --final --code ./src
# Sequence: detect_ai_slop → audit_spacing → validate_design → diff_design_vs_code
```

---

## Available Scripts

| Script | Usage | Role |
| :--- | :--- | :--- |
| `validate_design.py` | `DESIGN.md` | Validates sections §0–8, WCAG AA, dark mode |
| `detect_ai_slop.py` | `--design` + `--code` | Detects AI antipatterns (score 0–100, threshold 80) |
| `diff_design_vs_code.py` | `DESIGN.md --code ./src` | Detects contract ↔ implementation mismatches |
| `audit_spacing.py` | `--path ./src` | Enforces 8px grid on actual CSS/JSX |
| `visual_audit.py` | `--url localhost:3000` | Playwright screenshots & audit across 4 breakpoints |
| `check.py` | `--gate 0/1/final` | Sequential gate orchestrator |
| `search.py` | `"query" --domain` | BM25 search in the UI/UX Pro Max CSV data |
| `core.py` | - | BM25 search engine (dependency of search.py) |
| `design_system.py` | - | Design system generator (dependency of search.py) |

---

## Automatically Detected Antipatterns

| Antipattern | AI Signal | Remedy |
| :--- | :--- | :--- |
| Decorative Emojis | ✨🚀💡 inside the code | Immediate removal |
| Generic Lucide Icons | sparkles, zap, star, bot, magic | Cohesive icon pack or custom SVG |
| Cliché Gradients | blue→purple, pink→purple | Solid semantic colors |
| Unrequested Status Badges | ● LIVE NOW, SYS_STATUS: ONLINE | Remove or justify in §1 |
| Vague Buzzwords | premium, modern, elegant | Precise, measurable descriptions |
| Flat Typography | font-size: 16px everywhere | Respect H1–Small hierarchy in §4 |
| Excessive Hover Effects | translateY(-8px), 32px shadow | ≤ -4px, subtle/soft shadow |
| Improvisational Dark Mode | AI-invented dark colors | Mandatory section §8 |
| Forbidden Themes | glassmorphism, typewriter effect | Detected and blocked by validate_design |

---

## Project Structure

```
web-design-enhancer-pro/
├── SKILL.md                          # Main documentation (complete workflow)
├── README.md                         # This file
├── requirements.txt                  # Python dependencies
├── .slop-ignore                      # Whitelist for anti-slop false positives
├── data/                             # UI/UX Pro Max CSV files (styles, colors, fonts...)
│   └── stacks/                       # Stack-specific guidelines (16 frameworks)
├── scripts/
│   ├── validate_design.py            # DESIGN.md validator (§0–8, WCAG, dark mode)
│   ├── detect_ai_slop.py             # AI antipattern detector (score 0–100)
│   ├── diff_design_vs_code.py        # DESIGN.md ↔ real code diff
│   ├── audit_spacing.py              # 8px grid audit on CSS/JSX
│   ├── visual_audit.py               # Playwright audit (4 breakpoints)
│   ├── check.py                      # Gates orchestrator
│   ├── search.py                     # UI/UX Pro Max BM25 search engine
│   ├── core.py                       # Search core functions
│   └── design_system.py              # Design system generator
├── references/
│   ├── design-md-spec-v2.md          # DESIGN.md v3 specification (§0–8 detailed)
│   ├── api_reference.md              # Technical API reference
│   ├── antipatterns-guide.md         # Antipattern guide (❌ vs ✅)
│   └── gsap-best-practices.md        # GSAP guide (Phase 3)
├── templates/
│   ├── design-md-template.md         # DESIGN.md template (§0–8 + checklist)
│   ├── design-system.css             # Ready-to-customize CSS variables
│   └── brand-kit.json                # Exportable brand kit structure
└── examples/
    ├── manus-demo/DESIGN.md          # Validated example — dev tool, Neo-Brutalism
    └── dataflow-saas/DESIGN.md       # Validated example — SaaS analytics, Dense Dashboard
```

---

## Pre-delivery Checklist

- [ ] `DESIGN.md` §0–8 complete, `check.py --gate 0` passed.
- [ ] `validate_design.py`: 0 errors.
- [ ] `detect_ai_slop.py`: score ≥ 80/100.
- [ ] `diff_design_vs_code.py`: 0 mismatches.
- [ ] `audit_spacing.py`: 0 8px grid violations.
- [ ] `visual_audit.py`: screenshots validated across 4 breakpoints.
- [ ] Dark Mode section §8 present with bg < #333 and WCAG AA contrast.
- [ ] `prefers-reduced-motion` present in CSS/JS files.
- [ ] Zero decorative emojis, zero cliché gradients, zero generic icons.

---

*Designed to turn AI-generated code into exceptional design.*
