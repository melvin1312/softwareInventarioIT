## 2025-01-24 - [Password Visibility Interaction Pattern]
**Learning:** Functional micro-interactions like password visibility toggles in static prototypes require manual script injection and benefit from dynamic accessibility label updates to maintain screen reader accuracy.
**Action:** When implementing password toggles, always update `aria-label`, `title`, `textContent`, and `data-icon` simultaneously to ensure visual and assistive technology consistency.
