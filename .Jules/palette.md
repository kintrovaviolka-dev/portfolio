## 2026-06-16 - [Interactive Flip Card Accessibility]
**Learning:** [When making custom structural interactive elements like flip cards keyboard-accessible, simply mapping ':hover' to ':focus-visible' can cause unintended transformations on focus that users can't control. Additionally, using 'Space' to activate an element requires 'event.preventDefault()' to prevent page scrolling.]
**Action:** [Use separate ':focus-visible' outline styles without triggering structural transforms, and attach an 'onkeydown' handler handling 'Enter' and 'Space' with preventDefault.]

## 2026-06-17 - [Skip Link Positioning]
**Learning:** [A "Skip to main content" link must be visually hidden by default but positioned absolutely so it doesn't affect the layout, and then positioned on screen (e.g., `top: 0`) and given an outline when focused to ensure visibility for keyboard users. The `<main>` element needs an `id` matching the skip link's `href` to function correctly.]
**Action:** [Always include skip links on pages with extensive navigation, use absolute positioning to hide them off-screen, and ensure the target main content area has a matching ID.]
