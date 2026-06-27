## 2026-06-16 - [Interactive Flip Card Accessibility]
**Learning:** [When making custom structural interactive elements like flip cards keyboard-accessible, simply mapping ':hover' to ':focus-visible' can cause unintended transformations on focus that users can't control. Additionally, using 'Space' to activate an element requires 'event.preventDefault()' to prevent page scrolling.]
**Action:** [Use separate ':focus-visible' outline styles without triggering structural transforms, and attach an 'onkeydown' handler handling 'Enter' and 'Space' with preventDefault.]
## 2025-10-24 - Prevent Off-Screen Tab Traps
**Learning:** When using CSS `transform` to move elements like mobile menus off-screen, they remain keyboard focusable, creating a confusing "invisible" tab trap for screen reader and keyboard users.
**Action:** Always combine off-screen `transform` states with `visibility: hidden` (and `visibility: visible` when active), and ensure toggle buttons dynamically update their `aria-expanded` state via JavaScript.
