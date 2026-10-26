## 2026-03-29 - Password Visibility & Skip-Link Keyboard Accessibility
**Learning:** In login forms with eye toggles, adding interactive password unmasking without updating ARIA attributes (`aria-pressed`, `aria-label`, `title`) and icon representations (`data-icon`) leaves screen readers out of sync. Additionally, ensuring inputs have right padding (`pr-10`) avoids text overlapping with absolute position buttons.
**Action:** Always synchronize `aria-pressed`, localized `aria-label`, `title`, element text content, and `data-icon` attributes together when building visibility toggles.
