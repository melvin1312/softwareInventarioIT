# Palette's Journal - IT Assets Management

## 2026-03-06 - Input Padding Conflicts with Trailing Absolute Overlays
**Learning:** When designing standard input fields that feature absolute-positioned interactive elements on their trailing edge (such as password visibility eye toggles, copy-to-clipboard badges, or clear buttons), a default horizontal padding of `pr-3` is insufficient. When a user inputs a long value (such as a secure password or a complex email address), the characters expand into the absolute element, leading to a visual overlap bug that degrades readability and clickable space.
**Action:** Always enforce a right-hand padding of at least `pr-12` on inputs with trailing overlays to preserve clean text truncation and maintain target touch-zone boundaries.

## 2026-03-06 - Dual-Layer Icon Synchronization for Material Design Ligatures
**Learning:** In design systems utilizing Google Material Symbols via text ligatures (e.g. `textContent = 'visibility_off'`), dynamic iconography changes can lead to desynchronization between visual states and metadata states. Setting the `textContent` of the icon is sufficient for the rendering engine, but assistive technologies or automated test engines searching for visual elements through custom data attributes (like `data-icon`) will fail if the attributes do not mirror the visual state.
**Action:** When dynamically toggling ligature-based icons in JavaScript, simultaneously update both the `textContent` of the icon element and any custom data or state attributes (e.g. `data-icon` and `aria-pressed`) to guarantee consistency across visual rendering, metadata queries, and screen-readers.
