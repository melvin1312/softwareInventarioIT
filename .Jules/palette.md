## 2025-05-18 - Password Visibility Toggle & Skip Link Accessibility
**Learning:** Password toggle buttons inside password fields require matching right-padding on the input (e.g. `pr-10`) to avoid text overlap. Furthermore, screen readers need dynamic synchronization across `aria-pressed`, `aria-label`, `title`, icon `textContent`, and `data-icon` attributes when unmasking passwords in Spanish UI interfaces.
**Action:** When adding password visibility toggles, ensure `pr-10`/`pr-12` input padding and update all ARIA/title/icon attributes in tandem upon click.
