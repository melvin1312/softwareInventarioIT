## 2024-05-24 - Standardizing Form Accessibility and Focus States

**Learning:** Form fields in the AssetTrack prototypes often lack programmatic association between labels and inputs, and inconsistent focus styling can hinder keyboard navigation.

**Action:** Always ensure `<label>` elements have a `for` attribute matching the `id` of their target input/select. Use the standardized focus pattern `focus-visible:ring-2 focus-visible:ring-secondary focus-visible:ring-offset-2 focus-visible:outline-none` for consistent and accessible keyboard indicators.
