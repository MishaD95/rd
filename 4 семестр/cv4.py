import cv2  # Підключаємо бібліотеку OpenCV
import numpy as np  # Для роботи з масивами та порогами

def apply_sobel(frame, threshold_level):
    """Застосування фільтра Собеля для виділення меж із заданим порогом"""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Перетворюємо кадр у відтінки сірого
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # Обчислюємо похідну по X
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Обчислюємо похідну по Y
    sobel = cv2.magnitude(sobelx, sobely)  # Обчислюємо градієнт (загальна сила межі)
    sobel = np.uint8(np.clip(sobel, 0, 255))  # Приводимо до діапазону [0..255]

    # Порогове виділення меж
    _, binary = cv2.threshold(sobel, threshold_level, 255, cv2.THRESH_BINARY)
    return binary  # Повертаємо двійкове зображення з межами

#  Відео з файлу 
video_file = 'video.mp4'
cap_file = cv2.VideoCapture(video_file)

sobel_threshold = 50  # Початковий поріг для Sobel
print("Playing video from file with Sobel edge detection.")
print("Press: 1 = low threshold, 2 = medium, 3 = high, q = next")

while cap_file.isOpened():
    ret, frame = cap_file.read()
    if not ret:
        break

    key = cv2.waitKey(25) & 0xFF

    if key == ord('1'):         # Застосування 
        sobel_threshold = 30
        print("Low threshold")
    elif key == ord('2'):
        sobel_threshold = 70
        print("Medium threshold")
    elif key == ord('3'):
        sobel_threshold = 120
        print("High threshold")
    elif key == ord('q'):
        break

    edge_frame = apply_sobel(frame, sobel_threshold)
    cv2.imshow('Video from file - Sobel edges', edge_frame)

cap_file.release()
cv2.destroyAllWindows()

# Робота з вебкамерою 
cap_cam = cv2.VideoCapture(0)

if not cap_cam.isOpened():
    print("Failed to connect to the camera")
    exit()

frame_width = int(cap_cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap_cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('webcam_output_sobel.mp4', fourcc, 20.0, (frame_width, frame_height), isColor=False)

recording = False
image_count = 0
sobel_threshold = 70  # Початковий поріг для Sobel

print("Webcam started with Sobel edge detection.")
print("Press: 1/2/3 = threshold, r = record, s = save image, q = quit")

while True:
    ret, frame = cap_cam.read()
    if not ret:
        print("Failed to read frame")
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        sobel_threshold = 30
        print("Low threshold (camera)")
    elif key == ord('2'):
        sobel_threshold = 70
        print("Medium threshold (camera)")
    elif key == ord('3'):
        sobel_threshold = 120
        print("High threshold (camera)")
    elif key == ord('r'):
        recording = not recording
        print("Recording started." if recording else "Recording paused.")
    elif key == ord('s'):
        filename = f'captured_sobel_{image_count}.jpg'
        edge = apply_sobel(frame, sobel_threshold)
        cv2.imwrite(filename, edge)
        print(f"Saved {filename}")
        image_count += 1
    elif key == ord('q'):
        print("Exiting...")
        break

    # Застосовуємо фільтр 
    edge_frame = apply_sobel(frame, sobel_threshold)

    if recording:
        out.write(edge_frame)  # Записуємо чорно-біле зображення з межами

    cv2.imshow('Video from camera - Sobel edges', edge_frame)

cap_cam.release()
out.release()
cv2.destroyAllWindows()
