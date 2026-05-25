## 2026-05-25 - Essential Skip Links for Fixed Sidebar Layouts
**Learning:** In applications with fixed sidebars or complex headers, keyboard users must tab through numerous navigation items before reaching the main content. This creates a significant barrier to efficient navigation.
**Action:** Always implement a "Skip to Main Content" link ('Saltar al contenido principal') as the very first focusable element in the `<body>`. Ensure it targets a `<main>` element with `id="main-content"` and `tabindex="-1"` to guarantee focus management across all browsers.
