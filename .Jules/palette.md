# Palette's Journal - Critical UX Learnings

## 2025-05-14 - Standardized Focus and Accessibility Patterns
**Learning:** Static prototypes in the AssetTrack project often lack basic keyboard accessibility (skip links, focus indicators) and form-label associations. A consistent pattern for focus-visible styling and skip-to-content links improves the Corporate Modernist aesthetic by providing clear, accessible feedback.
**Action:** Apply the following patterns consistently:
- **Skip Link:** `sr-only focus:not-sr-only focus:fixed focus:top-4 focus:left-4 focus:z-[100] focus:bg-secondary focus:text-white focus:px-4 focus:py-2 focus:rounded-lg focus:ring-2 focus:ring-secondary focus:ring-offset-2` (Target `#main-content` with `tabindex="-1" outline-none`).
- **Focus Indicator:** `focus-visible:ring-2 focus-visible:ring-secondary focus-visible:ring-offset-2 focus-visible:outline-none rounded`.
- **Form Labels:** Always use unique IDs and associate with `for` attributes.
- **Icon Buttons:** Always include both `aria-label` and `title` attributes.
