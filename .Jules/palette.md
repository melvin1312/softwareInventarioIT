# Palette's Journal - Critical Learnings

## 2025-05-18 - Password Visibility Toggle & Skip-to-Content Pattern in Spanish Prototypes
**Learning:** In Spanish language prototype views, password unmasking triggers and skip links require specific ARIA sync (`aria-pressed`, localized `aria-label`/`title`, `data-icon` and `textContent` updates) alongside `pr-10` input padding to prevent text collision. Main content targets need `tabindex="-1"` and `outline-none` for clean keyboard focus without focus rings on structural containers.
**Action:** Always pair `aria-pressed` with matching Spanish labels ("Mostrar contraseña" / "Ocultar contraseña") and ensure `tabindex="-1"` on `<main id="main-content">`.
