import cv2  # Підключаємо бібліотеку OpenCV

def apply_geometry(frame, mode):
    """Функція для геометричних перетворень"""
    if mode == 'flip':
        return cv2.flip(frame, 1)  # Віддзеркалення по горизонталі
    elif mode == 'rotate':
        return cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)  # Поворот за годинниковою стрілкою
    elif mode == 'zoom':
        h, w = frame.shape[:2]
        center = (w // 2, h // 2)
        cropped = frame[center[1] - 100:center[1] + 100, center[0] - 100:center[0] + 100]  # По центру
        return cv2.resize(cropped, (w, h))  # Розтягуємо 
    return frame  # Повертаємо без змін, якщо режим — 'original'

# Робота з вебкамерою
cap = cv2.VideoCapture(0)  # Ініціалізуємо вебкамеру
if not cap.isOpened():  # Перевірка чи камера доступна
    print("Failed to open webcam")
    exit()

# Налаштування
geom_mode = 'original'  # Початковий режим — без трансформацій

print("Webcam started.")
print("Press: f = flip, r = rotate, z = zoom, o = original, q = quit")

while True:
    ret, frame = cap.read()  # Зчитуємо кадр з камери
    if not ret:
        print("Failed to read frame")  # Якщо кадр не прочитався
        break

    key = cv2.waitKey(1) & 0xFF  # Чекаємо натиснення клавіші

    # Керування геометричними режимами
    if key == ord('f'):
        geom_mode = 'flip'  # Встановлюємо режим "віддзеркалення"
    elif key == ord('r'):
        geom_mode = 'rotate'  # Поворот
    elif key == ord('z'):
        geom_mode = 'zoom'  # Встановлюємо режим "масштабування"
    elif key == ord('o'):
        geom_mode = 'original'  # Повертаємось до оригіналу
    elif key == ord('q'):
        print("Exiting...")
        break

    transformed_frame = apply_geometry(frame, geom_mode)  # Застосовуємо геометричну трансформацію

    cv2.imshow('Geometric Transformations', transformed_frame)  # Виводимо кадр

cap.release()  
cv2.destroyAllWindows()  # Закриваємо всі вікна
