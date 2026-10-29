## 2025-05-18 - Synchronized Password Toggle State and Focus Padding
**Learning:** Adding interactive password visibility toggles requires proper right padding (`pr-10`) on the input field so long passwords do not visually overlap the icon button, as well as synchronizing `aria-label`, `aria-pressed`, `title`, and icon attributes (`textContent` & `data-icon`) for screen readers.
**Action:** When adding password unmasking features, apply `pr-10` padding to input fields and update all ARIA and DOM attributes synchronously on toggle events.
