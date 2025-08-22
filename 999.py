from fastapi import FastAPI
from playwright.sync_api import sync_playwright
import requests

app = FastAPI()

@app.get("/kaithhealthcheck")
@app.get("/kaithheathcheck")
def healthcheck():
    return {"status": "ok"}

@app.get("/fetch")
def fetch_site():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://xinying.tainan.gov.tw/", timeout=90000)
            page.wait_for_selector("body", timeout=60000)
            body = page.query_selector("body")
            text = body.inner_text() if body else "❌ 無法擷取 body 元素"
            browser.close()
            return {"text": text, "source": "playwright"}
    except Exception as e:
        # 如果 playwright 爆掉，就用 requests 當備援
        r = requests.get("https://xinying.tainan.gov.tw/")
        return {"text": r.text[:2000], "source": "requests", "error": str(e)}











