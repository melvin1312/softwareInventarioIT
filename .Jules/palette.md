## 2025-09-16 - Password Toggle ARIA Synchronization in Spanish Prototypes
**Learning:** In Spanish UI prototypes with static HTML and Material Symbols, toggling password visibility requires updating both `aria-pressed`, localized `aria-label`/`title` ("Mostrar contraseña" / "Ocultar contraseña"), and both `textContent` and `data-icon` attributes ("visibility" / "visibility_off") to preserve screen reader accuracy and icon visual state.
**Action:** When adding password visibility toggles, ensure `aria-pressed`, localized labels, and icon `data-icon` attributes are updated synchronously in JS.
