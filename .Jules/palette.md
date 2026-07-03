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

## 2025-05-18 - Decorative Icons and Emojis Accessibility
**Learning:** While decorative text symbols (like HTML entities) are often properly hidden from screen readers, developers sometimes forget that CSS-generated icons (`::before`/`::after` content) and emojis are also announced by screen readers, which can add confusing noise (e.g., "Less than slash greater than" or "Flag of Czechia").
**Action:** Always explicitly add `aria-hidden="true"` to purely decorative icons (like `<i class="icon-*">`) and emojis to prevent redundant or confusing screen reader announcements.
