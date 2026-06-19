## 2025-05-14 - Skip-to-content links for accessibility
**Learning:** Skip-to-content links are a critical micro-UX for accessibility, especially in apps with complex sidebars. They must be the first child of <body> to be effective for keyboard users.
**Action:** Use the pattern `sr-only focus:not-sr-only focus:fixed focus:top-4 focus:left-4 focus:z-[100] focus:bg-secondary focus:text-white focus:px-4 focus:py-2 focus:rounded-lg focus:ring-2 focus:ring-secondary focus:ring-offset-2` for skip links.
