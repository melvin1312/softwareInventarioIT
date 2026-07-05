## 2025-01-24 - [Accessible Password Toggle]
**Learning:** Functional micro-interactions like password visibility toggles must include dynamic ARIA labels and title updates to remain accessible to screen reader users after the state changes.
**Action:** Always update `aria-label` and `title` attributes alongside the input `type` and icon text when implementing toggles.
