## 2025-02-14 - Keyboard Navigation & Pagination Accessibility in Inventory
**Learning:** Table inventory views need explicit navigation markup (`<nav aria-label="...">`) and page indicator attributes (`aria-current="page"`) alongside skip-to-content anchors for screen reader users navigating dense data tables.
**Action:** Always wrap pagination button groups in semantic `<nav>` elements with localized `aria-label` and `aria-current="page"` on active page buttons.
