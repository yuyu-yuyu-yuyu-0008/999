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
            browser = p.chromium.launch(
                headless=True,
                args=["--no-sandbox", "--disable-dev-shm-usage"]
            )
            page = browser.new_page()
            page.goto("https://xinying.tainan.gov.tw/", timeout=90000)
            page.wait_for_selector("body", timeout=60000)
            text = page.inner_text("body")
            browser.close()
            return {"text": text[:2000], "source": "playwright"}
    except Exception as e:
        # fallback
        r = requests.get("https://xinying.tainan.gov.tw/")
        return {"text": r.text[:2000], "source": "requests", "error": str(e)}












