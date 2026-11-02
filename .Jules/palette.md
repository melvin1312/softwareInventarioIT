# Palette's Journal - Critical UX/A11y Learnings

## 2024-05-24 - Dynamic ARIA attributes and text padding on password visibility toggles
**Learning:** For icon-only toggle buttons embedded inside inputs (like password visibility), changing the icon alone is insufficient for screen readers. The `aria-pressed`, `aria-label`, and `title` attributes must be synchronized dynamically to clearly communicate the current toggle state and the action triggered upon activation. In addition, right-hand input padding (`pr-10` or `pr-12`) is essential to prevent user-typed text from overlapping the overlay toggle button.
**Action:** When implementing password unmasking, always pair dynamic ARIA updates (`aria-pressed`, `aria-label`, `title`) and icon synchronization with adequate right padding on the input wrapper.
