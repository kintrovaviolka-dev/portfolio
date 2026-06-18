## 2026-06-16 - [Interactive Flip Card Accessibility]
**Learning:** [When making custom structural interactive elements like flip cards keyboard-accessible, simply mapping ':hover' to ':focus-visible' can cause unintended transformations on focus that users can't control. Additionally, using 'Space' to activate an element requires 'event.preventDefault()' to prevent page scrolling.]
**Action:** [Use separate ':focus-visible' outline styles without triggering structural transforms, and attach an 'onkeydown' handler handling 'Enter' and 'Space' with preventDefault.]

## 2026-06-18 - [Skip Links and Dark Theme Focus States]
**Learning:** [In dark-themed websites, default browser focus outlines are often invisible or have low contrast, especially against non-solid or textured backgrounds. Additionally, sites with fixed top navigation bars cause keyboard navigation to require excessive tabbing just to reach the main content.]
**Action:** [Always define explicit, high-contrast `:focus-visible` styles rather than relying on browser defaults. Also, provide a "Skip to main content" link for keyboard users to bypass fixed navigation headers.]
