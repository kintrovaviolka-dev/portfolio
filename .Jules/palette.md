## 2026-05-27 - Custom Interactive Component Accessibility
**Learning:** When building custom interactive components like flip cards with CSS, developers often rely solely on CSS pseudo-classes (`:hover`) and inline `onclick` events, ignoring keyboard users. This prevents those users from ever accessing the flipped content.
**Action:** Always ensure that custom interactive components use `tabindex="0"` and `role="button"` (if they behave as toggles), set appropriate `aria-expanded` attributes, and bind explicit `keydown` listeners (for 'Enter' and 'Space') to mirror pointer interactions.
