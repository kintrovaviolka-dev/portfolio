## 2026-06-16 - [Interactive Flip Card Accessibility]
**Learning:** [When making custom structural interactive elements like flip cards keyboard-accessible, simply mapping ':hover' to ':focus-visible' can cause unintended transformations on focus that users can't control. Additionally, using 'Space' to activate an element requires 'event.preventDefault()' to prevent page scrolling.]
**Action:** [Use separate ':focus-visible' outline styles without triggering structural transforms, and attach an 'onkeydown' handler handling 'Enter' and 'Space' with preventDefault.]

## 2026-06-24 - Accessible Mobile Menus
**Learning:** Combining `transform: translateY()` with `visibility: hidden` and `aria-expanded` attributes is necessary for accessible off-screen mobile menus, as purely using `transform` creates a tab trap.
**Action:** Always ensure that when menus are moved off-screen using `transform`, they are also set to `visibility: hidden` (and `visible` when open), and that toggle buttons dynamically update their `aria-expanded` state using JavaScript.
