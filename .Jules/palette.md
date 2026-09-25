# Palette's Journal - Critical UX & Accessibility Learnings

## 2025-05-18 - Synchronizing Password Visibility Toggles for Screen Readers
**Learning:** Toggling password field visibility requires updating `aria-pressed` (true when unmasked/text, false when masked/password), `aria-label`, `title`, visual textContent, and the `data-icon` attribute to ensure screen reader users and visual users remain perfectly aligned on the current security/masking state.
**Action:** Always synchronize `aria-pressed`, `aria-label`, `title`, and both textContent and `data-icon` attributes whenever unmasking sensitive text inputs in Spanish UI prototypes.
