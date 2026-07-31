# Palette's Journal

## 2026-07-31 - Overlapping Trailing Icons & Interactive Accessibility States in Spanish Prototypes
**Learning:** Inputs with absolute-positioned elements on the right (e.g., eye icons for password toggles or scanner icons) often default to standard small padding (`pr-3` or `pr-4`). Under long inputs, this causes text to visually overlap with the icon. Additionally, interactive toggles must maintain accurate screen reader states using `aria-pressed`, `aria-label`, and `title` translated to the correct target locale (Spanish in this system) to ensure an accessible, professional experience.
**Action:** When adding absolute trailing action icons or buttons inside input wrappers, always increase input right-padding to `pr-12` or similar. Pair this with standard focus-visible rings and a localized interactive JS state update that synchronizes HTML attributes with accessibility and icon states.
