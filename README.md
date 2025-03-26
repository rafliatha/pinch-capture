# Motion Capture dengan Gesture Tangan

Program untuk menangkap gambar menggunakan gesture tangan. Program ini menggunakan MediaPipe untuk mendeteksi tangan dan OpenCV untuk menangkap gambar dari kamera.

## Fitur

- Deteksi gesture tangan menggunakan MediaPipe
- Capture gambar otomatis dengan gesture pinch (jempol dan telunjuk)
- Tampilan real-time dengan OpenCV
- Visualisasi landmark tangan
- Penyimpanan gambar otomatis dengan penomoran berurutan

## Persyaratan

- Python 3.x
- OpenCV (cv2)
- MediaPipe
- NumPy

## Instalasi

1. Clone repository ini
2. Install dependencies yang diperlukan:
```bash
pip install opencv-python mediapipe numpy
```

## Cara Penggunaan

1. Jalankan program:
```bash
python capture.py
```

2. Cara menangkap gambar:
   - Tampilkan tangan Anda di depan kamera
   - Lakukan gesture pinch (menjepit) dengan jempol dan telunjuk
   - Program akan otomatis menangkap gambar ketika jarak antara jempol dan telunjuk cukup dekat
   - Gambar akan disimpan dengan format `capture_X.png` (X adalah nomor urut)

3. Tekan 'q' untuk keluar dari program

## Cara Kerja

Program menggunakan MediaPipe untuk mendeteksi landmark tangan, khususnya posisi jempol dan telunjuk. Ketika jarak antara kedua jari tersebut lebih kecil dari threshold yang ditentukan (30 pixel), program akan otomatis menangkap gambar dari kamera dan menyimpannya ke file.

## Output

Gambar yang ditangkap akan disimpan dalam format PNG dengan nama file:
- capture_0.png
- capture_1.png
- capture_2.png
dst.
