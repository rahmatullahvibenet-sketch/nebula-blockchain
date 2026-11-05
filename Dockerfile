FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends openssl && rm -rf /var/lib/apt/lists/* \
 && pip install --no-cache-dir cryptography
WORKDIR /app
COPY . /app
ENV PYTHONUNBUFFERED=1
EXPOSE 8333
CMD ["sh", "-c", "tail -f /dev/null | python3 nebula_v10_24.py node --port 8333 --datadir /data"]
