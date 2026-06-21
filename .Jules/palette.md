## 2026-06-16 - [Interactive Flip Card Accessibility]
**Learning:** [When making custom structural interactive elements like flip cards keyboard-accessible, simply mapping ':hover' to ':focus-visible' can cause unintended transformations on focus that users can't control. Additionally, using 'Space' to activate an element requires 'event.preventDefault()' to prevent page scrolling.]
**Action:** [Use separate ':focus-visible' outline styles without triggering structural transforms, and attach an 'onkeydown' handler handling 'Enter' and 'Space' with preventDefault.]
## 2026-06-21 - Fix Mobile Menu Off-screen Tab Trap
**Learning:** When using CSS transform to move menus off-screen, always combine it with visibility: hidden (and visibility: visible when open) to prevent off-screen tab traps. Additionally, ensure toggle buttons dynamically update their aria-expanded attribute using JavaScript.
**Action:** Add visibility properties to off-screen mobile menus and dynamically toggle aria-expanded attributes on hamburger menus for all future mobile navigation implementations.
