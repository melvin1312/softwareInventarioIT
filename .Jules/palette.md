# Palette's Journal - Critical UX/Accessibility Learnings

## 2025-05-14 - Standardizing High-Contrast Focus States and Functional Toggles
**Learning:** Functional micro-interactions like password visibility toggles must update `aria-label` and `title` attributes dynamically to reflect the current state (e.g., switching between 'Mostrar contraseña' and 'Ocultar contraseña') to maintain screen reader accuracy. Additionally, replacing low-contrast focus rings with high-contrast `focus-visible` patterns (`ring-2`, `ring-offset-2`) significantly improves keyboard navigability without affecting mouse users.
**Action:** Always pair visual state changes (like icons) with ARIA label updates. Use `focus-visible:ring-2 focus-visible:ring-secondary focus-visible:ring-offset-2` as the standard focus pattern for the AssetTrack project.
