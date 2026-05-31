## 2025-05-14 - Accessible Password Visibility Toggle
**Learning:** Functional micro-interactions like password visibility toggles should update aria-label and title attributes dynamically to reflect the current state (e.g., switching between 'Mostrar contraseña' and 'Ocultar contraseña') to maintain screen reader accuracy.
**Action:** Always use ARIA attributes (`aria-pressed`, `aria-label`, `aria-controls`) and update them via JavaScript alongside the visual icon change. Ensure the input has sufficient padding to avoid text overlap with the toggle button.
