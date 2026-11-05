# Palette's Journal - Critical Learnings

## 2025-05-18 - Password Visibility Toggle & Skip Link Accessibility Pattern
**Learning:** In corporate authentication prototypes with trailing icon overlays, input text can bleed into the button without sufficient right padding (`pr-11` or `pr-12`). Additionally, password toggles need synchronization of `aria-pressed`, localized `aria-label`/`title`, `textContent`, and `data-icon` for complete screen reader and UI fidelity. Skip links require `tabindex="-1"` and `outline-none` on `<main>` to enable programmatic focus without jarring default outline styles.
**Action:** When implementing password unmasking in static prototypes, always use vanilla JS with dynamic ARIA labels/pressed attributes, update `data-icon` alongside `textContent`, and pair with an accessible skip-to-content target.
