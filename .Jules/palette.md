## 2026-07-29 - [Prefers Reduced Motion Animated Custom Cursors]
**Learning:** Animated custom cursors powered by `requestAnimationFrame` and CSS transitions violate the `prefers-reduced-motion` intent if left active. Simply overriding `transition: none` is insufficient because the JavaScript animation loop continues running and applying inline styles, causing a jarring, stuttering cursor experience.
**Action:** When `prefers-reduced-motion: reduce` is active, completely hide custom cursor elements (`display: none !important`), restore default cursors on interactive elements (`cursor: auto/pointer !important`), and conditionally prevent the JavaScript animation loop from initializing.

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

## 2026-06-18 - [Mobile Navigation Outside Click Trap]
**Learning:** For mobile off-canvas navigation menus, users intuitively expect to be able to close the menu by tapping anywhere outside of it. Without a document-level click listener, users can feel trapped if they don't explicitly tap the close button or a navigation link.
**Action:** Implement a document-level `click` event listener to close the menu when a user clicks outside the menu container and not on the toggle button (`!navLinks.contains(e.target) && !hamburger.contains(e.target)`).

## 2026-06-18 - [Mobile Navigation Focusout Close]
**Learning:** For mobile off-canvas navigation menus, when a keyboard user tabs completely out of an open dropdown mobile menu, the menu should close to prevent obscuring the main content they are now focusing on.
**Action:** Add a `focusout` event listener on the `nav` container. If `!nav.contains(e.relatedTarget)` and the menu is open, close the menu automatically.
## 2026-07-27 - [Inline JavaScript & Screen Reader Announcements]\n**Learning:** Avoid embedding complex JavaScript logic (e.g., Promises, DOM manipulation, `setTimeout`) directly into inline `onclick` HTML attributes. Extract this logic into dedicated, reusable functions within `<script>` blocks to maintain readability and avoid anti-patterns.\n**Action:** When adding interactive behaviors, create a reusable function in a `<script>` block and bind it to the element's event handler. Always update an `aria-live="polite"` region to announce dynamic state changes (like 'Copied to clipboard') to screen readers.\n\n## 2026-07-27 - [Timeout Race Conditions]\n**Learning:** When using `setTimeout` to revert a visual success state on a button (like a 'Copied' indicator), rapid successive clicks create multiple overlapping timers, causing the visual state to revert prematurely.\n**Action:** Always track and clear existing timeouts (e.g., via `clearTimeout` and `dataset.timeoutId`) to prevent race conditions when implementing timed visual state resets.

## 2026-07-28 - [Dynamic Native Tooltips for Icon Buttons]
**Learning:** For icon-only action buttons (like "Copy to Clipboard"), providing a static `title` attribute isn't enough when the action has a dynamic success state. Users benefit from the native tooltip updating (e.g., to "Copied!") alongside visual feedback, providing explicit confirmation.
**Action:** When implementing icon-only buttons with visual success states, always add a descriptive `title` attribute. Dynamically update this `title` attribute to reflect the success state (e.g., "Copied!") and ensure it reverts to its original value when the visual state resets.

## 2026-07-29 - [Global Screen Reader Announcer]
**Learning:** Having multiple localized `aria-live` regions or updating states without feedback can leave screen reader users unaware of dynamic changes, like interactive cards flipping.
**Action:** Implement a single global `aria-live="polite"` region (e.g., `#sr-announcer` at the top of `<body>`) and use a centralized JavaScript function with a short timeout (to force reflow) to broadcast dynamic state changes reliably to assistive technologies.

## 2026-07-30 - [Custom Cursors and Touch Devices]
**Learning:** Custom JS mouse cursors and hover-based interactive effects (like magnetic tilt) can get permanently stuck on touch devices (where users tap instead of move a mouse). Relying solely on `@media (max-width: 768px)` or `window.innerWidth <= 768` fails to account for larger touch devices like iPads or touchscreen laptops, resulting in a confusing and frustrating UX where the cursor remains frozen where the user last tapped.
**Action:** When implementing custom cursors or hover-based interactions, always explicitly disable them for touch devices by checking for pointer type. In CSS, use `@media (pointer: coarse)` to hide custom cursor elements and restore native interactions. In JavaScript, use `window.matchMedia('(pointer: coarse)').matches` to conditionally disable hover-specific event listeners and logic.

## 2026-08-04 - [Section Landmarks and Accessible Names]
**Learning:** For screen readers to correctly recognize and allow navigation by regions (sections of the page), `<section>` tags must have an explicitly defined accessible name. Without it, the semantic value of the `<section>` tag is often ignored by assistive technologies.
**Action:** Always provide an accessible name to `<section>` tags by either referencing their visible heading with `aria-labelledby="heading-id"` or providing an explicit `aria-label="Section Name"`.

## 2026-08-05 - [Visual and Screen Reader Feedback for Async Clipboard Failures]
**Learning:** When using the asynchronous `navigator.clipboard` API, failures can occur silently if permissions are denied or if the API is unsupported. Without explicit error handling that updates the visual state (like changing the icon and tooltip) and announces the failure to screen readers via an `aria-live` region, users are left wondering if the action succeeded.
**Action:** Always implement a `.catch()` block or fallback for clipboard operations. In the failure handler, provide clear visual error state (e.g., a red '✗' and an updated `title` attribute for native tooltips), announce the failure via a global `aria-live` region, and ensure the state resets gracefully just like the success state.

## 2026-08-10 - [Interaction Hints for Custom Hover-Based Components]
**Learning:** For custom interactive components that rely on `:hover` for mouse users (e.g., flip cards), users may not immediately know they can interact with them. Providing explicit interaction hints helps guide users.
**Action:** Use native HTML attributes like `title="Press Space or click to flip"` as a fallback mechanism for tooltips to ensure discoverability without breaking layout constraints.

## 2026-08-15 - [Dynamic Accessible Names for Toggle Buttons]
**Learning:** For toggle buttons (e.g., mobile hamburger menus), using generic labels like "Toggle menu" is less informative than dynamic labels that explicitly state the action available based on the current state.
**Action:** Dynamically update the `aria-label` and `title` attributes on toggle buttons via JavaScript to accurately reflect the available action (e.g., 'Open menu' vs 'Close menu') rather than relying on static, generic labels.

## 2026-08-20 - [Explicitly Surface Custom Keyboard Shortcuts]
**Learning:** For custom keyboard shortcuts implemented via JavaScript (like 'Escape' to close a menu), simply adding the keydown event listener is insufficient for accessibility and discoverability. Users relying on assistive technologies or those who hover for hints need to be explicitly informed of the shortcut.
**Action:** When implementing custom keyboard shortcuts, explicitly surface them by adding the `aria-keyshortcuts` attribute (only when the action is available) and appending the shortcut hint (e.g., '(Escape)') to visual tooltips (`title` and `aria-label`).

## 2026-08-25 - [Interactive Flip Card Backface Accessibility]
**Learning:** For 3D flip cards, CSS `backface-visibility: hidden` hides the back face visually but does not hide it from screen readers. This causes screen readers to read the back content even when it is visually hidden.
**Action:** Explicitly set `aria-hidden="false"` on the front face and `aria-hidden="true"` on the back face initially, and dynamically toggle these attributes in JavaScript when the card flips to maintain accurate state for assistive technologies.
