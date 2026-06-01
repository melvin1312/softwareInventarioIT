## 2025-06-01 - Standardized Accessibility for Icon-only Buttons
**Learning:** Icon-only buttons in the AssetTrack prototypes frequently lack `aria-label` and `title` attributes, making them inaccessible to screen readers and providing no visual tooltips for sighted users.
**Action:** Always include both `aria-label` and `title` attributes on icon-only buttons, and apply `focus-visible:ring-2 focus-visible:ring-secondary focus-visible:ring-offset-2 focus-visible:outline-none` for standardized keyboard navigation feedback.
