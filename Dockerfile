FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Pastikan menggunakan versi prebuilt (tanpa kompilasi)
RUN pip install --upgrade pip
RUN pip install --prefer-binary -r requirements.txt

COPY . .

CMD ["python", "main.py"]
