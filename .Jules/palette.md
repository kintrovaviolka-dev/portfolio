## 2026-06-16 - [Decorative Symbols & External Link Accessibility]
**Learning:** [Decorative symbols like arrows (&darr;) within interactive elements can cause screen readers to announce confusing characters. External links opening in a new tab without proper context and security attributes can cause a poor and insecure experience.]
**Action:** [Always wrap decorative symbols in `<span aria-hidden="true">`. Add `rel="noopener noreferrer"` and an `aria-label` (e.g., 'opens in a new tab') to `target="_blank"` links.]

## 2026-06-16 - [Scrollspy Navigation Accessibility]
**Learning:** [When implementing scrollspy navigation (e.g., using IntersectionObserver), visually updating the active navigation link is not enough for screen readers. The 'aria-current="page"' attribute must be dynamically managed alongside visual classes.]
**Action:** [In scrollspy logic, ensure you remove 'aria-current' from links losing active status and set 'aria-current="page"' on the link becoming active.]

## 2026-06-16 - [Interactive Flip Card Accessibility]
**Learning:** [When making custom structural interactive elements like flip cards keyboard-accessible, simply mapping ':hover' to ':focus-visible' can cause unintended transformations on focus that users can't control. Additionally, using 'Space' to activate an element requires 'event.preventDefault()' to prevent page scrolling.]
**Action:** [Use separate ':focus-visible' outline styles without triggering structural transforms, and attach an 'onkeydown' handler handling 'Enter' and 'Space' with preventDefault.]

## 2023-10-24 - Mobile Navigation Tab Trap & Aria-Expanded
**Learning:** Off-canvas menus hidden via `transform: translateY` still remain accessible to screen readers and keyboard focus unless explicitly hidden using `visibility: hidden` or `display: none`. Furthermore, the menu toggle button must dynamically update its `aria-expanded` attribute for screen readers.
**Action:** When implementing animated off-canvas elements, always combine transforms with `visibility: hidden`/`visible` and `transition` on visibility. Add `aria-expanded` logic to toggle buttons in JavaScript to reflect state accurately.

## 2026-06-16 - [Decorative Emojis & Icon Accessibility]
**Learning:** Decorative emojis (like flags) or purely visual CSS-generated icons (like `</>` or `⚕`) are announced by screen readers, leading to confusing or redundant information for users relying on assistive technologies.
**Action:** Always wrap purely decorative text emojis or icon elements with `aria-hidden="true"` to prevent screen readers from reading them out loud.

## 2026-06-16 - [Mobile Menu Escape Key Accessibility]
**Learning:** When users open a mobile navigation menu via a hamburger button, they expect to be able to close it using the `Escape` key. If they do so, focus should programmatically return to the toggle button (the hamburger button) to prevent keyboard tab traps and maintain logical focus flow.
**Action:** Add a document-level `keydown` listener that checks for the `Escape` key, closes the menu, updates `aria-expanded` on the toggle button to `false`, and calls `.focus()` on the toggle button.

## 2026-06-16 - [Brand Logo Return-to-Top Accessibility]
**Learning:** Brand logos acting as non-interactive elements in navigation bars miss an opportunity to provide a quick "return to top" function. Users often click the logo expecting it to take them to the homepage or top of the page.
**Action:** When modifying navigation, ensure brand logos act as 'return to top' anchors by wrapping them in an anchor tag pointing to the top section (e.g., `<a href="#hero">`) and include a descriptive `aria-label`.

## 2026-06-16 - [Mobile Toggle Visual Feedback]
**Learning:** Mobile toggle buttons (like hamburger menus) can leave users confused if the icon doesn't change state to indicate it can now close the menu.
**Action:** For mobile toggle buttons, dynamically update the visual text icon (e.g., from `☰` to `✕`) in JavaScript when the state changes to provide clear visual feedback.
