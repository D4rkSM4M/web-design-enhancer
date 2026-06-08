# Web Design Enhancer Pro

**Eliminate AI visual improvisation — deliver clean, precise, professional interfaces.**

A Claude Code skill (also runnable from Codex, OpenCode, Antigravity) that enforces a machine-verifiable `DESIGN.md` contract. Every rule is validated by a Python script before code is generated, so the agent cannot produce "AI slop" patterns — decorative emojis, cliche gradients, glassmorphism, improvised dark modes, broken 8px grids, WCAG violations, Three.js antipatterns, etc.

See [`docs/README.md`](./docs/README.md) for the full technical reference (philosophy, 5-phase workflow, scripts, antipatterns, CI/CD, delivery checklist).

---

## Install

Clone the repo, install Python dependencies:

```bash
git clone https://github.com/Steph-ux/web-design-enhancer.git
cd web-design-enhancer
pip install -r requirements.txt
```

**Prerequisites**: Python 3.10+. No LLM API key required — scripts are deterministic.

### Per AI tool

| Tool | Install location | How to invoke |
| :--- | :--- | :--- |
| **Claude Code** | `~/.claude/skills/web-design-enhancer-pro/` | Auto-discovered. Use `/web-design-enhancer` or let Claude detect it |
| **Codex** (OpenAI CLI) | Clone anywhere | `codex --context ./web-design-enhancer-pro "validate my DESIGN.md"` |
| **OpenCode** | Clone or add as submodule in the project | `/add SKILL.md` then run `python3 scripts/...` |
| **Antigravity** (Google) | Clone into the workspace | Load `SKILL.md` as agent context; run scripts in the built-in terminal |

### Optional CI/CD hooks

```bash
# Husky pre-commit gate
npx husky install
chmod +x .husky/pre-commit

# GitHub Actions: .github/workflows/design-gate.yml is already wired up
```

Both no-op when no `DESIGN.md` is at the repo root.

---

## Quick start

```bash
# 1. Anchor on real references (mandatory)
npx getdesign@latest add stripe
python3 scripts/search.py "saas analytics dashboard" --design-system -p "MyProject"

# 2. Fill DESIGN.md from the template
cp templates/design-md-template.md DESIGN.md

# 3. Validate the contract
python3 scripts/check.py --gate 1

# 4. After implementation, run the final gate
python3 scripts/check.py --final --code ./src
```

Full workflow, script reference, and antipattern catalog: [`docs/README.md`](./docs/README.md).

---

*Built to turn AI-generated code into exceptional design.*
