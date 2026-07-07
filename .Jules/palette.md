# Palette's Journal - Critical UX Learnings

## 2025-05-15 - Standardized Accessibility Foundations for AssetTrack
**Learning:** The initial prototypes lack basic accessibility foundations such as skip-to-content links, descriptive labels for icon-only buttons, and visible focus indicators. In a data-heavy application like AssetTrack, these are critical for professional usability.
**Action:** Always implement the 'Skip to Main Content' link as the first child of `<body>` and ensure `<main>` has `id="main-content"` and `tabindex="-1"`. Apply standardized Spanish ARIA labels ('Notificaciones', 'Historial de actividad', 'Más acciones') and `focus-visible:ring-2` to all interactive elements.
