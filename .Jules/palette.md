# Palette's UX & Accessibility Journal

## 2025-05-18 - Interactive Password Visibility & Focus Management
**Learning:** In login forms, password toggle buttons require synced `aria-pressed`, dynamic `aria-label`, `title`, and updating both `textContent` and `data-icon` attributes so that screen readers and icon fonts reflect state changes consistently.
**Action:** When implementing password unmasking features, ensure all ARIA state attributes, input `pr-10` padding, and icon attributes update synchronously in vanilla JS.
