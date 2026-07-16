
## 2026-07-16 - Static HTML Testing Strategy
**Learning:** This repository contains static HTML prototypes without a Node.js environment or `package.json`. Standard frontend testing tools (like `npx playwright test`) are not available.
**Action:** Use Python Playwright scripts (`playwright.sync_api`) to verify accessibility and interactions for static files, using the `file://` protocol with absolute paths for navigation.
