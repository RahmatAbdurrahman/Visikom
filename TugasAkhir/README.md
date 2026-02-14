# Pemanfaatan SIFT untuk Image Matching (Tugas Besar Visi Komputer)

[cite_start]Proyek ini bertujuan untuk menguji pemahaman mengenai konsep *feature detection* dan *feature matching* menggunakan algoritma **Scale-Invariant Feature Transform (SIFT)**[cite: 5]. [cite_start]Proyek ini juga mencakup perbandingan dengan algoritma **ORB** sebagai nilai tambah dalam analisis[cite: 13].

## 📋 Deskripsi Proyek
Implementasi ini mencakup tiga skenario utama pencocokan citra:
1. **ORB dengan Brute-Force Matcher**: Metode deteksi fitur biner yang cepat.
2. **SIFT dengan Brute-Force Matcher (Ratio Test)**: Implementasi standar SIFT dengan penyaringan jarak Lowe.
3. **SIFT dengan FLANN Based Matcher**: Optimasi pencocokan untuk dataset fitur yang besar.

## 🛠️ Prasyarat (Requirements)
[cite_start]Bahasa pemrograman yang digunakan adalah **Python** [cite: 16] [cite_start]dengan pustaka utama sebagai berikut[cite: 17]:
* [cite_start]**OpenCV**: Untuk pemrosesan citra dan algoritma SIFT/ORB[cite: 18].
* [cite_start]**NumPy**: Untuk manipulasi array data[cite: 19].
* [cite_start]**Matplotlib**: Untuk visualisasi hasil matching[cite: 20].

Instalasi pustaka dapat dilakukan melalui terminal:
```bash
pip install opencv-python numpy matplotlib
```

📁 Struktur Folder
<img width="579" height="129" alt="image" src="https://github.com/user-attachments/assets/eecf52a9-7326-4916-bb49-1b90622244e3" />

.
├── images/           # Folder berisi dataset citra (FM1.jpeg, FM2.jpeg)
├── orb_bf.py         # Skrip pencocokan ORB + Brute-Force
├── sift_bf.py        # Skrip pencocokan SIFT + Brute-Force (Ratio Test)
├── sift_flann.py     # Skrip pencocokan SIFT + FLANN Matcher
└── README.md         # Dokumentasi proyek

🚀 Cara Menjalankan
Pastikan dataset gambar berada di dalam folder ./images/ dengan nama FM1.jpeg dan FM2.jpeg.

Buka terminal atau VS Code pada direktori proyek.

Jalankan skrip menggunakan perintah:
```bash
python code/Image_Matching-ORB.py
```

📊 Analisis Invariansi
Program ini dirancang untuk membuktikan invariansi SIFT terhadap:

Skala: Tetap mengenali objek meski ukuran pada citra berubah.
Rotasi: Tetap mengenali objek meski posisi citra diputar.

✍️ Penulis
Nama: Rahmat Abdurrahman
Instansi: Universitas Darussalam Gontor

