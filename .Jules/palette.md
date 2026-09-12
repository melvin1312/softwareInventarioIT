## 2025-05-18 - Password Visibility Toggle ARIA States & Focus Management

**Learning:** Static HTML prototypes often lack interactive feedback for password inputs and screen reader accessible toggle controls. When toggling password visibility, `aria-pressed` should sync with the boolean state, while `aria-label` and `title` switch localized descriptions ('Mostrar contraseña' / 'Ocultar contraseña') alongside input padding (`pr-12`) to prevent text overlapping overlay buttons.
**Action:** Always pair password toggles with dynamic `aria-pressed`, localized `aria-label` updates, input `pr-12` padding, and standard `focus:ring-2` styling.
