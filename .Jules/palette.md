## 2025-01-24 - Accessible Skip Links in AssetTrack
**Learning:** Prototype files in this repository lack basic keyboard accessibility foundations like "Skip to Content" links, which are critical for navigating past the fixed 280px sidebar.
**Action:** Always check for and implement a "Saltar al contenido principal" link as the first child of <body>, targeting a <main id="main-content" tabindex="-1" class="outline-none"> element.
