## 2025-05-18 - Password Toggle Accessibility & Input Padding
**Learning:** Adding a password unmasking toggle requires synchronized screen-reader state properties (`aria-pressed`, dynamic `aria-label`/`title`), keyboard focus rings (`focus-visible:ring-2`), and `pr-12` input padding to prevent text overlap with absolute overlay icons.
**Action:** Always pair password unmasking toggles with `aria-pressed`, localized labels, keyboard focus styling, and adequate right-padding on the input field.
