import cv2
import mediapipe as mp
import numpy as np
import time

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Inisialisasi Kamera
cap = cv2.VideoCapture(0)
capture_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame untuk pengalaman mirroring
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Deteksi tangan
    result = hands.process(rgb_frame)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Ambil koordinat ibu jari (tip) dan telunjuk (tip)
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Konversi ke piksel
            h, w, _ = frame.shape
            thumb_pos = (int(thumb_tip.x * w), int(thumb_tip.y * h))
            index_pos = (int(index_tip.x * w), int(index_tip.y * h))

            # Hitung jarak antara ibu jari dan telunjuk
            distance = np.linalg.norm(np.array(thumb_pos) - np.array(index_pos))

            # Jika jarak cukup kecil, tangkap gambar
            if distance < 30:  # Threshold jarak (pixel)
                cv2.putText(frame, "Capture!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                # Simpan gambar
                filename = f"capture_{capture_count}.png"
                cv2.imwrite(filename, frame)
                capture_count += 1
                time.sleep(0.5)  # Delay untuk mencegah multiple captures

    # Tampilkan frame
    cv2.imshow("Hand Gesture Capture", frame)

    # Break jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan resources
cap.release()
cv2.destroyAllWindows()
