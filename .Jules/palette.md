# Palette UX & Accessibility Journal

## 2025-05-18 - Password Visibility and Skip Link Micro-UX
**Learning:** In static authentication screens, users frequently mistype long or complex corporate passwords without immediate visual feedback. Adding a lightweight, keyboard-accessible password toggle with synchronized `aria-pressed`, `aria-label`, and `title` attributes alongside `pr-10` input padding prevents visual collisions while enhancing usability. Pairing it with a skip-to-content target on `<main id="main-content" tabindex="-1">` completes keyboard navigability without introducing external dependencies.
**Action:** Always synchronize `aria-pressed` ("true"/"false"), update both text content and `data-icon` for Material Symbols ligatures, and pad input wrappers appropriately (`pr-10` or higher) when placing action buttons at the end of form fields.
