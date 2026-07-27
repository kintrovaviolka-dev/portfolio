from playwright.sync_api import sync_playwright
import time

def run_cuj(page):
    page.goto("http://localhost:8080/portfolio.html")
    page.wait_for_timeout(1000)

    # Scroll to the contact section
    contact_section = page.locator("#contact")
    contact_section.scroll_into_view_if_needed()
    page.wait_for_timeout(1000)

    # Find the copy buttons
    copy_buttons = page.locator(".copy-btn")

    # Click the first copy button (Email)
    copy_buttons.nth(0).click()
    page.wait_for_timeout(500)

    # Take screenshot of the "copied" state
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1500) # Wait for state to revert

    # Click the second copy button (Phone)
    copy_buttons.nth(1).click()
    page.wait_for_timeout(500)

    # Hold final state for the video
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        # Important: grant clipboard permissions
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos",
            permissions=['clipboard-read', 'clipboard-write']
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
