"""
tests/test_audit_style_uniqueness.py
Tests for the Generic AI Template detector (audit_style_uniqueness.py).
Each test validates that a specific template signal is correctly detected or correctly ignored.
"""
import tempfile
import textwrap
from pathlib import Path

import pytest
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from audit_style_uniqueness import StyleUniquenessAuditor


# ─── Helpers ────────────────────────────────────────────────────────────────

def _make_project(files: dict[str, str]) -> Path:
    """Create a temporary directory with the given {filename: content} files."""
    tmp = Path(tempfile.mkdtemp())
    for fname, content in files.items():
        fp = tmp / fname
        fp.parent.mkdir(parents=True, exist_ok=True)
        fp.write_text(textwrap.dedent(content), encoding="utf-8")
    return tmp


def _audit(files: dict[str, str], warn=40, block=65) -> StyleUniquenessAuditor:
    root = _make_project(files)
    auditor = StyleUniquenessAuditor(root_path=root, threshold_warn=warn, threshold_block=block)
    auditor.scan()
    return auditor


def _triggered_ids(auditor: StyleUniquenessAuditor) -> set[str]:
    return {v["id"] for v in auditor.violations}


# ─── T1: Blue → purple hero gradient ────────────────────────────────────────

class TestT1HeroGradient:
    def test_classic_blue_purple_gradient_detected(self):
        a = _audit({"styles.css": """
            .hero {
                background: linear-gradient(135deg, #3B82F6, #8B5CF6);
            }
        """})
        assert "T1" in _triggered_ids(a)

    def test_tailwind_class_gradient_detected(self):
        a = _audit({"index.html": """
            <div class="from-blue-500 to-purple-500 hero">Hello</div>
        """})
        assert "T1" in _triggered_ids(a)

    def test_non_blue_purple_gradient_not_detected(self):
        a = _audit({"styles.css": """
            .hero {
                background: linear-gradient(135deg, #e8f5e9, #1b5e20);
            }
        """})
        assert "T1" not in _triggered_ids(a)

    def test_solid_color_hero_not_detected(self):
        a = _audit({"styles.css": """
            .hero { background: #0f0f0f; }
        """})
        assert "T1" not in _triggered_ids(a)


# ─── T2: Inter + Poppins combo ──────────────────────────────────────────────

class TestT2FontCombo:
    def test_both_inter_and_poppins_detected(self):
        a = _audit({"styles.css": """
            body { font-family: 'Inter', sans-serif; }
            h1   { font-family: 'Poppins', sans-serif; }
        """})
        assert "T2" in _triggered_ids(a)

    def test_only_inter_not_detected(self):
        a = _audit({"styles.css": """
            body { font-family: 'Inter', sans-serif; }
        """})
        assert "T2" not in _triggered_ids(a)

    def test_only_poppins_not_detected(self):
        a = _audit({"styles.css": """
            body { font-family: 'Poppins', sans-serif; }
        """})
        assert "T2" not in _triggered_ids(a)

    def test_different_combo_not_detected(self):
        a = _audit({"styles.css": """
            body { font-family: 'Fraunces', serif; }
            code { font-family: 'JetBrains Mono', monospace; }
        """})
        assert "T2" not in _triggered_ids(a)


# ─── T3: Testimonial card ────────────────────────────────────────────────────

class TestT3TestimonialCard:
    def test_testimonial_card_class_detected(self):
        a = _audit({"index.html": """
            <div class="testimonial-card">
                <p>Great product!</p>
            </div>
        """})
        assert "T3" in _triggered_ids(a)

    def test_review_card_class_detected(self):
        a = _audit({"styles.css": """
            .review-card { padding: 24px; border-radius: 8px; }
        """})
        assert "T3" in _triggered_ids(a)

    def test_regular_card_not_detected(self):
        a = _audit({"index.html": """
            <div class="feature-card">
                <h3>Feature</h3>
            </div>
        """})
        assert "T3" not in _triggered_ids(a)


# ─── T4: Glassmorphism spam ───────────────────────────────────────────────────

