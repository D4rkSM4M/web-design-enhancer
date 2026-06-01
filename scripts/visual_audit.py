#!/usr/bin/env python3
"""
Visual Audit Script - Utilise Playwright pour vérifier le rendu réel du site.
Vérifie:
- Polices chargées (computed styles)
- Espacements réels (multiples de 8px)
- Absence d'éléments "AI slop" visibles (stickers, emojis non autorisés)
- Screenshots pour inspection humaine/IA

Usage:
    python3 visual_audit.py --url http://localhost:3000 --output ./audit-results
"""

import asyncio
import argparse
import os
import json
from pathlib import Path

async def run_audit(url, output_dir):
    from playwright.async_api import async_playwright

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    results = {
        "url": url,
        "fonts": [],
        "spacing_errors": [],
        "ai_slop_detected": [],
        "screenshots": {}
    }

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_context(viewport={'width': 1280, 'height': 800}).new_page()
        
        print(f"🌐 Navigation vers {url}...")
        try:
            await page.goto(url, wait_until="networkidle")
        except Exception as e:
            print(f"❌ Erreur de navigation: {e}")
            await browser.close()
            return

        # 1. Capture Screenshots (Desktop & Mobile)
        print("📸 Capture des screenshots...")
        await page.screenshot(path=str(output_path / "desktop.png"), full_page=True)
        results["screenshots"]["desktop"] = str(output_path / "desktop.png")
        
        await page.set_viewport_size({"width": 375, "height": 667})
        await page.screenshot(path=str(output_path / "mobile.png"), full_page=True)
        results["screenshots"]["mobile"] = str(output_path / "mobile.png")

        # 2. Audit Typographie et Espacements via JS
        print("🔍 Analyse du DOM et des styles calculés...")
        audit_data = await page.evaluate("""
            () => {
                const elements = document.querySelectorAll('h1, h2, h3, p, button, section, div');
                const fonts = new Set();
                const spacingErrors = [];
                const slopElements = [];
                
                const isMultipleOf8 = (val) => {
                    const num = parseInt(val);
                    return isNaN(num) || num === 0 || num % 8 === 0 || num === 4;
                };

                elements.forEach(el => {
                    const style = window.getComputedStyle(el);
                    
                    // Fonts
                    fonts.add(style.fontFamily);
                    
                    // Spacing (Padding/Margin)
                    ['paddingTop', 'paddingBottom', 'marginTop', 'marginBottom'].forEach(prop => {
                        if (!isMultipleOf8(style[prop])) {
                            spacingErrors.append(`${el.tagName} ${el.className}: ${prop}=${style[prop]}`);
                        }
                    });

                    // AI Slop (Emojis, stickers, generic icons, placeholders)
                    const text = el.innerText || "";
                    const emojiRegex = /[\\u{1F300}-\\u{1F9FF}]|[\\u{2700}-\\u{27BF}]/u;
                    if (emojiRegex.test(text) && !el.closest('footer')) {
                        slopElements.push(`Artefact IA (Emoji) détecté: "${text.substring(0, 20)}..."`);
                    }

                    const placeholderRegex = /logo-placeholder|your-logo|brandname|company-name/i;
                    if (placeholderRegex.test(text)) {
                        slopElements.push(`Logo/Nom générique détecté: "${text.substring(0, 20)}..."`);
                    }

                    // Détection des formes bizarres (stickers/placeholders SVG)
                    if (el.tagName === 'SVG' && el.getBBox().width > 0) {
                        const title = el.querySelector('title')?.textContent || "";
                        if (/sparkle|magic|bot|ai|stars/i.test(title)) {
                            slopElements.push(`Icône "Odeur d'IA" détectée: ${title}`);
                        }
                    }
                });

                return {
                    fonts: Array.from(fonts),
                    spacingErrors: spacingErrors,
                    slopElements: slopElements
                };
            }
        """)

        results["fonts"] = audit_data["fonts"]
        results["spacing_errors"] = audit_data["spacingErrors"]
        results["ai_slop_detected"] = audit_data["slopElements"]

        await browser.close()

    # Sauvegarder les résultats
    with open(output_path / "audit_report.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✅ Audit terminé. Résultats dans {output_dir}")
    print(f"📊 Polices détectées: {len(results['fonts'])}")
    print(f"⚠️  Erreurs d'espacement: {len(results['spacing_errors'])}")
    print(f"🚫 Éléments Slop: {len(results['ai_slop_detected'])}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://localhost:3000")
    parser.add_argument("--output", default="./audit-results")
    args = parser.parse_args()
    
    asyncio.run(run_audit(args.url, args.output))
