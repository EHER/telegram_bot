FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
COPY .env .
COPY bot.py .
COPY model.py .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "bot.py"]
