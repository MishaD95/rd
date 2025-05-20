import cv2  # Підключаємо бібліотеку OpenCV

def apply_filter(frame, filter_mode):
    """Функція для застосування фільтра до кадру"""
    if filter_mode == 'grayscale':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif filter_mode == 'invert':
        return cv2.bitwise_not(frame)
    elif filter_mode == 'hsv':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    return frame  # original

# Налаштування
video_file = 'video.mp4'
filter_mode = 'original'
recording = False
image_count = 0

# Відео з файлу 
cap_file = cv2.VideoCapture(video_file)

print("Playing video from file with filters.")
print("Press: g = grayscale, i = invert, h = HSV, o = original, q = next")

while cap_file.isOpened():
    ret, frame = cap_file.read()
    if not ret:
        break

    key = cv2.waitKey(25) & 0xFF

    # Перемикання фільтрів
    if key == ord('g'):
        filter_mode = 'grayscale'
    elif key == ord('i'):
        filter_mode = 'invert'
    elif key == ord('h'):
        filter_mode = 'hsv'
    elif key == ord('o'):
        filter_mode = 'original'
    elif key == ord('q'):
        break

    filtered_frame = apply_filter(frame, filter_mode)

    # Показуємо результат
    cv2.imshow('Video from file', filtered_frame)

cap_file.release()
cv2.destroyAllWindows()

# Робота з вебкамерою 
cap_cam = cv2.VideoCapture(0)
if not cap_cam.isOpened():
    print("Failed to connect to the camera")
    exit()

# Отримуємо розміри кадру
frame_width = int(cap_cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap_cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Запис відео
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('webcam_output.mp4', fourcc, 20.0, (frame_width, frame_height))

print("Webcam started.")
print("Press: g/i/h/o = filter, r = record, s = save image, q = quit")

while True:
    ret, frame = cap_cam.read()
    if not ret:
        break

    key = cv2.waitKey(1) & 0xFF

    # Управління фільтрами
    if key == ord('g'):
        filter_mode = 'grayscale'
    elif key == ord('i'):
        filter_mode = 'invert'
    elif key == ord('h'):
        filter_mode = 'hsv'
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

    # Вихід
    elif key == ord('q'):
        break

    # Обробка фільтра
    display_frame = apply_filter(frame.copy(), filter_mode)

    # Якщо grayscale або hsv — конвертуємо в BGR для запису тексту
    if filter_mode in ['grayscale', 'hsv']:
        display_frame = cv2.cvtColor(display_frame, cv2.COLOR_GRAY2BGR) if filter_mode == 'grayscale' else cv2.cvtColor(display_frame, cv2.COLOR_HSV2BGR)

    # Показ індикатора запису
    if recording:
        out.write(frame)
        cv2.putText(display_frame, "REC", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Показ кадру
    cv2.imshow('Video from camera', display_frame)

cap_cam.release()
out.release()
cv2.destroyAllWindows()
