## 2025-05-14 - Tailwind Skip-Link Positioning
**Learning:** When using the Tailwind class `not-sr-only` to reveal a "Skip to Main Content" link on focus, it resets the element's CSS `position` to `static`. This can cause the link to appear at the start of the document flow instead of being overlaid on top of the UI.
**Action:** Always explicitly re-declare the desired positioning using focus variants (e.g., `focus:fixed` or `focus:absolute`) alongside `focus:not-sr-only` to ensure the skip link remains correctly positioned when visible.
