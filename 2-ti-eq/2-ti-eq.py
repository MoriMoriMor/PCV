"""
Created on Mon Sep  27 20:40:04 2026

@author: yoga
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def proses_transformasi(gambar_input, mode='pencerahan', alpha=1.3, beta=40):
    tinggi, lebar = gambar_input.shape
    img_hasil = np.zeros((tinggi, lebar), dtype=np.float32)
    
    if mode == 'pencerahan':
        for b in range(tinggi):
            for k in range(lebar):
                val = alpha * float(gambar_input[b, k]) + beta
                if val > 255.0:
                    img_hasil[b, k] = 255.0
                elif val < 0.0:
                    img_hasil[b, k] = 0.0
                else:
                    img_hasil[b, k] = val
                    
    elif mode == 'negatif':
        for b in range(tinggi):
            for k in range(lebar):
                img_hasil[b, k] = 255.0 - float(gambar_input[b, k])
                
    return img_hasil.astype(np.uint8)

def jalankan_ekualisasi(gambar_input):
    tinggi, lebar = gambar_input.shape
    jml_pixel = tinggi * lebar
    
    tabel_frekuensi = np.zeros(256, dtype=int)
    for b in range(tinggi):
        for k in range(lebar):
            tabel_frekuensi[gambar_input[b, k]] += 1
            
    tabel_cdf = np.zeros(256, dtype=float)
    tabel_cdf[0] = tabel_frekuensi[0]
    for idx in range(1, 256):
        tabel_cdf[idx] = tabel_cdf[idx-1] + tabel_frekuensi[idx]
        
    cdf_minimum = 0
    for val_celi in tabel_cdf:
        if val_celi > 0:
            cdf_minimum = val_celi
            break
            
    cdf_normal = np.zeros(256, dtype=np.uint8)
    for idx in range(256):
        if tabel_cdf[idx] > 0:
            pembilang = tabel_cdf[idx] - cdf_minimum
            penyebut = jml_pixel - cdf_minimum
            rasio = (pembilang / penyebut) * 255.0
            
            selisih = rasio - int(rasio)
            if selisih >= 0.5:
                cdf_normal[idx] = int(rasio) + 1
            else:
                cdf_normal[idx] = int(rasio)
        else:
            cdf_normal[idx] = 0
            
    img_terekualisasi = np.zeros((tinggi, lebar), dtype=np.uint8)
    for b in range(tinggi):
        for k in range(lebar):
            img_terekualisasi[b, k] = cdf_normal[gambar_input[b, k]]
            
    return img_terekualisasi, tabel_frekuensi, cdf_normal

if __name__ == "__main__":
    nama_berkas = 'sepurane_keturon.jpeg'
    
    img_mentah = cv2.imread(nama_berkas, cv2.IMREAD_GRAYSCALE)
    
    if img_mentah is None:
        print(f"Peringatan: File '{nama_berkas}' tidak ditemukan. Periksa kembali nama file!")
    else:
        print("File berhasil dimuat. Memproses kalkulasi...")
        
        img_pencerahan = proses_transformasi(img_mentah, mode='pencerahan', alpha=1.3, beta=40)
        img_negatif = proses_transformasi(img_mentah, mode='negatif')
        
        img_hasil_eq, hist_asli, _ = jalankan_ekualisasi(img_mentah)
        
        hist_hasil_eq = np.zeros(256, dtype=int)
        h_eq, w_eq = img_hasil_eq.shape
        for b in range(h_eq):
            for k in range(w_eq):
                hist_hasil_eq[img_hasil_eq[b, k]] += 1

        plt.figure(figsize=(13, 8))
        
        plt.subplot(2, 3, 1)
        plt.imshow(img_mentah, cmap='gray')
        plt.title('1. Citra Asli (Grayscale)')
        plt.axis('off')
        
        plt.subplot(2, 3, 2)
        plt.imshow(img_pencerahan, cmap='gray')
        plt.title('2. Transformasi Pencerahan')
        plt.axis('off')
        
        plt.subplot(2, 3, 3)
        plt.imshow(img_negatif, cmap='gray')
        plt.title('3. Transformasi Negatif')
        plt.axis('off')
        
        plt.subplot(2, 3, 4)
        plt.imshow(img_hasil_eq, cmap='gray')
        plt.title('4. Hasil Ekualisasi Manual')
        plt.axis('off')
        
        plt.subplot(2, 3, 5)
        plt.plot(hist_asli, color='purple', linewidth=1.2)
        plt.title('Histogram Asli')
        plt.xlim([0, 255])
        plt.grid(alpha=0.3)
        
        plt.subplot(2, 3, 6)
        plt.plot(hist_hasil_eq, color='teal', linewidth=1.2)
        plt.title('Histogram Setelah Ekualisasi')
        plt.xlim([0, 255])
        plt.grid(alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        print("Proses komputasi selesai!")
