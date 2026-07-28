# Palette's UX & Accessibility Journal

## 2025-07-28 - Standardizing Trailing Interactive Form Controls and Skip Links
**Learning:** In static HTML prototypes, form controls often lack functional interactive states. Adding interactive details (like password visibility toggles or submit loaders) is a perfect micro-UX enhancement, but we must protect usability. Specifically:
- Trailing absolute elements in text inputs require matching padding (`pr-12` or `pr-20` for badges) to prevent user-typed text from overlapping the icons.
- Buttons triggering visibility/state toggles must sync their `aria-label`, `title`, and Material Icon ligatures/data-attributes simultaneously.
- A Skip-to-Content link requires a clear target element with `#main-content`, `tabindex="-1"`, and `outline-none` so that focus moves cleanly without showing default browser focus outlines.

**Action:** When adding trailing elements or skip links, always apply standard padding, clear tabindex targets, and fully synchronized ARIA attributes via vanilla JS event listeners.
