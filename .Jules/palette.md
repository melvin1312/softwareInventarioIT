## 2025-05-15 - Password Visibility Toggle Pattern
**Learning:** Functional micro-interactions like password visibility toggles should update `aria-label` and `title` attributes dynamically to reflect the current state (e.g., switching between 'Mostrar contraseña' and 'Ocultar contraseña') to maintain screen reader accuracy and provide tooltips.
**Action:** Use a stable `id` for the toggle button and update its `textContent` (for icons) and accessibility attributes (`aria-label`, `title`) within the event listener.
