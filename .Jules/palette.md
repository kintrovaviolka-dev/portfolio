
## 2026-06-10 - Keyboard Accessible Flip Cards
**Learning:** Custom interactive elements (like flip cards using `onclick`) are completely invisible to keyboard users unless explicitly given semantic meaning and keyboard event handlers. Hover states that trigger structural changes (like flipping) should not be mapped to `:focus`, as this removes user control.
**Action:** When creating custom interactive widgets, always add `tabindex="0"`, `role="button"`, descriptive `aria-label`s, and `onkeydown` handlers for Enter/Space. Ensure a distinct `:focus-visible` outline is provided, separate from the `:hover` state.
