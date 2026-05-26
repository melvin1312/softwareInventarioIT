## 2024-05-26 - Accessible 'Skip to Main Content' Links
**Learning:** For IT management systems with fixed sidebars (z-50), 'Skip to Main Content' links must use explicit positioning (focus:fixed focus:top-4 focus:left-4) and high z-index (focus:z-[100]) to be visible on focus. Target elements like <main> need id="main-content" and tabindex="-1" for reliable cross-browser navigation.
**Action:** Always verify skip-link visibility over fixed headers/sidebars and ensure the target is focusable.
