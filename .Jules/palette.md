## 2025-10-21 - Accessible Password Toggle & Focus Management
**Learning:** Adding a password toggle to input wrappers requires sufficient right padding (e.g. `pr-10`) on the input to avoid text overlap, as well as keeping screen-reader attributes (`aria-pressed`, `aria-label`, `title`, icon content and `data-icon`) strictly synchronized when unmasking.
**Action:** Always pair `aria-pressed` with updated localized labels ("Mostrar contraseña" / "Ocultar contraseña") and ensure `focus-visible` ring styling is applied.
