"""
Created on Tue Sep  28 22:56:04 2026

@author: yoga
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def terapkan_konvolusi_warna(gambar_input, kernel):
    tinggi, lebar, channel = gambar_input.shape
    k_tinggi, k_lebar = kernel.shape
    pad_t = k_tinggi // 2
    pad_l = k_lebar // 2
    
    img_hasil = np.zeros((tinggi, lebar, channel), dtype=np.float32)
    
    for c in range(channel):
        kanal_tunggal = gambar_input[:, :, c].astype(np.float32)
        citra_pad = np.pad(kanal_tunggal, ((pad_t, pad_t), (pad_l, pad_l)), mode='edge')
        kanal_hasil = np.zeros((tinggi, lebar), dtype=np.float32)
        
        for b in range(tinggi):
            for k in range(lebar):
                area_lokal = citra_pad[b:b + k_tinggi, k:k + k_lebar]
                nilai_konvolusi = np.sum(area_lokal * kernel)
                
                if nilai_konvolusi > 255.0:
                    kanal_hasil[b, k] = 255.0
                elif nilai_konvolusi < 0.0:
                    kanal_hasil[b, k] = 0.0
                else:
                    kanal_hasil[b, k] = nilai_konvolusi
                    
        img_hasil[:, :, c] = kanal_hasil
        
    return img_hasil.astype(np.uint8)

def filter_median_warna(gambar_input, ukuran_kernel=3):
    tinggi, lebar, channel = gambar_input.shape
    pad = ukuran_kernel // 2
    img_hasil = np.zeros((tinggi, lebar, channel), dtype=np.uint8)
    
    for c in range(channel):
        kanal_tunggal = gambar_input[:, :, c].astype(np.float32)
        citra_pad = np.pad(kanal_tunggal, ((pad, pad), (pad, pad)), mode='edge')
        kanal_hasil = np.zeros((tinggi, lebar), dtype=np.uint8)
        
        for b in range(tinggi):
            for k in range(lebar):
                area_lokal = citra_pad[b:b + ukuran_kernel, k:k + ukuran_kernel]
                vektor_lokal = area_lokal.flatten()
                
                for i in range(len(vektor_lokal)):
                    for j in range(i + 1, len(vektor_lokal)):
                        if vektor_lokal[i] > vektor_lokal[j]:
                            temp = vektor_lokal[i]
                            vektor_lokal[i] = vektor_lokal[j]
                            vektor_lokal[j] = temp
                            
                tengah = len(vektor_lokal) // 2
                kanal_hasil[b, k] = int(vektor_lokal[tengah])
                
        img_hasil[:, :, c] = kanal_hasil
        
    return img_hasil

if __name__ == "__main__":
    nama_berkas = 'rooftop_view.jpeg'
    
    img_mentah_bgr = cv2.imread(nama_berkas, cv2.IMREAD_COLOR)
    
    if img_mentah_bgr is None:
        print(f"Peringatan: File '{nama_berkas}' tidak ditemukan. Periksa kembali nama file!")
    else:
        print("File berhasil dimuat. Memproses...")
        
        img_mentah_rgb = cv2.cvtColor(img_mentah_bgr, cv2.COLOR_BGR2RGB)
        
        kernel_rata = np.ones((7, 7), dtype=np.float32) / 49.0
        
        kernel_sharpen_unik = np.array([
            [0.0, -1.0, 0.0],
            [-1.0, 5.0, -1.0],
            [0.0, -1.0, 0.0]
        ], dtype=np.float32)
        
        img_smoothing = terapkan_konvolusi_warna(img_mentah_rgb, kernel_rata)
        img_sharpen = terapkan_konvolusi_warna(img_mentah_rgb, kernel_sharpen_unik)
        img_median = filter_median_warna(img_mentah_rgb, ukuran_kernel=3)

        plt.figure(figsize=(13, 8))
        
        plt.subplot(2, 2, 1)
        plt.imshow(img_mentah_rgb)
        plt.title('1. Citra Asli')
        plt.axis('off')
        
        plt.subplot(2, 2, 2)
        plt.imshow(img_smoothing)
        plt.title('2. Filter Smoothing')
        plt.axis('off')
        
        plt.subplot(2, 2, 3)
        plt.imshow(img_sharpen)
        plt.title('3. Filter Sharpening )
        plt.axis('off')
        
        plt.subplot(2, 2, 4)
        plt.imshow(img_median)
        plt.title('4. Filter Median')
        plt.axis('off')
        
        plt.tight_layout()
        plt.show()
        print("Proses filter spasial selesai!")
