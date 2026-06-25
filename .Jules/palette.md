# Palette's Journal
## 2024-05-24 - Accessible 'Skip to Main Content' Link for Fixed Sidebars
**Learning:** In complex layouts with fixed-position sidebars (like the 280px sidebar in AssetTrack), a standard 'Skip to Main Content' link needs explicit high z-index and fixed/absolute positioning to ensure it's not obscured when it becomes visible on focus.
**Action:** Use the Tailwind pattern `sr-only focus:not-sr-only focus:fixed focus:top-4 focus:left-4 focus:z-[100] focus:bg-secondary focus:text-white focus:px-4 focus:py-2 focus:rounded-lg focus:ring-2 focus:ring-secondary focus:ring-offset-2` and ensure the target element has `id="main-content"`, `tabindex="-1"`, and `outline-none`.
