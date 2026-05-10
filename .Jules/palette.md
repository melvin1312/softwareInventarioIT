## 2024-05-24 - Dynamic ARIA labels for functional toggles
**Learning:** For icon-only toggle buttons (like password visibility), updating the icon alone is insufficient for screen readers. The `aria-label` and `title` must be updated dynamically to reflect the *new* action available to the user.
**Action:** Always implement a JavaScript handler for toggles that synchronizes the DOM state with corresponding accessibility attributes (`aria-label`, `title`) and visual cues (Material Symbol name).
