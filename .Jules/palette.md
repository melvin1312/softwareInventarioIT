## 2025-05-18 - Interactive Password Toggle & Skip Link Accessibility
**Learning:** In login prototypes, password toggles often lack screen reader attributes (`aria-pressed`, dynamic `aria-label`/`title`) and vanilla JS functionality, while input text can overflow behind the toggle button without `pr-12` padding.
**Action:** Always complement password visibility toggle buttons with `id="toggle-password"`, `pr-12` right-padding on the input, dynamic ARIA state switching, and skip-to-content navigation (`Saltar al contenido principal`).
