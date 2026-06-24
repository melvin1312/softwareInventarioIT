# Palette's Journal - Critical UX Learnings
## 2026-06-24 - [Skip-to-Content Pattern]
**Learning:** Static HTML prototypes in this repository often lack basic keyboard accessibility foundations like skip-to-content links, which are critical for navigating past fixed sidebars.
**Action:** Always check for and implement a 'Skip to Main Content' link as the first child of the <body>, targeting the <main> element with id='main-content' and tabindex='-1'.
