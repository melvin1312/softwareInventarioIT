## 2025-05-14 - Accessible Password Visibility Toggle
**Learning:** Functional micro-interactions like password visibility toggles must update `aria-label` and `title` attributes dynamically alongside the visual state (icon/input type) to maintain screen reader accuracy and provide helpful tooltips.
**Action:** Always include dynamic ARIA attribute updates in toggle interactions (e.g., switching between 'Mostrar' and 'Ocultar' labels).

## 2025-05-14 - Verifying Password Visibility in Screenshots
**Learning:** When using Playwright to verify password visibility toggles, the input field must be explicitly filled with unique text. Static placeholders like '••••••••' can look identical to masked passwords in screenshots, making it impossible to visually confirm the unmasking without actual text.
**Action:** Use `.fill()` with recognizable text before taking screenshots of unmasked password states.
