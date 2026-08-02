# Palette UX Journal - Critical Learnings Only

## 2026-04-21 - Avoiding Playwright Locator Conflicts in Nested Labeled Structures
**Learning:** When using accessible forms where helper buttons (like a password visibility toggle) are nested or structurally close to a labeled input field, searching via `get_by_label` can cause a Playwright strict-mode locator conflict. This happens because the aria-label of the button and the label of the input field are both associated with the input's context or contain overlapping terms (e.g., "Contraseña").
**Action:** Use specific ID selectors (`#password` or `#toggle-password`) or exact-match parameters (`exact=True`) in automated Playwright verification scripts to target the desired element uniquely without losing accessible HTML markup patterns.
