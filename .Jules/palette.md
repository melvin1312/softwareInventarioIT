# Palette Journal - Critical UX & Accessibility Learnings

## 2024-10-18 - Keyboard Navigation & Password Unmasking ARIA Patterns
**Learning:** For login interfaces, password toggle buttons must communicate unmasking state through synchronized `aria-pressed`, dynamic `aria-label`, and `title` attributes while updating `textContent` and `data-icon`. Skip-to-content links require `tabindex="-1"` on the target `<main>` container for keyboard focus management without ring outline artifacts.
**Action:** Always include skip-to-content links as the first `<body>` child and pair password visibility toggles with synchronized ARIA attributes and `pr-10` padding on inputs.
