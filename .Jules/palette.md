# Palette's Journal - Critical UX & Accessibility Learnings

This journal tracks critical UX and accessibility learnings discovered during the design and development of the AssetTrack platform.

## 2026-04-21 - Standardizing Skip-to-Content and Keyboard Focus in High-Density Dashboards
**Learning:** High-density IT dashboards often lack core keyboard navigation pathways. Providing a 'Skip to Main Content' ('Saltar al contenido principal') link is critical for screen reader and keyboard-only users to bypass repeated sidebar and header elements. Additionally, removing standard browser focus outlines without replacing them with custom focus-visible indicators makes keyboard navigation impossible.
**Action:** Always include a skip-to-content link styled with the Tailwind screen-reader focus pattern, pair it with a target container using `id="main-content" tabindex="-1" class="outline-none"`, and ensure interactive elements utilize the standardized focus-visible rings (`ring-2 ring-secondary ring-offset-2`).
