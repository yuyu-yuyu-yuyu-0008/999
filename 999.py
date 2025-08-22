import nest_asyncio
import asyncio
from playwright.async_api import async_playwright

nest_asyncio.apply()  # 解決 asyncio.run() 在已存在事件循環報錯

async def scrape_site_text():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        url = "https://xinying.tainan.gov.tw/"
        print("⏳ 正在開啟頁面...")
        await page.goto(url, timeout=90000)

        await page.wait_for_selector("body", timeout=60000)
        body_handle = await page.query_selector("body")
        return await body_handle.inner_text() if body_handle else "❌ 無法擷取 body 元素"

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    text_content = loop.run_until_complete(scrape_site_text())
    print(text_content[:3000])  # 只顯示前 3000 字




