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
<img width="928" height="551" alt="opencv_output_statis" src="https://github.com/user-attachments/assets/6f7c2d2d-b68b-4ec7-be8c-786cdd8365b8" />
#### 2. Live Webcam
Membuka jendela video tangkapan kamera secara real-time yang warnanya berubah-ubah otomatis sesuai filter (jendela terpisah untuk filter merah, hijau, dan kuning) berdasarkan pergerakan di depan kamera.
<img width="928" height="551" alt="opencv_output_livecam" src="https://github.com/user-attachments/assets/aa3a9ac8-aa55-4a49-b7cc-b28b09a98b18" />



## 2-ti-eq
Program ini dibuat untuk melakukan perbaikan kualitas citra melalui _point operations_ secara manual tanpa menggunakan fungsi instan bawaan dari library yang meliputi pengaturan pencerahan, pembuatan citra negatif, hingga perataan kontras otomatis (histogram equalization).

### A. Cara Kerja Program
Program memuat gambar masukan dalam format hitam-putih (grayscale), lalu memprosesnya melalui tiga tahapan utama:
#### 1. Transformasi Pencerahan
Mengubah intensitas setiap piksel menggunakan rumus linier ($pixel\_baru = \alpha \times pixel\_lama + \beta$). Nilai $\alpha$ berfungsi mengatur kontras, sedangkan $\beta$ berfungsi menambah atau mengurangi tingkat kecerahan secara matematis.
#### 2. Transformasi Negatif
Membalikkan nilai intensitas piksel secara berkebalikan dari nilai maksimumnya ($255 - nilai\_pixel\_lama$). Hal ini membuat area gelap menjadi terang dan sebaliknya, menyerupai film negatif kamera analog.
#### 3. Ekualisasi Histogram Manual
Program menghitung tabel frekuensi kemunculan setiap nilai piksel, membangun fungsi distribusi kumulatif (CDF), lalu menormalkan kembali rentangnya dari 0 sampai 255. Proses ini membuat distribusi intensitas warna tersebar merata agar detail gambar yang awalnya kurang jelas menjadi lebih tajam.

### B. Output
1. Panel 1 - Citra Asli (Grayscale): Menampilkan gambar masukan awal dalam format keabuan.
2. Panel 2 - Transformasi Pencerahan: Menampilkan hasil gambar yang tampak lebih terang dan kontrasnya meningkat.
3. Panel 3 - Transformasi Negatif: Menampilkan hasil pembalikan warna di mana bagian terang menjadi gelap total.
4. Panel 4 - Hasil Ekualisasi Manual: Menampilkan gambar dengan ketajaman dan kontras lokal yang jauh lebih merata.
5. Panel 5 & 6 - Perbandingan Grafik Histogram Asli dan Setelah Ekualisasi: Menampilkan perbandingan grafik distribusi intensitas piksel. Histogram asli terlihat tidak merata, sedangkan histogram setelah ekualisasi tersebar lebih luas untuk memaksimalkan detail gambar.
<img width="928" height="551" alt="Figure 2026-09-29 010001" src="https://github.com/user-attachments/assets/2b87a108-1824-42e4-a96f-2f3661422425" />



## 3-filter-spasial
Program ini dirancang untuk menerapkan operasi spasial secara manual pada kanal warna tanpa menggunakan fungsi instan filter bawaan OpenCV, lengkap dengan teknik padding agar bagian pinggir gambar tidak rusak.

