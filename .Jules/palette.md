# Palette's Journal - Critical Learnings

## 2025-05-20 - Password Visibility Toggle & Skip Link Patterns in Spanish Prototypes
**Learning:** In Spanish static HTML login prototypes, password visibility toggle buttons must explicitly manage screen reader accessibility attributes (`aria-pressed`, `aria-label`, `title`) in sync with dynamic DOM changes (`type`, `textContent`, `data-icon`) using Spanish localized strings ('Mostrar contraseña' / 'Ocultar contraseña'). Furthermore, skip-to-content targets need `id="main-content"`, `tabindex="-1"`, and `outline-none` on `<main>` for seamless keyboard navigation without browser focus artifacts.
**Action:** Always include localized `aria-label`/`title` and `aria-pressed` updates alongside icon toggling, and implement standardized Tailwind `sr-only focus:not-sr-only` skip links.
