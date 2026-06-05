## 2026-06-05 - ARIA Labels on Rich Content Elements
**Learning:** Applying `aria-label` to an interactive container (like an `<article role="button">`) completely overrides the internal text content for screen reader users, preventing them from accessing the rich content (like lists) inside the element.
**Action:** Remove `aria-label` from elements containing rich text content that serves as the label or description itself. Alternatively, use a visually hidden `<button>` inside the card for toggling state if a dedicated label is needed without hiding the content.
