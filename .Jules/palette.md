## 2025-05-18 - Synchronized Password Toggle State & Input Padding
**Learning:** When adding absolute-positioned password toggles inside input wrappers in static Tailwind prototypes, input right-padding must be increased (`pr-10` or `pr-12`) to avoid visual text collision. Furthermore, screen reader accessibility requires synchronizing `aria-pressed`, `aria-label`, `title`, textContent, and `data-icon` upon state transition.
**Action:** Always set `pr-10`+ on password inputs with toggles and update all 5 state attributes in the click event listener.
