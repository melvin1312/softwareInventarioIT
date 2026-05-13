## 2026-05-13 - [Skip Link Accessibility with Fixed Layouts]
**Learning:** In layouts with fixed sidebars (z-50), skip-to-content links require explicit positioning (e.g., `focus:fixed`) and a high z-index (e.g., `focus:z-[100]`) to remain visible on focus. Additionally, Tailwind's `not-sr-only` utility resets positioning to `static`, so the desired position (fixed/absolute) must be re-declared.
**Action:** Always use `focus:fixed` (or `focus:absolute`) along with `focus:not-sr-only` and high z-index for skip-links in this project's fixed-sidebar architecture.
