# Palette Journal

## 2026-06-18 - [Skip to Main Content Link Implementation]
**Learning:** For keyboard-only and screen reader users, a "Skip to Main Content" link is a critical micro-UX improvement that allows them to bypass repetitive navigation elements. In this repository, the presence of a 280px wide fixed sidebar makes this even more important.
**Action:** When working on new prototype screens in AssetTrack, always ensure a skip-to-content link is present as the first child of `<body>` and targets a `<main id="main-content" tabindex="-1">` element.
