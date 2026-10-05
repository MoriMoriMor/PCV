# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 22:12:21 2026

@author: yoga
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

file_gambar = 'dana_masuk.png'
gambar_bgr = cv2.imread(file_gambar)

if gambar_bgr is None:
  print('Gambar tidak ditemukan...')
else:
  gambar_rgb = cv2.cvtColor(gambar_bgr, cv2.COLOR_BGR2RGB)

  gambar_hsv = cv2.cvtColor(gambar_bgr, cv2.COLOR_BGR2HSV)

  f_img = gambar_rgb.astype(np.float32) / 255.0
  r, g, b = f_img[:, :, 0], f_img[:, :, 1], f_img[:, :, 2]

  i_channel = (r + g + b) / 3.0

  min_rgb = np.minimum(np.minimum(r, g), b)
  s_channel = 1.0 - (3.0 / (r + g + b + 1e-6)) * min_rgb

  atas = 0.5 * ((r - g) + (r - b))
  bawah = np.sqrt((r - g) ** 2 + (r - b) * (g - b)) + 1e-6
  h_channel = np.arccos(np.clip(atas / bawah, -1.0, 1.0))
  h_channel[b > g] = 2 * np.pi - h_channel[b > g]
  h_channel = h_channel / (2 * np.pi)

  gambar_hsi = cv2.merge(
      [
          (h_channel * 255).astype(np.uint8),
          (s_channel * 255).astype(np.uint8),
          (i_channel * 255).astype(np.uint8),
      ]
  )

  
  k_channel = 1.0 - np.fmax(np.fmax(r, g), b)
  penyebut = 1.0 - k_channel
  penyebut[penyebut == 0] = 1e-6

  c_channel = (1.0 - r - k_channel) / penyebut
  m_channel = (1.0 - g - k_channel) / penyebut
  y_channel = (1.0 - b - k_channel) / penyebut

  plt.figure(figsize=(12, 6))

  plt.subplot(2, 3, 1)
  plt.imshow(gambar_rgb)
  plt.title('1. RGB (Asli)')
  plt.axis('off')

  plt.subplot(2, 3, 2)
  plt.imshow(gambar_hsv)
  plt.title('2. HSV')
  plt.axis('off')

  plt.subplot(2, 3, 3)
  plt.imshow(gambar_hsi)
  plt.title('3. HSI')
  plt.axis('off')

  plt.subplot(2, 3, 4)
  plt.imshow(k_channel, cmap='gray')
  plt.title('4. CMYK')
  plt.axis('off')

  plt.tight_layout()
  plt.show()
