## 2026-06-04 - Standardized Skip-to-Content Implementation
**Learning:** Accessibility in complex IT dashboards with fixed sidebars requires a "Skip to Main Content" link that is explicitly positioned to bypass high-z-index sidebars and headers. Standard `sr-only` links need `focus:fixed` and high z-index to be visible.
**Action:** Always implement skip links as the first child of `<body>` and ensure the target `<main>` has both `id="main-content"` and `tabindex="-1"`.
