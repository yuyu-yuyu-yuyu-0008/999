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
        page.goto("https://tw.yahoo.com/", timeout=60000)
        content = page.content()
        browser.close()
        return {"html": content}








