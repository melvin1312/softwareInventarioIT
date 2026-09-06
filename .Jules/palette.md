# Palette Journal - Critical UX & Accessibility Learnings

## 2026-03-06 - Password Input Visual Overlap & Accessible Toggle States
**Learning:** In static form layouts with trailing absolute overlay elements (such as password visibility toggle icons), standard `pr-3` padding causes entered text to visually collide with the toggle button. Setting `pr-12` on the input provides sufficient clearance. Furthermore, password visibility toggles require synchronized `aria-pressed`, localized `aria-label`/`title`, `textContent` ligature, and `data-icon` attribute updates to provide full accessibility for screen readers and consistency with Material Symbols.
**Action:** Always check input right padding when placing absolute icon buttons inside input wrappers, and ensure password toggles update `aria-pressed`, `aria-label`, `title`, and both icon textContent and `data-icon` attributes dynamically.
