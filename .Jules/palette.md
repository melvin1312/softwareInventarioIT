## 2025-05-18 - Synchronizing Password Visibility Toggle ARIA States in Spanish Prototypes

**Learning:** When adding password visibility toggles to localized forms, toggling the input type (`password` <-> `text`) alone is insufficient for screen reader users. Dynamic updating of `aria-pressed`, `aria-label`, `title`, and icon attributes (`data-icon`) ensures screen reader feedback matches visual status.

**Action:** Always synchronize `aria-pressed="true|false"` alongside localized labels ("Ocultar contraseña" / "Mostrar contraseña") and adjust input right-padding (`pr-10`) to prevent text overlap with absolute-positioned action buttons.
