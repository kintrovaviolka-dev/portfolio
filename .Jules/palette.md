## 2026-06-16 - [Interactive Flip Card Accessibility]
**Learning:** [When making custom structural interactive elements like flip cards keyboard-accessible, simply mapping ':hover' to ':focus-visible' can cause unintended transformations on focus that users can't control. Additionally, using 'Space' to activate an element requires 'event.preventDefault()' to prevent page scrolling.]
**Action:** [Use separate ':focus-visible' outline styles without triggering structural transforms, and attach an 'onkeydown' handler handling 'Enter' and 'Space' with preventDefault.]

## 2026-06-23 - [Off-Screen Menu Tab Traps and ARIA]
**Learning:** [When using CSS `transform` to move menus off-screen, they remain in the DOM and are still focusable via keyboard navigation, creating "tab traps". Additionally, toggle buttons for off-screen elements need explicit `aria-expanded` attributes that dynamically update via JavaScript to inform screen readers of the menu's state.]
**Action:** [Always combine off-screen `transform` with `visibility: hidden` (and `visibility: visible` when open) to remove hidden elements from the focus order. Update CSS `transition` to handle the delayed `visibility` change. Attach JavaScript listeners to update the `aria-expanded` attribute on the corresponding toggle button.]
