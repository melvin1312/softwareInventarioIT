## 2025-09-10 - Login Password Toggle & Skip-Link Accessibility

**Learning:** Static HTML prototypes often lack keyboard navigation skip-links and interactive password visibility unmasking logic. Adding explicit `aria-label`, `aria-pressed`, and `title` switches along with `pr-12` input padding ensures screen readers and keyboard users get complete visual and auditory context without overlapping layout issues.
**Action:** Always verify overlay buttons inside input fields have `pr-12` container spacing and dynamic `aria-pressed` state updates.
