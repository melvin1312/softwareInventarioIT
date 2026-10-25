## 2025-05-18 - Accessible Password Visibility Toggles & Skip Links
**Learning:** In login prototypes with password visibility toggles, adding `aria-pressed`, dynamic `aria-label`/`title` attributes, and `pr-10` padding to the password input ensures long passwords do not visually overlap with icon buttons while keeping screen readers synchronized.
**Action:** Always complement password toggles with right-padding adjustments on the input wrapper and update `aria-pressed` alongside text content and `data-icon` attributes.
