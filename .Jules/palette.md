# Palette's Journal - Critical UX Learnings

This journal tracks critical UX and accessibility learnings discovered during the development of the AssetTrack project.

---

## 2025-01-24 - Accessibility Foundations: Skip Links and Icon-Only Buttons
**Learning:** In highly structured dashboards with fixed navigation sidebars (z-50) and top bars, standard accessibility features like "Skip to Main Content" links are often overlooked. These links must have a higher z-index (e.g., z-[100]) and explicit positioning to be useful when focused. Additionally, the target element (<main>) requires `tabindex="-1"` and `outline-none` to receive programmatic focus smoothly without visual artifacts in Chromium.
**Action:** Always include a skip-to-content link as the first child of <body> and ensure all icon-only action buttons (like those in table rows) have both `aria-label` and `title` for screen readers and tooltips respectively.
