## 2026-05-31 - Accessible Interactive Cards
**Learning:** Custom interactive elements (like hover/click "flip cards") often lack native keyboard support. They need tabindex, role, ARIA states, and keyboard event listeners (Enter/Space) to be fully accessible. Global focus states are also critical.
**Action:** When creating custom interactive widgets, always pair `onclick` with `onkeydown` (handling Enter and Space), add `tabindex="0"`, assign a semantic `role`, and ensure a global `:focus-visible` style exists.
