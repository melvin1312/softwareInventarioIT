# Palette's Journal - Critical UX Learnings

## 2025-05-14 - Standardizing Dashboard Accessibility
**Learning:** AssetTrack dashboards often lack fundamental accessibility hooks like "Skip to Content" links and descriptive labels for icon-only table actions (`more_vert`). The fixed sidebar (280px) and top header (16px/h-16) require the skip link to have high z-index and explicit positioning to remain visible when focused.
**Action:** Always implement the `sr-only focus:not-sr-only` skip-link pattern as the first child of `<body>` and target a `<main id="main-content" tabindex="-1">` element. Ensure icon-only buttons use both `aria-label` and `title` for screen readers and tooltips.
