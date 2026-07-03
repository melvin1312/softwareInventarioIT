# Palette's Journal - Critical UX Learnings

## 2025-05-14 - Standardized Accessibility Foundations
**Learning:** The base prototypes often lack essential accessibility features like skip-to-content links and descriptive labels for icon-only buttons. Using a consistent Tailwind-based skip-link pattern and standardized Spanish labels improves the overall maturity of the interface.
**Action:** Always implement 'Saltar al contenido principal' as the first child of `<body>` and ensure `<main>` has `id="main-content"`, `tabindex="-1"`, and `outline-none`. Apply `focus-visible:ring-2 focus-visible:ring-secondary focus-visible:ring-offset-2 focus-visible:outline-none rounded` to all interactive elements for clear keyboard feedback.
