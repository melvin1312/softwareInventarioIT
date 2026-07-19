# Palette's Journal - Critical UX/Accessibility Learnings

## 2024-07-19 - Standardized Password Visibility Toggle for Tailwind Static Prototypes
**Learning:** In static HTML prototypes styled with Tailwind, password inputs with absolutely positioned visibility toggles require careful spacing; using default narrow right padding (e.g., `pr-3`) causes typed passwords to visually overlap with the toggle icon. Standardizing right padding to `pr-12` is critical. Furthermore, when using Material Symbols icons as ligatures (e.g., `visibility`), updating both the element's `textContent` and the custom `data-icon` attribute is necessary to ensure consistent state and support accessibility utilities.
**Action:** When implementing password toggle components in this design system, always pair a `pr-12` input padding with an absolute toggle button, and explicitly update both the `textContent` and `data-icon` attributes to either `visibility` or `visibility_off` in the JavaScript handler.
