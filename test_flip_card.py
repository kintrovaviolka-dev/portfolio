import os
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Determine the absolute path to the local file
        filepath = os.path.abspath('portfolio.html')
        file_url = f"file://{filepath}"

        print(f"Navigating to {file_url}")
        await page.goto(file_url)

        # Tab to the first flip card
        await page.keyboard.press("Tab") # Skip to main content link
        await page.keyboard.press("Tab") # Return to top logo
        await page.keyboard.press("Tab") # Hamburger menu
        await page.keyboard.press("Tab") # About link
        await page.keyboard.press("Tab") # Skills link
        await page.keyboard.press("Tab") # Projects link
        await page.keyboard.press("Tab") # Experience link
        await page.keyboard.press("Tab") # Contact link

        # Wait a bit to ensure animations finish if any
        await page.wait_for_timeout(500)

        # Focus the first flip card directly just to be sure it's focused
        flip_card = page.locator('.flip-card').first
        await flip_card.focus()

        # Verify initial states
        front = flip_card.locator('.flip-card-front')
        back = flip_card.locator('.flip-card-back')

        print(f"Initial front aria-hidden: {await front.get_attribute('aria-hidden')}")
        print(f"Initial back aria-hidden: {await back.get_attribute('aria-hidden')}")

        assert await front.get_attribute('aria-hidden') == 'false'
        assert await back.get_attribute('aria-hidden') == 'true'

        # Flip the card by pressing Space
        print("Pressing Space to flip the card...")
        await page.keyboard.press("Space")

        # Wait a moment for JavaScript and transitions
        await page.wait_for_timeout(500)

        # Verify flipped states
        print(f"Flipped front aria-hidden: {await front.get_attribute('aria-hidden')}")
        print(f"Flipped back aria-hidden: {await back.get_attribute('aria-hidden')}")

        assert await front.get_attribute('aria-hidden') == 'true'
        assert await back.get_attribute('aria-hidden') == 'false'

        print("Flip card accessibility verified successfully!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
