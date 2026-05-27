## 2026-05-27 - Standardizing Skip-to-Content Links
**Learning:** In fixed-layout dashboards with sidebars and headers (z-indexed), skip links need explicit high z-index and fixed positioning to ensure they are visible over other elements when focused. Using `focus:not-sr-only` alone is insufficient as it resets positioning to static.
**Action:** Always apply `focus:fixed focus:top-4 focus:left-4 focus:z-[100]` and ensure the target `<main>` has `tabindex="-1"` for reliable focus management.
