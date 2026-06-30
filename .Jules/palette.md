# Palette Journal - UX & Accessibility Learnings

## 2025-05-14 - Skip Links in Fixed Layouts
**Learning:** In layouts with fixed sidebars (z-50) and fixed headers (z-40), 'Skip to Main Content' links must have a very high z-index (e.g., z-[100]) and explicit positioning (top/left) to ensure they are visible when focused and not hidden behind other fixed elements.
**Action:** Always include `focus:z-[100] focus:fixed focus:top-4 focus:left-4` when implementing skip links in the AssetTrack project.

## 2025-05-14 - Standardized Icon Button A11y
**Learning:** Icon-only buttons in the AssetTrack dashboard (notifications, history, more_vert) were missing both ARIA labels and titles, making them inaccessible to screen readers and providing no hover feedback for sighted users.
**Action:** Standardize use of `aria-label` and `title` with Spanish labels (e.g., 'Notificaciones', 'Más acciones') and apply the `focus-visible` ring pattern.
