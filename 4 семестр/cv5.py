import cv2  # Підключаємо бібліотеку OpenCV

def apply_low_pass_filter(frame, kernel_size):
    """Застосовуємо НЧ-фільтр (розмиття) з заданою маскою"""
    return cv2.blur(frame, (kernel_size, kernel_size))  # Просте згладжування (бокс-фільтр)

# Відео з файлу
video_file = 'video.mp4'
cap_file = cv2.VideoCapture(video_file)

kernel_size = 3  # Початковий розмір маски (3x3)

print("Playing video from file with low-pass filter.")
print("Press: 1 = 3x3, 2 = 5x5, 3 = 9x9 mask, q = next")

while cap_file.isOpened():
    ret, frame = cap_file.read()
    if not ret:
        break

    key = cv2.waitKey(25) & 0xFF

    if key == ord('1'):  # Перемикання
        kernel_size = 3
        print("Kernel size: 3x3")
    elif key == ord('2'):
        kernel_size = 5
        print("Kernel size: 5x5")
    elif key == ord('3'):
        kernel_size = 9
        print("Kernel size: 9x9")
    elif key == ord('q'):
        break

    filtered = apply_low_pass_filter(frame, kernel_size)  # Застосовуємо НЧ-фільтр
    cv2.imshow('Video from file - Low Pass Filter', filtered)  # Виводимо зображення

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
out = cv2.VideoWriter('webcam_output_lowpass.mp4', fourcc, 20.0, (frame_width, frame_height))

recording = False
image_count = 0

print("Webcam started with low-pass filter.")
print("Press: 1/2/3 = change filter size, r = record, s = save image, q = quit")

while True:
    ret, frame = cap_cam.read()
    if not ret:
        print("Failed to read frame")
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        kernel_size = 3
        print("Kernel size: 3x3 (camera)")
    elif key == ord('2'):
        kernel_size = 5
        print("Kernel size: 5x5 (camera)")
    elif key == ord('3'):
        kernel_size = 9
        print("Kernel size: 9x9 (camera)")
    elif key == ord('r'):
        recording = not recording
        print("Recording started." if recording else "Recording paused.")
    elif key == ord('s'):
        filename = f'captured_blur_{image_count}.jpg'
        filtered = apply_low_pass_filter(frame, kernel_size)
        cv2.imwrite(filename, filtered)
        print(f"Saved {filename}")
        image_count += 1
    elif key == ord('q'):
        break

    filtered = apply_low_pass_filter(frame, kernel_size)

    if recording:
        out.write(filtered)  # Записуємо відфільтроване відео
        cv2.putText(filtered, "REC", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Video from camera - Low Pass Filter', filtered)
 
 # Завершення
cap_cam.release()
out.release()
cv2.destroyAllWindows()
