## 2025-05-14 - Tailwind Skip-Link Positioning
**Learning:** Tailwind's `not-sr-only` utility resets an element's position to `static`. If a skip-link needs to be fixed or absolute when focused (which is typical), these positioning classes must be explicitly added with the `focus:` prefix alongside `focus:not-sr-only`.
**Action:** Always use `focus:fixed` or `focus:absolute` when implementing skip-links with `sr-only focus:not-sr-only`.

## 2025-05-14 - Dynamic Accessibility Labels for Interactive Elements
**Learning:** Functional micro-interactions like password visibility toggles must update `aria-label` and `title` attributes dynamically via JavaScript to maintain screen reader accuracy and provide correct visual tooltips as the state changes.
**Action:** Include attribute updates (e.g., `setAttribute('aria-label', ...)` in the event listener of toggle components.
