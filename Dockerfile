# --- Tahap 1: Builder ---
# Di tahap ini kita mempersiapkan semua kebutuhan dan menginstall library.
# Menggunakan 'slim' agar ukurannya lebih kecil.
FROM python:3.12-slim AS builder

# Variabel lingkungan standar untuk Python di Docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Tentukan direktori kerja di dalam container
WORKDIR /app

# Install paket sistem yang dibutuhkan untuk kompilasi `mysqlclient`
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libmariadb-dev \
    pkg-config \
    gcc

# Buat dan aktifkan virtual environment di dalam container
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Salin file requirements dan install semua library Python ke venv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# --- Tahap 2: Runner ---
# Di tahap ini kita membuat image akhir yang akan dijalankan.
# Image ini lebih bersih dan hanya berisi apa yang dibutuhkan.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# Salin virtual environment yang sudah jadi dari tahap 'builder'
COPY --from=builder /opt/venv /opt/venv

# Salin semua kode aplikasi Anda
COPY . .

# Aktifkan virtual environment untuk perintah selanjutnya
ENV PATH="/opt/venv/bin:$PATH"

# Perintah untuk menjalankan server Gunicorn saat container dimulai.
# Railway akan secara otomatis memberikan nilai untuk variabel $PORT.
CMD gunicorn mysite.wsgi --bind 0.0.0.0:$PORT --log-file -