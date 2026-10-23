## 2023-10-23 - Accessible Pagination & Skip Navigation Pattern
**Learning:** Table/inventory pages with top bars benefit immensely from structured `<nav aria-label="Paginación">` wrapper and `aria-current="page"` markers, allowing screen reader users to understand pagination context without reading through tabular data first.
**Action:** Always wrap pagination page controls in semantic `<nav>` elements with localized `aria-label` and `aria-current="page"` attributes.
