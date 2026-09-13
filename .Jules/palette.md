# Palette Agent Journal

## 2024-05-20 - Icon-Only Action Buttons in Data Tables & Offboarding Screens
**Learning:** Icon-only action buttons in offboarding/HR views (like `assignment_return` or header controls like `notifications` and `history`) frequently lack accessible labels and focus rings, causing accessibility barriers for keyboard/screen reader users.
**Action:** Always provide explicit `aria-label`, `title`, and `focus-visible:ring-2 focus-visible:ring-secondary` classes to all icon-only action buttons in UI prototypes.
