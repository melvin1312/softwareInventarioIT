# Palette's Journal - Critical Learnings Only

## 2023-11-23 - Accessible Password Visibility Toggle Pattern
**Learning:** Static prototypes in this project lack interactive feedback and ARIA associations for security-sensitive fields. A consistent pattern for password toggles improves both micro-UX (unmasking) and accessibility (screen reader state).
**Action:** Use standardized `focus-visible:ring-secondary` on the toggle button and dynamically update `aria-label`, `title`, and `data-icon` (Material Symbols) within a `DOMContentLoaded` script block at the end of the `<body>`.
