# Palette's Journal - Critical Learnings Only

## 2024-08-07 - Accessible Login UX and Input Overlay Protection
**Learning:**
- Accessible Skip-to-Content links are vital for keyboard-only users to bypass branding or visual sidebars. Target elements like `<main>` need `id="main-content"`, `tabindex="-1"`, and `outline-none` for correct focus management without default focus rings.
- Absolute trailing elements (such as password toggle icons or search badges) placed within relative input wrappers will visually overlap with long user-entered text unless the input field's padding-right is set to a minimum of `pr-12` (or similar).
- Dynamically updating interactive elements (like the password unmask toggle button) must synchronize both visual elements (Material Symbols ligature textContent and custom `data-icon` attribute) and screen reader states (`aria-pressed="true|false"` alongside localized `aria-label`/`title` attributes in Spanish) to preserve a high-fidelity accessible experience.

**Action:**
- Always add a "Saltar al contenido principal" skip link when constructing or enhancing accessible static prototypes.
- Ensure any input field containing trailing absolute overlays has a robust right padding of at least `pr-12`.
- Fully synchronize screen reader attributes, icon ligatures, and data attributes whenever building interactive toggle elements.
