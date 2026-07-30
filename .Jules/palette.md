# Palette Journal - Critical UX/A11y Learnings

This journal tracks critical UX and accessibility insights discovered across the AssetTrack prototypes.

## 2026-04-21 - Accessible and Interactive Password Visibility in Static Prototypes
**Learning:** Adding a keyboard-navigable password toggle to static login prototypes using custom `aria-pressed`, `aria-label`, and `title` attributes in Spanish ensures that the component is readable by screen readers and usable via keyboard shortcuts, matching the application's native language.
**Action:** When working on authentication or hidden data forms, look for static visual placeholders and replace them with fully accessible, dynamic toggles that maintain focus and ARIA state sync in vanilla JavaScript.
