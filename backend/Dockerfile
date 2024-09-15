FROM python:3.12-alpine AS builder
LABEL stage="builder"

WORKDIR /app

COPY requirements.txt ./

RUN pip wheel --no-cache-dir --wheel-dir wheels -r requirements.txt


FROM python:3.12-alpine AS runner

COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/* && rm -rf /wheels

WORKDIR /app

COPY src src
COPY pyproject.toml .
RUN pip install --no-cache-dir --no-deps .

WORKDIR /app/src/basic_shop

RUN python manage.py makemigrations shop
RUN python manage.py migrate

EXPOSE 8000

ENTRYPOINT [ "python", "-m", "uvicorn", "basic_shop.asgi:application", "--host", "0.0.0.0" ]
