# Palette's Journal - Critical UX/A11y Learnings

## 2026-04-21 - Accessible Keyboard and Screen Reader Password Toggling
**Learning:** For password visibility toggle buttons, standard interactive attributes (like type="button" instead of default submit, explicit `id`, sync'd `aria-label`, and `title`) combined with focus-visible visual indicators (`focus-visible:ring-2 focus-visible:ring-secondary`) significantly improve key usability for keyboard-only and screen reader users. Updating the textContent and data-icon attributes synchronously preserves layout consistency while avoiding screen reader confusion when toggling.
**Action:** When adding password inputs in prototypes, always wrap password-toggling logic in a robust vanilla script that maintains button accessibility labels, title, and Material Symbols ligatures in sync.

## 2026-04-21 - Skip to Main Content Link Layout Integration
**Learning:** Adding a "Skip to Main Content" link is standard practice, but it must be the very first child element under `<body>` to function correctly for keyboard users. To avoid layout shifts or breaking CSS grids, use absolute positioning (`sr-only focus:not-sr-only focus:fixed focus:top-4 focus:left-4 focus:z-[100]`) and target the main element using `id="main-content"` combined with `tabindex="-1"` and `outline-none` so it receives programmatical focus without visual focus rings on click.
**Action:** Always place the skip-to-content link as the absolute first child of `<body>` and configure the target element with `tabindex="-1"` and `outline-none` to guarantee seamless focus management.
