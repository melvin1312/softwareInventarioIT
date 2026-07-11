# Palette's Journal - Critical UX Learnings

## 2024-07-11 - Standardizing Accessibility for Dashboard Actions
**Learning:** Icon-only interactive elements (like <span> or <button> with symbols) are often missed by keyboard and screen reader users if they lack semantic tags and descriptive labels. In AssetTrack dashboards, converting <span> triggers to <button> and adding both `aria-label` and `title` ensures parity between visual and assistive technology experiences.
**Action:** Always wrap Material Symbols icons in <button> elements when they are interactive, and apply the standardized focus-visible ring pattern (`focus-visible:ring-2 focus-visible:ring-secondary focus-visible:ring-offset-2 focus-visible:outline-none rounded`).
