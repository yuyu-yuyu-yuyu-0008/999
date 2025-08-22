from fastapi import FastAPI
from playwright.sync_api import sync_playwright

app = FastAPI()

# Health check endpoints（Leapcell 檢查會用到）
@app.get("/kaithhealthcheck")
@app.get("/kaithheathcheck")
def healthcheck():
    return {"status": "ok"}

@app.get("/fetch")
def fetch_yahoo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://xinying.tainan.gov.tw/", timeout=90000)
        page.wait_for_selector("body", timeout=60000)
        body = page.query_selector("body")
        text = body.inner_text() if body else "❌ 無法擷取 body 元素"
        browser.close()
        return {"text": text}









