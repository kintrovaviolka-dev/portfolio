## 2026-06-16 - [Interactive Flip Card Accessibility]
**Learning:** [When making custom structural interactive elements like flip cards keyboard-accessible, simply mapping ':hover' to ':focus-visible' can cause unintended transformations on focus that users can't control. Additionally, using 'Space' to activate an element requires 'event.preventDefault()' to prevent page scrolling.]
**Action:** [Use separate ':focus-visible' outline styles without triggering structural transforms, and attach an 'onkeydown' handler handling 'Enter' and 'Space' with preventDefault.]

## 2026-06-16 - [Mobile Nav Hidden Tab Trap]
**Learning:** [Using CSS `transform: translateY()` to move a menu off-screen hides it visually, but leaves interactive links accessible via keyboard tab navigation, causing a confusing invisible tab trap. Additionally, mobile toggles often lack a dynamic `aria-expanded` state.]
**Action:** [Use `visibility: hidden;` alongside `transform` on off-screen menus to hide them from screen readers and keyboards, and toggle `visibility: visible;` when opened. Always pair toggle menus with an `aria-expanded` attribute that updates dynamically in JavaScript.]
