# Palette's Journal - Critical Learnings

## 2025-05-18 - Password Toggle and Skip Link UX Pattern
**Learning:** Adding interactive password toggling to static HTML login prototypes requires dynamic ARIA state (`aria-pressed`, `aria-label`, `title`) and icon synchronization (`textContent` + `data-icon`), as well as increasing right padding on the input field (`pr-12`) so text does not overlap the absolute-positioned toggle button. Furthermore, skip-to-content targets (`<main>`) must have `tabindex="-1"` and `outline-none` for clean keyboard focus management.
**Action:** When working with form inputs having absolute positioned right icons, ensure `pr-12` is set on the `<input>` element and maintain strict synchronization across visual icon and screen reader attributes during JS state updates.
