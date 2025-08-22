from playwright.sync_api import sync_playwright

def fetch_yahoo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless 爬取
        page = browser.new_page()
        page.goto("https://tw.yahoo.com/", timeout=60000)
        content = page.content()  # 抓取完整 HTML
        browser.close()
        return content

if __name__ == "__main__":
    html = fetch_yahoo()
    print(html)   # ✅ 在 Leapcell 的 Task Log / Output 會顯示