class TestT4GlassmorphismSpam:
    def test_three_or_more_backdrop_detected(self):
        a = _audit({"styles.css": """
            .card1 { backdrop-filter: blur(10px); }
            .card2 { backdrop-filter: blur(8px); }
            .card3 { backdrop-filter: blur(12px); }
        """})
        assert "T4" in _triggered_ids(a)

    def test_two_backdrops_not_detected(self):
        a = _audit({"styles.css": """
            .modal   { backdrop-filter: blur(10px); }
            .tooltip { backdrop-filter: blur(4px); }
        """})
        assert "T4" not in _triggered_ids(a)

    def test_no_backdrop_not_detected(self):
        a = _audit({"styles.css": """
            .card { background: rgba(255,255,255,0.1); }
        """})
        assert "T4" not in _triggered_ids(a)


# ─── T5: All 4 generic SaaS sections ─────────────────────────────────────────

class TestT5SectionCombo:
    def test_all_four_sections_detected(self):
        a = _audit({"index.html": """
            <section id="hero">...</section>
            <section id="features">...</section>
            <section id="testimonials">...</section>
            <section id="cta">...</section>
        """})
        assert "T5" in _triggered_ids(a)

    def test_only_three_sections_not_detected(self):
        a = _audit({"index.html": """
            <section id="hero">...</section>
            <section id="features">...</section>
            <section id="cta">...</section>
        """})
        assert "T5" not in _triggered_ids(a)


# ─── T7: Uniform 3-column grid ───────────────────────────────────────────────

class TestT7ThreeColGrid:
    def test_repeat_3_1fr_detected(self):
        a = _audit({"styles.css": """
            .grid { grid-template-columns: repeat(3, 1fr); }
        """})
        assert "T7" in _triggered_ids(a)

    def test_tailwind_grid_cols_3_detected(self):
        a = _audit({"index.html": """
            <div class="grid grid-cols-3 gap-8">...</div>
        """})
        assert "T7" in _triggered_ids(a)

    def test_asymmetric_grid_not_detected(self):
        a = _audit({"styles.css": """
            .grid { grid-template-columns: 2fr 1fr; }
        """})
        assert "T7" not in _triggered_ids(a)


# ─── T8: Dramatic card shadow ─────────────────────────────────────────────────

class TestT8DramaticShadow:
    def test_0_25px_shadow_detected(self):
        a = _audit({"styles.css": """
            .card { box-shadow: 0 25px 50px rgba(0,0,0,0.25); }
        """})
        assert "T8" in _triggered_ids(a)

    def test_0_20px_shadow_detected(self):
        a = _audit({"styles.css": """
            .card { box-shadow: 0 20px 40px rgba(0,0,0,0.15); }
        """})
        assert "T8" in _triggered_ids(a)

    def test_subtle_shadow_not_detected(self):
        a = _audit({"styles.css": """
            .card { box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        """})
        assert "T8" not in _triggered_ids(a)

    def test_no_shadow_not_detected(self):
        a = _audit({"styles.css": """
            .card { border: 1px solid #e5e7eb; }
        """})
        assert "T8" not in _triggered_ids(a)


# ─── T9: Unsolicited decorative animations ───────────────────────────────────

class TestT9UnsoliticitedAnimation:
    def test_float_keyframe_detected(self):
        a = _audit({"styles.css": """
            @keyframes float {
                0%, 100% { transform: translateY(0); }
                50%       { transform: translateY(-10px); }
            }
        """})
        assert "T9" in _triggered_ids(a)

    def test_pulse_keyframe_detected(self):
        a = _audit({"styles.css": """
            @keyframes pulse { 0% { opacity:1; } 100% { opacity:0.5; } }
        """})
        assert "T9" in _triggered_ids(a)

    def test_entrance_animation_not_detected(self):
        a = _audit({"styles.css": """
            @keyframes fade-in {
                from { opacity: 0; transform: translateY(8px); }
                to   { opacity: 1; transform: translateY(0); }
            }
        """})
        assert "T9" not in _triggered_ids(a)


# ─── T12: Tailwind blue-500 hardcoded ────────────────────────────────────────

