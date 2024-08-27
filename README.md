# Automate Task Scheduler

Automate Task Scheduler adalah sebuah project Python yang digunakan untuk mengotomatisasi penjadwalan task di Windows Task Scheduler. Project ini memanfaatkan file JSON yang berisi daftar flow dari Power Automate dan menghasilkan file XML untuk diimport ke dalam Task Scheduler.

## Fitur

- Menghasilkan file XML dari data JSON untuk Task Scheduler.
- Mengatur tugas secara otomatis berdasarkan flow dari Power Automate.
- Menggunakan konfigurasi variabel lingkungan untuk fleksibilitas dan keamanan.

## Prasyarat

Pastikan Anda sudah menginstal prasyarat berikut sebelum memulai:

- Python 3.8 atau lebih tinggi
- Pip (Python package manager)
- Windows OS (karena menggunakan Windows Task Scheduler)
- Anaconda atau Virtualenv (opsional, untuk mengelola lingkungan Python)

## Langkah pemakaian    

Ikuti langkah-langkah di bawah ini untuk menginstal dan menyiapkan project ini:

1. **Clone repository ini**:

   ```bash
   git clone https://github.com/romijulianto/automate-task-scheduler.git
   cd automate-task-scheduler
   ```
2. **Install packages**:

   ```bash
   pip install -r requirements.txt
   ```
3. **Buat File .env**:

   ```bash
   buat file .env dari .env.example
   ```
4. **Running**:

   ```bash
   python server.py 
   python import.py
   ```
