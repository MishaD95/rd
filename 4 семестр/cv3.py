import cv2  # Підключаємо OpenCV
import numpy as np  # Для створення матриці зсуву

def apply_shift(frame, apply, shift_value=100):
    """Застосовує горизонтальний зсув, якщо apply=True"""
    if not apply:
        return frame
    height, width = frame.shape[:2]
    M = np.float32([[1, 0, shift_value], [0, 1, 0]])  # Матриця зсуву праворуч
    return cv2.warpAffine(frame, M, (width, height))  # Застосування зсуву

#  Відео з файлу 
video_file = 'video.mp4'
cap_file = cv2.VideoCapture(video_file)

apply_shift_flag = False  # Початково зсув вимкнено

print("Playing video from file...")
print("Press 'x' to toggle shift, 'q' to proceed to webcam")

while cap_file.isOpened():
    ret, frame = cap_file.read()
    if not ret:
        break

    key = cv2.waitKey(25) & 0xFF

    if key == ord('x'): # Перемикання зсуву
        apply_shift_flag = not apply_shift_flag
        print("Shift ON (file)" if apply_shift_flag else "Shift OFF (file)")

    elif key == ord('q'):
        break

    shifted_frame = apply_shift(frame, apply_shift_flag)
    cv2.imshow('Video from file', shifted_frame)

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

recording = False
image_count = 0
apply_shift_flag = False  # Окремий зсув для камери

print("Webcam started.")
print("Press: r = record, s = save, x = toggle shift, q = quit")

while True:
    ret, frame = cap_cam.read()
    if not ret:
        print("Failed to read frame")
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        recording = not recording
        print("Recording started." if recording else "Recording paused.")

    elif key == ord('s'):
        filename = f'captured_image_{image_count}.jpg'
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        image_count += 1

    elif key == ord('x'):
        apply_shift_flag = not apply_shift_flag
        print("Shift ON (camera)" if apply_shift_flag else "Shift OFF (camera)")

    elif key == ord('q'):
        print("Exiting...")
        break

    # Застосовуємо зсув (якщо потрібно)
    display_frame = apply_shift(frame.copy(), apply_shift_flag)


    if recording:
        out.write(frame)
        cv2.putText(display_frame, "REC", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Video from camera', display_frame)

# Завершення 
cap_cam.release()
out.release()
cv2.destroyAllWindows()
