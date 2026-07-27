# Palette's Journal - Critical UX Learnings

This journal tracks critical UX and accessibility learnings, patterns, and decisions for the AssetTrack application.

## 2026-04-21 - Input Padding with Trailing Elements & Icon-Only Toggle Accessibility
**Learning:** In the "Corporate Modernist" design system, form inputs that include absolutely positioned trailing action components (like password visibility buttons) suffer from visual overlap if standard trailing padding (`pr-3`) is used. To prevent text characters from colliding with icons, inputs with standard trailing icons/buttons require a padding layout pattern of `pr-12`. Additionally, interactive icon-only buttons in static HTML prototypes require explicit visual focus rings (`focus-visible:ring-2 focus-visible:ring-secondary`) and descriptive ARIA label updates corresponding with their interactive states (e.g. toggling `aria-label` and `title` alongside script behaviors).
**Action:** Always verify right-side padding (`pr-12` minimum) on inputs with trailing buttons, and ensure all icon-only toggles have active state-aware ARIA attributes and focus-visible rings for keyboard users.
