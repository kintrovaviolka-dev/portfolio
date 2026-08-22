import os
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        errors = []
        page.on('pageerror', lambda err: errors.append(err))

        filepath = os.path.abspath('portfolio.html')
        file_url = f"file://{filepath}"

        print(f"Navigating to {file_url}")
        await page.goto(file_url)

        await page.wait_for_timeout(1000)

        if errors:
            print("Errors found!")
            for e in errors:
                print(e)
            exit(1)
        else:
            print("No JavaScript errors found during load.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
