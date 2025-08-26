FROM python:3.12-slim-bookworm

WORKDIR /app

# 安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y \
    libnss3 libxss1 libasound2 fonts-liberation \
    libatk-bridge2.0-0 libatk1.0-0 libcups2 \
    libdrm2 libxkbcommon0 libgbm1
    
# 如果你沒有 requirements.txt，可以直接這樣裝
# RUN pip install fastapi uvicorn[standard]

# 複製程式碼
COPY . /app

# 啟動服務
CMD ["uvicorn", "999:app", "--host", "0.0.0.0", "--port", "8080"]



