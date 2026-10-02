## 2025-10-02 - Accessible Password Toggle Pattern
**Learning:** Password visibility toggles in absolute-positioned input fields require adequate right padding (`pr-10` or `pr-12`) to prevent text overlap, along with synchronous updates to `aria-pressed`, `aria-label`, `title`, text content, and `data-icon` attributes for full screen reader and visual alignment.
**Action:** Always verify `pr-10` padding on password input wrappers and update all five ARIA/DOM state indicators simultaneously when unmasking password fields.
