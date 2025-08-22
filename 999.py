from fastapi import FastAPI
from playwright.sync_api import sync_playwright
import requests
import traceback

app = FastAPI()

@app.get("/kaithhealthcheck")
@app.get("/kaithheathcheck")
def healthcheck():
    return {"status": "ok"}

@app.get("/fetch")
def fetch_site():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
              headless=True,
              args=[
                  "--no-sandbox",
                  "--disable-dev-shm-usage",
                  "--disable-setuid-sandbox"
                ]
            )
            # 建立新的瀏覽器 Context
            context = browser.new_context()
            
            # 再從 Context 開新頁面
            page = context.new_page()
            
            # 造訪網頁
            page.goto("https://xinying.tainan.gov.tw/", timeout=500000)
            
            # 等待 body 元素
            page.wait_for_selector("body", timeout=300000)
            
            # 取得 body 文字
            body = page.query_selector("body")
            text = body.inner_text() if body else "❌ 無法擷取 body 元素"
            
            # 關閉 Context 與瀏覽器
            context.close()
            browser.close()
            
            return {"text": text, "source": "playwright"}

    except Exception as e:
        # 如果 playwright 失敗，用 requests 做備援
        r = requests.get("https://xinying.tainan.gov.tw/")
        return {
            "text": r.text[:2000],
            "source": "requests",
            "error": str(e),
            "traceback": traceback.format_exc()
        }













