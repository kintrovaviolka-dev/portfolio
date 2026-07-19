## 2026-06-17 - [Flip Card Double Focus Ring]
**Learning:** When a parent interactive element (like `.flip-card`) delegates focus styling to a child element (`.flip-card-inner`), universal `*:focus-visible` rules can cause a double focus ring if the parent doesn't explicitly suppress its own outline.
**Action:** Explicitly apply `outline: none` to the parent's `:focus-visible` state (`.flip-card:focus-visible`) to prevent double focus rings when styling is delegated to a child.

## 2026-06-17 - [Prefers Reduced Motion Smooth Scroll]
**Learning:** `scroll-behavior: smooth` persists even when `animation` and `transition` are set to `none` via `prefers-reduced-motion: reduce`, which fails to fully respect the user's preference to avoid excessive motion.
**Action:** Always include `html { scroll-behavior: auto !important; }` within the `@media (prefers-reduced-motion: reduce)` media query.

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

## 2026-06-16 - [Mobile Navigation Visual Feedback & External Close Triggers]
**Learning:** Users rely on clear visual feedback for toggle states; a hamburger menu icon should change to a close icon (e.g., '✕') when open. Furthermore, interactive elements outside the primary navigation list, such as a brand logo serving as a 'return to top' anchor, should reliably trigger the menu to close, otherwise the menu overlays the top content.
**Action:** Dynamically toggle the content of mobile menu buttons (e.g., '☰' to '✕') based on the 'nav-open' state. Extract menu closing logic to a reusable function and explicitly bind it to external navigation elements like the brand logo.

## 2026-06-16 - [Interactive Flip Card aria-expanded]
**Learning:** For interactive toggle elements like flip cards, simply assigning a class like `flipped` isn't enough for screen readers; they need to know the state via `aria-expanded`.
**Action:** When creating structural elements that function as toggles (e.g., `<article class="flip-card">`), add `aria-expanded="false"` and dynamically update it to `"true"` or `"false"` in the interaction handlers.

## 2026-06-16 - [False Affordances with Custom Cursors]
**Learning:** Applying interactive hover states (like an enlarged custom cursor or a pointer) to non-interactive elements (like a wrapping div without a click handler) creates a false affordance, confusing users who expect an action to occur upon clicking.
**Action:** Carefully audit JavaScript query selectors that apply custom cursor or hover behaviors to ensure they only target genuinely clickable or interactive elements (e.g., `a`, `button`, or custom components with `onclick` handlers).

## 2023-10-25 - [Skip-to-Content Focus Ring on main tag]
**Learning:** Universal `:focus-visible` outlines applied to structural wrappers like `<main tabindex="-1">` cause a jarring, full-page focus ring when targeted by skip-to-content links.
**Action:** Always suppress the universal `:focus-visible` outline specifically on structural tags like `#main-content` by setting `outline: none` so that the skip link doesn't create a massive focus ring while still allowing programmatic focus.
