# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:40:04 2026

@author: yoga
"""
import cv2
import numpy as np

img = cv2.imread("aoka_coklat.jpeg")

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    abu = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    merah = np.zeros_like(img)
    merah[:, :, 2] = gray

    hijau = np.zeros_like(img)
    hijau[:, :, 1] = gray

    biru = np.zeros_like(img)
    biru[:, :, 0] = gray

    kuning = np.zeros_like(img)
    kuning[:, :, 1] = gray
    kuning[:, :, 2] = gray

    cv2.imshow("Original Image", img)
    cv2.imshow("Abu-abu Image", abu)
    cv2.imshow("Merah Image", merah)
    cv2.imshow("Hijau Image", hijau)
    cv2.imshow("Biru Image", biru)
    cv2.imshow("Kuning Image", kuning)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ga bisa akses webacam")
    exit()

print("webcam nyala, tekan q untuk keluar")

while True:
    ret, frame = cap.read()
    if not ret:
        print("gabisa baca feed webcam")
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_abu = cv2.cvtColor(frame_gray, cv2.COLOR_GRAY2BGR)

    frame_merah = np.zeros_like(frame)
    frame_merah[:, :, 2] = frame_gray

    frame_hijau = np.zeros_like(frame)
    frame_hijau[:, :, 1] = frame_gray

    frame_kuning = np.zeros_like(frame)
    frame_kuning[:, :, 1] = frame_gray
    frame_kuning[:, :, 2] = frame_gray

    cv2.imshow("Webcam - Original", frame)
    cv2.imshow("Webcam - Filter Merah", frame_merah)
    cv2.imshow("Webcam - Filter Hijau", frame_hijau)
    cv2.imshow("Webcam - Filter Kuning", frame_kuning)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()