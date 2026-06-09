## 2026-06-09 - Keyboard Accessible Flip Cards
**Learning:** Custom interactive elements (like `article` used as a flip card) require manual keyboard accessibility mapping, including `tabindex`, `role`, `aria-label`, and handling both `Enter` and `Space` keys (with `event.preventDefault()` to stop scrolling) to provide the same experience as mouse clicks.
**Action:** When creating non-standard interactive UI elements, always ensure corresponding keyboard events (`onkeydown`) and visual focus states (`:focus-visible`) are added to maintain accessibility.
