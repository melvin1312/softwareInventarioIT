# Palette's Journal

## 2026-03-07 - Password Visibility Toggle & Skip Link Micro-UX
**Learning:** When adding inline toggle buttons inside text input wrappers in Tailwind CSS forms, increasing padding right (`pr-10`) is essential to prevent long password inputs from overlapping the action icon. Additionally, updating both `aria-label`, `title`, `aria-pressed`, `textContent`, and `data-icon` ensures seamless accessibility across screen readers and Material Symbols font ligatures.
**Action:** Always pair `pr-10` padding with synchronized ARIA attributes and focus-visible rings whenever building password or search adornment toggles.
