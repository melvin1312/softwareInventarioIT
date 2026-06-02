## 2025-05-14 - Semantic Buttons vs. Clickable Spans
**Learning:** The project frequently uses `<span>` with `cursor-pointer` for icon buttons (e.g., notifications, history). These are not keyboard-accessible by default and lack proper roles.
**Action:** When improving interactivity or accessibility, replace these `<span>` elements with semantic `<button>` tags and ensure they have `aria-label` and `title` attributes.
