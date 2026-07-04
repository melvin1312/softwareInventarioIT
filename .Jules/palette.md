
## 2024-07-04 - Accessibility Foundations in Dashboards
**Learning:** Legacy prototypes often lack basic accessibility entry points like skip links and explicit ARIA labels for icon-only action buttons. Using standardized Tailwind focus rings (ring-2 ring-secondary) provides a consistent visual cue for keyboard users without clashing with the Corporate Modernist aesthetic.
**Action:** Always insert a skip link as the first child of <body> and ensure the <main> element has a matching ID and tabindex="-1" to support it.
