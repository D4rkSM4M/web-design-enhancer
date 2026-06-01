# Meilleures Pratiques GSAP pour l'UI

GSAP (GreenSock Animation Platform) est l'outil standard pour des animations web performantes et fluides.

## Principes de base
- **Performance** : Privilégier l'animation des `transforms` (`x`, `y`, `rotation`, `scale`) et de l'`opacity`. Ces propriétés ne provoquent pas de recalcul du layout (reflow).
- **Shorthand GSAP** :
  - `x: 100` au lieu de `translateX(100px)`
  - `yPercent: 50` au lieu de `translateY(50%)`
  - `autoAlpha: 0` combine `opacity: 0` et `visibility: hidden`

## Patterns d'animation UI courants
1. **Entrées Staggered (échelonnées)** :
   ```javascript
   gsap.from(".card", {
     opacity: 0,
     y: 20,
     stagger: 0.1,
     duration: 0.8,
     ease: "power2.out"
   });
   ```
2. **ScrollTrigger** : Déclencher des animations au défilement.
3. **Hover Effects** : Utiliser des timelines pour des transitions fluides au survol.
4. **Micro-interactions** : Petits retours visuels sur les boutons ou icônes.

## Conseils de Designer
- **Ease** : Utiliser `power2.out` pour les entrées (ralentissement à la fin) et `power2.in` pour les sorties. `expo.out` pour un effet plus premium/vif.
- **Durée** : Garder les animations UI entre 0.2s et 0.6s. Plus c'est long, plus l'interface semble lente.
- **Accessibilité** : Respecter `prefers-reduced-motion`.
