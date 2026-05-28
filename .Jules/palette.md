## 2026-05-28 - Keyboard Accessibility for Interactive Structural Elements
**Learning:** When using non-standard interactive structural elements like `<article>` instead of `<button>` for interactions like flip cards, they require explicit `role="button"`, `tabindex="0"`, and keydown event listeners (specifically for 'Enter' and 'Space') to be fully accessible to keyboard and screen reader users.
**Action:** Always ensure custom interactive components built with semantic HTML containers include proper ARIA roles, tabindex, and keyboard event handlers in future UI components.