### A. Cara Kerja Program
Program memuat file citra berwarna, lalu memprosesnya melalui tiga tahapan filter spasial secara independen di setiap kanal warna:
#### 1. Filter Smoothing (Mean Blur)
Menggunakan kernel rata-rata berukuran $7 \times 7$ untuk merata-rata nilai piksel tetangga di sekitar area lokal. Teknik ini berfungsi meredam variasi intensitas yang terlalu tajam dan membuat gambar menjadi lebih halus (blur)
#### 2. Filter Sharpening (Penajaman)
Menggunakan matriks kernel khusus (-1, 5, -1) untuk mempertegas perbedaan intensitas piksel yang saling berdampingan. Proses ini bertujuan menajamkan detail objek, memperjelas garis, dan membuat tekstur pada gambar tampak jauh lebih kontras.
#### 3. Filter Median
Menyortir nilai piksel di area lokal secara manual menggunakan algoritma pengurutan (sorting) untuk mencari nilai tengahnya. Filter ini sangat efektif membersihkan derau (noise) acak tanpa mengorbankan ketajaman tepi objek utama.

### B. Output
Hasil eksekusi program ini menampilkan satu jendela grid berisi 4 panel perbandingan citra:
1. Panel 1 - Citra Asli: Menampilkan gambar masukan awal (rooftop_view.jpeg) dalam format warna RGB.
2. Panel 2 - Filter Smoothing: Menampilkan hasil gambar yang tampak lebih kabur/halus karena perataan nilai piksel tetangga.
3. Panel 3 - Filter Sharpening: Menampilkan hasil gambar dengan detail garis, tepi bangunan, dan tekstur yang menjadi jauh lebih tegas dan tajam.
4. Panel 4 - Filter Median: Menampilkan hasil pembersihan citra menggunakan nilai tengah piksel lokal, menjaga kualitas visual agar tetap bersih dan natural.
<img width="598" height="569" alt="Figure 2026-09-29 010848" src="https://github.com/user-attachments/assets/b2fcdc0b-7cc1-4e7a-bad5-299b40bfa074" />



## 4-model-warna
Kode ini akan membaca sebuah citra digital dan melakukan konversi ruang warna secara simultan ke dalam empat model warna utama: RGB, HSV, HSI, dan CMYK.

### A. Cara Kerja Program
Program memuat file citra digital, lalu memprosesnya melalui beberapa tahapan konversi matematis dan fungsi pustaka standar:
#### 1. Konversi Ke Ruang Warna HSV
Menggunakan fungsi bawaan pustaka OpenCV (cv2.cvtColor) untuk mengubah format warna standar BGR ke dalam model HSV (Hue, Saturation, Value), yang memisahkan informasi warna dasar (Hue) dari aspek pencahayaan.
#### 2. Konversi ke Ruang Warna HSI
Mengekstrak kanal warna RGB, melakukan normalisasi rentang piksel, lalu menghitung komponen Intensity (rata-rata intensitas), Saturation (tingkat kejenuhan), dan Hue (sudut warna menggunakan perhitungan trigonometri berbasis matriks) secara manual.
#### 3. Konversi ke Ruang Warna CMYK
Mengonversi nilai piksel RGB ke model warna subtraktif cetak dengan mencari nilai maksimum untuk mengekstrak komponen kunci Key / Hitam ($K$), lalu menurunkan nilai komponen Cyan, Magenta, dan Yellow.

### B. Output
Hasil eksekusi program ini menampilkan satu jendela grid berisi 4 panel perbandingan citra:
1. Panel 1 - RGB (Asli): Menampilkan gambar masukan awal (dana_masuk.png) dalam format warna standar RGB.
2. Panel 2 - HSV: Menampilkan hasil konversi ke ruang warna HSV dengan pergeseran tampilan visual akibat pemisahan kanal kecerahan dan warna dasar.
3. Panel 3 - HSI: Menampilkan hasil konversi ruang warna HSI berdasarkan perhitungan manual intensitas dan sudut hue.
4. Panel 4 - CMYK: Menampilkan kanal komponen hitam (Key/K) dari model CMYK dalam bentuk citra grayscale untuk melihat distribusi elemen gelap pada gambar.
<img width="1521" height="849" alt="image" src="https://github.com/user-attachments/assets/b47f8206-3ff5-4f3e-becc-a8b678812ae7" />

