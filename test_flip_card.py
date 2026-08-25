import os
import re
from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{os.path.abspath('portfolio.html')}")

        # Get the first flip card
        flip_card = page.locator('.flip-card').first
        front = flip_card.locator('.flip-card-front')
        back = flip_card.locator('.flip-card-back')

        # Check initial state
        expect(front).to_have_attribute("aria-hidden", "false")
        expect(back).to_have_attribute("aria-hidden", "true")

        # Click to flip
        flip_card.click()

        # Check flipped state
        expect(front).to_have_attribute("aria-hidden", "true")
        expect(back).to_have_attribute("aria-hidden", "false")

        # Click to flip back
        flip_card.click()

        # Check original state
        expect(front).to_have_attribute("aria-hidden", "false")
        expect(back).to_have_attribute("aria-hidden", "true")

        print("Playwright test passed!")
        browser.close()

if __name__ == '__main__':
    run()
