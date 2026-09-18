# Palette's Journal - Critical Learnings

## 2025-09-18 - Password Toggle UX & Input Overlay Padding
**Learning:** When adding absolute overlay elements (such as password visibility toggle buttons) inside input containers, inputs require sufficient right-padding (`pr-10` or `pr-12`) to prevent entered text from visually colliding with the overlay icon.
**Action:** Always set `pr-10`/`pr-12` on input elements that feature absolute right action buttons, and ensure proper `aria-label`, `aria-pressed`, `title`, and focus indicator rings are applied.
