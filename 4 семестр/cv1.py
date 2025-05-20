import cv2  # Підключаємо бібліотеку OpenCV

#  Відтворення відео з файлу 
video_file = 'video.mp4'
cap_file = cv2.VideoCapture(video_file)

print("Playing video from file...")
while cap_file.isOpened():
    ret, frame = cap_file.read()
    if not ret:
        break
    cv2.imshow('Video from file', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap_file.release()
cv2.destroyAllWindows()

#  Робота з вебкамерою 
cap_cam = cv2.VideoCapture(0)

if not cap_cam.isOpened():
    print("Failed to connect to the camera")
    exit()

# Отримуємо розміри кадру з камери
frame_width = int(cap_cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap_cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Налаштування для запису відео
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('webcam_output.mp4', fourcc, 20.0, (frame_width, frame_height))

recording = False  # Спочатку запис вимкнено
image_count = 0    # Лічильник збережених кадрів

print("Webcam started.")
print("Press 'r' to toggle recording, 's' to save image, 'q' to quit.")

while True:
    ret, frame = cap_cam.read()
    if not ret:
        print("Failed to read frame")
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):  # Перемикач запису
        recording = not recording  # Змінюємо значення True <-> False
        if recording:
            print("Recording started.")
        else:
            print("Recording paused.")

    elif key == ord('s'):  # Збереження зображення
        filename = f'captured_image_{image_count}.jpg'
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        image_count += 1

    elif key == ord('q'):  # Вихід
        print("Exiting...")
        break

    if recording:
        out.write(frame)  # Записуємо кадр, якщо активний запис

    # Відображення кадру з індикатором "REC", якщо запис активний
    display_frame = frame.copy()
    if recording:
        cv2.putText(display_frame, "REC", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Video from camera', display_frame)

# Завершення
cap_cam.release()
out.release()
cv2.destroyAllWindows()
