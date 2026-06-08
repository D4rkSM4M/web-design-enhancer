# Web Design Enhancer Pro

**Eliminate AI visual improvisation — deliver clean, precise, professional interfaces.**

Ever asked an AI to build a UI and gotten back a wall of glossy gradients, random emojis, glassmorphism, and an "improvised" dark mode? This skill stops that.

You write a short `DESIGN.md` (the design contract for your project). A few small Python scripts check it — and the code your AI produces afterwards — against real design rules: 8px grid, WCAG contrast, sane typography, no forbidden tropes, no Three.js antipatterns. If anything drifts, the gate fails and tells you exactly what to fix.

Works the same way in Claude Code, Codex, OpenCode, Antigravity, or just your terminal. No API key, no cloud, no surprise — just Python.

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
| **Any other agent / plain shell** | Clone anywhere | Run the scripts directly with `python3 scripts/...` |

---

*Built to turn AI-generated code into exceptional design.*
