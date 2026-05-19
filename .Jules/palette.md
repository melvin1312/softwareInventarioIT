## 2025-05-15 - Accessible Skip Links with Fixed Sidebars
**Learning:** When implementing skip-to-content links in layouts with fixed sidebars (z-50), the link requires an even higher z-index (e.g., z-[100]) and explicit positioning (fixed/absolute) to be visible. Tailwind's `not-sr-only` utility resets positioning to `static`, which can cause the link to be hidden behind fixed elements if not explicitly re-declared.
**Action:** Always use `focus:fixed` or `focus:absolute` along with a high `z-index` when using `focus:not-sr-only` for skip links in modern layouts.
