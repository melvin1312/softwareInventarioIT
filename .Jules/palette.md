## 2025-01-24 - Accessible Skip Links in Dashboards
**Learning:** Dashboard layouts with persistent sidebars significantly increase the tab-stop count before reaching main content, hindering keyboard users. Standard skip links must be explicitly positioned (fixed/absolute) and given high z-index to appear correctly over fixed sidebars.
**Action:** Always implement 'Skip to Main Content' links as the first child of <body> in dashboards, using `sr-only focus:not-sr-only focus:fixed focus:z-[100]` with standardized styling.
