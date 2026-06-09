## 2026-06-09 - Functional Password Visibility Toggle
**Learning:** In the AssetTrack design system, password inputs with visibility toggles require at least `pr-12` padding to prevent text overlap with the toggle button. Functional toggles should use `aria-pressed` and dynamic `aria-label` to communicate state correctly to screen readers.
**Action:** Always apply `pr-12` to password inputs with toggles and implement vanilla JS to sync `type`, `textContent` (icon), `aria-label`, and `aria-pressed`.
