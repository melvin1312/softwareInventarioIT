# Palette's Journal - Critical UX & Accessibility Learnings

This journal contains critical learnings discovered during the implementation of UX and accessibility improvements in the AssetTrack project.

## 2025-06-16 - Accessible 'Skip to Main Content' Links
**Learning:** For SPAs or complex layouts with large sidebars (like AssetTrack's 280px sidebar), a 'Skip to Main Content' link is essential for keyboard users to bypass repetitive navigation. Using `sr-only` combined with `focus:not-sr-only` and explicit fixed positioning ensures it's only visible when needed and doesn't disrupt the layout.
**Action:** Always insert the skip link as the first child of `<body>`, target `<main id="main-content">`, and ensure the target has `tabindex="-1"` and `outline-none` for smooth focus transition without browser-default rings.
