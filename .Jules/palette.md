# Palette's Journal - Critical Learnings

## 2026-08-09 - Trailing Input Overlays and Padding Right
**Learning:** When using trailing absolute-positioned overlay elements (like custom password eye-toggles, search clear badges, or copy buttons) inside an input field container, the standard right padding (e.g. `pr-3`) on the `<input>` element allows user-typed text to visually overlap with the absolute-positioned overlay, which ruins readability and visual polish.
**Action:** Always ensure the input's right padding is set to at least `pr-12` (or more depending on the size of the overlay) when an absolute-positioned interactive element is placed trailing inside the input wrapper.
