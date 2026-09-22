## 2025-09-22 - Accessible Password Toggle & Skip Navigation
**Learning:** In Spanish static prototypes, password visibility toggles need synchronized `aria-label`/`title` ("Mostrar contraseña" / "Ocultar contraseña") and `aria-pressed` state ("false" / "true") alongside `data-icon` and `textContent` updates for screen reader clarity.
**Action:** Always include complete ARIA accessibility attributes (`aria-pressed`, `aria-label`, `title`) when implementing interactive password toggles in HTML prototypes.
