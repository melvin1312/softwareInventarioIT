## 2026-05-29 - Skip-to-content accessibility improvement
**Learning:** In dashboards with fixed sidebars (z-50) and fixed headers, 'Skip to Main Content' links must have a higher z-index (e.g., z-[100]) and explicit absolute or fixed positioning to be visible when focused.
**Action:** Use `sr-only focus:not-sr-only focus:fixed focus:top-4 focus:left-4 focus:z-[100]` for skip links in similar layout patterns.
