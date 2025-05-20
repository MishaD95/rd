import cv2  # Підключаємо бібліотеку OpenCV
import numpy as np  # Для роботи з масивами (потрібно для контрасту)

def apply_new_filter(frame, filter_mode):
    """Застосовуємо нові кольорові перетворення"""
    if filter_mode == 'yuv':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)  # Перетворення у YUV
    elif filter_mode == 'contrast':
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)  # Перетворюємо у LAB
        l, a, b = cv2.split(lab)  # Розділяємо канали
        l = cv2.equalizeHist(l)  # Покращуємо контраст на L-каналі
        enhanced = cv2.merge((l, a, b))  # Об’єднуємо канали назад
        return cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)  # Назад у BGR
    return frame  # Без змін (original)

# Налаштування
video_file = 'video.mp4'
filter_mode = 'original'
recording = False
image_count = 0

# Відео з файлу
cap_file = cv2.VideoCapture(video_file)

print("Playing video from file with new filters.")
print("Press: y = YUV, c = contrast, o = original, q = next")

while cap_file.isOpened():
    ret, frame = cap_file.read()
    if not ret:
        break

    key = cv2.waitKey(25) & 0xFF

    # Перемикання нових фільтрів
    if key == ord('y'):
        filter_mode = 'yuv'
    elif key == ord('c'):
        filter_mode = 'contrast'
    elif key == ord('o'):
        filter_mode = 'original'
    elif key == ord('q'):
        break

    filtered_frame = apply_new_filter(frame.copy(), filter_mode)

    cv2.imshow('Video from file', filtered_frame)

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
out = cv2.VideoWriter('webcam_output.mp4', fourcc, 20.0, (frame_width, frame_height))

print("Webcam started.")
print("Press: y = YUV, c = contrast, o = original")
print("        r = record, s = save image, q = quit")

while True:
    ret, frame = cap_cam.read()
    if not ret:
        break

    key = cv2.waitKey(1) & 0xFF

    # Перемикання фільтрів
    if key == ord('y'):
        filter_mode = 'yuv'
    elif key == ord('c'):
        filter_mode = 'contrast'
    elif key == ord('o'):
        filter_mode = 'original'

    # Перемикач запису
    elif key == ord('r'):
        recording = not recording
        print("Recording started." if recording else "Recording paused.")

    # Збереження зображення
    elif key == ord('s'):
        filename = f'captured_image_{image_count}.jpg'
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        image_count += 1

    elif key == ord('q'):
        break

    # Застосування фільтра
    display_frame = apply_new_filter(frame.copy(), filter_mode)

    # Показ "REC", якщо запис увімкнено
    if recording:
        out.write(frame)
        cv2.putText(display_frame, "REC", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Video from camera', display_frame)

cap_cam.release()
out.release()
cv2.destroyAllWindows()
