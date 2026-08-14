# Palette's Journal - Critical UX/Accessibility Learnings

This journal tracks critical UX and accessibility insights discovered during development.

## 2025-08-14 - Overlapping Text with Absolute Input Overlays
**Learning:** In highly compact modern designs like "Corporate Modernist", trailing action/toggle icons (e.g. password visibility toggles, QR scanner search buttons) are often placed inside relative-positioned input boxes as absolute-positioned overlays on the right. When the user enters long inputs, the text visually collides with or hides beneath the absolute element if default right-padding is not sufficiently increased.
**Action:** Always ensure any text input wrapping a trailing absolute overlay has right-padding set to at least `pr-12` (or equivalent `3rem` space) to guarantee long user entries remain fully legible and never overlap the interactive elements.
