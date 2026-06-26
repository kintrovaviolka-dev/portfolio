## 2026-06-16 - [Interactive Flip Card Accessibility]
**Learning:** [When making custom structural interactive elements like flip cards keyboard-accessible, simply mapping ':hover' to ':focus-visible' can cause unintended transformations on focus that users can't control. Additionally, using 'Space' to activate an element requires 'event.preventDefault()' to prevent page scrolling.]
**Action:** [Use separate ':focus-visible' outline styles without triggering structural transforms, and attach an 'onkeydown' handler handling 'Enter' and 'Space' with preventDefault.]

## 2026-06-26 - Mobile Menu Tab Trap & ARIA State
**Learning:** When using CSS `transform` to animate mobile navigation off-screen, the links remain focusable, creating an invisible tab trap. Setting `visibility: hidden` removes them from the focus order but immediately snapping it breaks the closing animation.
**Action:** Add `visibility: hidden` alongside `transition: visibility 0.3s ease` to delay the hiding effect until the CSS transform animation completes. Also, dynamic elements like hamburger buttons must actively toggle `aria-expanded` via JavaScript to announce their state to screen readers.
