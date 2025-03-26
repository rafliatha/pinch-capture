## Hand Gesture Capture

###Deskripsi

Program ini menggunakan OpenCV dan MediaPipe untuk mendeteksi tangan melalui webcam. Jika ibu jari dan telunjuk bersentuhan atau mendekati jarak tertentu, program akan menangkap dan menyimpan gambar secara otomatis.

###Fitur
- Deteksi tangan secara real-time menggunakan MediaPipe
- Menggambar titik dan garis koneksi pada tangan yang terdeteksi
- Menangkap gambar secara otomatis saat ibu jari dan telunjuk bersentuhan
- Menyimpan gambar yang ditangkap dalam format .png

###Prasyarat
Sebelum menjalankan program, pastikan Anda telah menginstal pustaka berikut:
    pip install opencv-python mediapipe numpy

###Cara Menjalankan
- Jalankan program dengan perintah berikut:

    python script.py

- Program akan menampilkan tampilan video dari webcam.
- Saat ibu jari dan telunjuk mendekati satu sama lain (kurang dari 30 piksel), program akan menangkap gambar.
- Gambar yang diambil akan disimpan dalam format capture_X.png, di mana X adalah nomor urutan.
- Tekan tombol q untuk keluar dari program.

###Struktur Program
- Inisialisasi Kamera: Membuka webcam untuk menangkap video secara real-time.
- Deteksi Tangan: Menggunakan MediaPipe untuk mendeteksi dan melacak posisi tangan.
- Perhitungan Jarak: Menghitung jarak antara ibu jari dan telunjuk.
- Penangkapan Gambar: Jika jarak di bawah ambang batas (30 piksel), gambar disimpan.
- Keluar Program: Tekan q untuk keluar dari program.

###Catatan
- Pastikan kamera laptop/PC dalam kondisi berfungsi.
- Sesuaikan threshold jarak jika perlu untuk sensitivitas yang lebih baik.
