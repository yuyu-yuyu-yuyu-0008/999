FROM python:3.12-slim-bookworm

WORKDIR /app

# 安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製程式碼
COPY . /app

# 啟動服務
CMD ["uvicorn", "999:app", "--host", "0.0.0.0", "--port", "8080"]


