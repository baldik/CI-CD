# Используем актуальный, минималистичный и безопасный образ
FROM python:3.11-slim-bookworm
WORKDIR /app
# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Копируем исходный код
COPY . .
# Запускаем приложение от непривилегированного пользователя
RUN useradd -m -r appuser && chown -R appuser /app
USER appuser
CMD ["python", "app.py"]
