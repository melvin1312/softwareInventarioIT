# Palette's Journal - Critical UX Learnings
## 2026-06-20 - Standardized Accessibility Patterns for Data Tables
**Learning:** Icon-only action buttons in dense data tables often lack descriptive labels and visible focus indicators, making them inaccessible to screen reader and keyboard users. Using Spanish labels in a predominantly Spanish UI maintains consistency.
**Action:** Apply `aria-label`, `title`, and `focus-visible:ring-2` patterns to all icon-only buttons (`more_vert`, pagination, view toggles) to ensure WCAG compliance and improved UX.
