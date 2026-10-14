# Palette's Journal - Critical UX & Accessibility Learnings

## 2024-05-20 - Password Toggle ARIA Synchronization & Skip Links in Tailwind Prototypes
**Learning:** In Tailwind CSS login forms, password visibility toggles need `aria-pressed`, localized `aria-label`/`title`, `data-icon` attribute updates alongside `textContent`, and input `pr-10` padding to prevent text overlap with absolute overlay buttons. Main containers require `id="main-content"`, `tabindex="-1"`, and `outline-none` when paired with visually hidden skip-to-content links.
**Action:** Always synchronize `aria-pressed`, `aria-label`, `title`, icon ligatures, and `data-icon` attributes on password toggle buttons, and ensure proper skip link focus management on `<main>`.
