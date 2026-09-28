# PCV ASSIGNMENTS
## 1-Intro.py 
Program ini dibuat untuk memanipulasi warna gambar dan video real-time dengan cara memisahkan serta menggabungkan kanal warna dasar (Merah, Hijau, Biru) menggunakan OpenCV dan NumPy.

### A. Cara Kerja Program
#### 1. Memproses Gambar Statis (aoka_coklat.jpeg)
- Cara kerja: Program membaca file gambar dari direktori, lalu mengubahnya menjadi hitam-putih (grayscale).
- Setelah itu, data tingkat keabuan tersebut dimasukkan secara manual ke dalam kanal warna tertentu (misalnya dimasukkan ke kanal merah saja untuk membuat seluruh gambar bernuansa merah, atau digabung ke kanal hijau dan merah sekaligus untuk menghasilkan nuansa kuning).

#### 2. Memproses Live Webcam (Kamera Laptop)
- Cara kerja: Program membuka akses kamera secara langsung (real-time) per _frame_ video menggunakan perulangan (while True).
- Setiap frame yang ditangkap kamera langsung diubah ke _grayscale_ secara instan, lalu diberi filter warna yang sama (merah, hijau, dan kuning) seperti pada gambar statis tadi. Program akan terus berjalan sampai Anda menekan tombol q pada keyboard untuk keluar.

### B. Output
#### 1. Gambar Statis
Membuka beberapa jendela terpisah secara bersamaan yang menampilkan gambar asli (aoka_coklat.jpeg), versi hitam-putih, hingga hasil filter modifikasi warna (Biru, Hijau, Kuning, dan Merah).
<img width="1000" height="500" alt="opencv_output_statis" src="https://github.com/user-attachments/assets/6f7c2d2d-b68b-4ec7-be8c-786cdd8365b8" />


#### 2. Live Webcam
Membuka jendela video tangkapan kamera secara real-time yang warnanya berubah-ubah otomatis sesuai filter (jendela terpisah untuk filter merah, hijau, dan kuning) berdasarkan pergerakan di depan kamera.
<img width="1000" height="500" alt="opencv_output_livecam" src="https://github.com/user-attachments/assets/aa3a9ac8-aa55-4a49-b7cc-b28b09a98b18" />



## 2-ti-eq

