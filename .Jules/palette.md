# Palette's Journal - Critical UX Learnings

This journal tracks critical UX and accessibility learnings for the AssetTrack project.

## 2024-06-17 - Functional Password Visibility Toggle
**Learning:** Static prototypes in this repository often lack functional micro-interactions. Implementing a password visibility toggle requires not only switching the input type but also updating the Material Symbols text, the `data-icon` attribute, and ARIA labels to maintain accessibility and visual consistency.
**Action:** Use a Vanilla JavaScript `DOMContentLoaded` listener at the end of the body to attach toggle logic, ensuring `aria-label` and `title` are synchronized with the visible state.
