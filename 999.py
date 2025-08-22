import asyncio
from playwright.async_api import async_playwright

async def scrape_site_text():
    async with async_playwright() as p:
        # 啟動 Chromium 瀏覽器（headless 模式）
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        # 開啟新分頁
        page = await browser.new_page()

        url = "https://xinying.tainan.gov.tw/"
        print("⏳ 正在開啟頁面:", url)

        # 前往目標網址，並設定 90 秒的超時
        await page.goto(url, timeout=90000)

        # 等待網頁載入完成 (確保 body 出現 & 網路閒置)
        await page.wait_for_selector("body", timeout=60000)
        await page.wait_for_load_state("networkidle")

        # 擷取 body 文字
        body_handle = await page.query_selector("body")
        content = await body_handle.inner_text() if body_handle else "❌ 無法擷取 body 元素"

        # 關閉瀏覽器
        await browser.close()

        return content

if __name__ == "__main__":
    # 使用 asyncio.run() 執行非同步函式
    text_content = asyncio.run(scrape_site_text())

    # 只顯示前 3000 字，避免終端機被塞爆
    print(text_content[:3000])






