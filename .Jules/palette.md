# Palette Journal

## 2024-10-31 - Password Visibility Toggle & Skip Link Micro-UX in Login Screen
**Learning:** In static authentication prototypes using Tailwind and Material Symbols ligatures, password visibility toggles often exist only as non-interactive decorative icon buttons inside input wrappers. When implementing interactivity, it is essential to increase trailing padding on the input (e.g. `pr-12`) to prevent text collision, update both ligature text and `data-icon` attribute for icon fidelity, and pair state changes with localized ARIA labels and `aria-pressed`.
**Action:** When adding password unmasking to prototype inputs, ensure `pr-12` is applied to `<input>`, synchronize `aria-pressed`, `aria-label`, and `title` alongside Material Symbol ligature updates, and add a keyboard-accessible Skip-to-content link to `<main tabindex="-1">`.
