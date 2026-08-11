# Palette's UX Journal

## 2026-03-06 - Preventing Input Overlay Overlaps and Supporting Standard Keyboard Skip Links
**Learning:** In highly structured corporate platforms like AssetTrack, static base prototypes often omit vital accessibility baselines such as skip-to-content links and focus outline states, and overlook overlapping of absolute positioned interactive overlays (such as password toggles) with input text.
**Action:** Always add standard keyboard skip-to-content links, configure target focus containers properly, and enforce a minimum of `pr-12` padding on input fields containing overlay buttons to preserve visual clarity.
