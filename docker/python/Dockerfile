FROM python:3.9.2-buster

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

COPY ./docker/python/requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app

# Tesseract-OCRのインストールを追加
RUN apt-get update \
    && apt-get install -y tesseract-ocr \
    && apt-get install -y libgl1-mesa-glx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
