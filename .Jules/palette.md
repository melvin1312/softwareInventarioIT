# Palette's UX Journal

## 2026-04-21 - Accessible Multi-state Password Masking and Skip Links in Spanish Prototypes
**Learning:** For secure localized applications (Spanish/es), custom elements like password visibility toggles and skip links must not only be visually appealing but also carry fully synchronized screen reader attributes (e.g., `aria-pressed`, `aria-label`, `title`). Furthermore, trailing absolute-positioned buttons inside interactive inputs require proportional right padding on the input itself (at least `pr-12`) to prevent visual overlap when entering long user credentials.
**Action:** Always verify overlay buttons inside inputs have proper right padding to prevent layout overlaps, use standard Spanish localized accessibility labels, and implement target element container focus management via `tabindex="-1"` and `outline-none`.
