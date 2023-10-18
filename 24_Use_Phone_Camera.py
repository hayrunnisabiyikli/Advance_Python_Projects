import cv2

# URL adresini buraya yerleştirin
url = "Your_URL_here"

cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Kamera verisi alınamadı.")
        break

    cv2.imshow("Frame", frame)

    # Eğer "q" tuşuna basılırsa döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