class TestT12TailwindBlue:
    def test_3b82f6_detected(self):
        a = _audit({"styles.css": """
            .button { background-color: #3B82F6; }
        """})
        assert "T12" in _triggered_ids(a)

    def test_lowercase_3b82f6_detected(self):
        a = _audit({"index.html": """
            <div style="color: #3b82f6">text</div>
        """})
        assert "T12" in _triggered_ids(a)

    def test_custom_property_not_detected(self):
        a = _audit({"styles.css": """
            .button { background-color: var(--primary); }
            :root { --primary: #2563EB; }
        """})
        assert "T12" not in _triggered_ids(a)


# ─── Score and exit code logic ────────────────────────────────────────────────

class TestScoreAndExitCode:
    def test_clean_project_score_zero(self):
        a = _audit({"styles.css": """
            :root { --primary: #2C4A2E; }
            body { font-family: 'Fraunces', serif; background: #FAF8F4; }
            .hero { background: var(--primary); }
            .card { border: 1px solid #e5e7eb; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
        """})
        assert a.capped_score == 0
        assert a._exit_code() == 0

    def test_high_score_blocked(self):
        # Plant multiple high-weight signals
        a = _audit({
            "styles.css": """
                .hero { background: linear-gradient(135deg, #3B82F6, #8B5CF6); }
                body  { font-family: 'Inter', sans-serif; }
                h1    { font-family: 'Poppins', sans-serif; }
                .card1 { backdrop-filter: blur(10px); box-shadow: 0 25px 50px rgba(0,0,0,0.25); }
                .card2 { backdrop-filter: blur(8px); }
                .card3 { backdrop-filter: blur(12px); }
                @keyframes float { 0% { transform: translateY(0); } }
                .btn  { color: #3B82F6; }
                .testimonial-card { padding: 24px; }
                .grid { grid-template-columns: repeat(3, 1fr); }
            """,
            "index.html": """
                <section id="hero">...</section>
                <section id="features">...</section>
                <section id="testimonials">...</section>
                <section id="cta">...</section>
            """,
        })
        assert a.capped_score > 65
        assert a._exit_code() == 2

    def test_warning_zone(self):
        # One high-weight + one medium — should land in warning zone
        a = _audit({"styles.css": """
            .hero { background: linear-gradient(135deg, #3B82F6, #8B5CF6); }
            .card1 { backdrop-filter: blur(10px); }
            .card2 { backdrop-filter: blur(8px); }
            .card3 { backdrop-filter: blur(6px); }
        """}, warn=20, block=65)
        assert a.capped_score > 20
        assert a._exit_code() in (1, 2)

    def test_score_capped_at_100(self):
        # Even if raw weights sum > 100, capped_score must be <= 100
        a = _audit({
            "styles.css": """
                .hero { background: linear-gradient(135deg, #3B82F6, #8B5CF6); }
                body  { font-family: 'Inter', sans-serif; }
                h1    { font-family: 'Poppins', sans-serif; }
                .c1 { backdrop-filter: blur(10px); }
                .c2 { backdrop-filter: blur(8px); }
                .c3 { backdrop-filter: blur(6px); }
                @keyframes float {}
                @keyframes pulse {}
                .btn { color: #3B82F6; }
                .card { box-shadow: 0 25px 50px rgba(0,0,0,.2); }
                .grid { grid-template-columns: repeat(3, 1fr); }
                .testimonial-card { padding: 8px; }
                .review-card { margin: 4px; }
            """,
            "index.html": """
                <section id="hero">Hero</section>
                <section id="features">Features</section>
                <section id="testimonials">Testimonials</section>
                <section id="cta">CTA</section>
                <span class="badge pill">🚀 New</span>
            """,
        })
        assert a.capped_score <= 100


# ─── Ignore vendor/build directories ─────────────────────────────────────────

class TestSkipDirs:
    def test_node_modules_ignored(self):
        a = _audit({
            "node_modules/bootstrap/styles.css": """
                .hero { background: linear-gradient(135deg, #3B82F6, #8B5CF6); }
            """,
            "src/app.css": """
                :root { --primary: #1a1a1a; }
            """,
        })
        assert "T1" not in _triggered_ids(a)

    def test_dist_ignored(self):
        a = _audit({
            "dist/bundle.css": """
                .hero { background: linear-gradient(135deg, #3B82F6, #8B5CF6); }
                body { font-family: 'Inter', sans-serif; }
                h1   { font-family: 'Poppins', sans-serif; }
            """,
        })
        assert not _triggered_ids(a)
