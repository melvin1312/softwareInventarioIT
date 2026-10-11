## 2025-02-14 - Interactive Password Toggle with Accessibility Attributes
**Learning:** Icon-only password visibility buttons require `aria-label`, `aria-pressed`, and `title` attributes synchronized with JS state changes (`password` vs `text`), and input fields with trailing absolute toggle buttons require `pr-10` padding to avoid overlapping text.
**Action:** Always provide explicit padding-right (`pr-10`/`pr-12`) on inputs with embedded action icons and sync `aria-pressed` and `aria-label` when dynamically toggling visibility.
