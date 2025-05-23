import cv2
import numpy as np

# КЛАС ДЛЯ ОБРОБКИ ВІДЕО
class VideoProcessor:
    def __init__(self, source):
        self.source = source                      # Джерело відео: файл або камера
        self.threshold = 70                       # Початковий поріг для Sobel
        self.kernel_size = 3                      # Початковий розмір маски для фільтра НЧ
        self.cap = None                           # Об'єкт захоплення відео

    def open_source(self):
        self.cap = cv2.VideoCapture(self.source)  # Відкриття відео
        if not self.cap.isOpened():
            print("Cannot open video source")
            return False
        return True

    # === РЕЖИМИ ОБРОБКИ КАДРУ ===
    def shift_frame(self, frame):
        h, w = frame.shape[:2]
        M = np.float32([[1, 0, 100], [0, 1, 0]])   # Матриця зсуву праворуч на 100 пікселів
        return cv2.warpAffine(frame, M, (w, h))

    def sobel_edges(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        magnitude = cv2.magnitude(sobelx, sobely)
        _, binary = cv2.threshold(magnitude, self.threshold, 255, cv2.THRESH_BINARY)
        return np.uint8(binary)

    def yuv_contrast(self, frame):
        yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)     # Перетворення в YUV
        yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])     # Підвищення контрасту Y-каналу
        return cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)       # Назад у BGR

    def low_pass_filter(self, frame):
        return cv2.blur(frame, (self.kernel_size, self.kernel_size))  # Згладжування

    # ОСНОВНИЙ ЦИКЛ ОБРОБКИ
    def process(self):
        while True:
            print("\nSelect processing mode:")
            print("1 - Horizontal Shift")
            print("2 - Sobel Edges (-/+ threshold)")
            print("3 - YUV + Contrast")
            print("4 - Low-Pass Filter (1/2/3 kernel)")
            print("m - Return to effect menu")
            print("q - Quit")
            mode = input("Enter choice: ")

            if mode == 'q':
                break

            if not self.open_source():
                break

            while True:
                ret, frame = self.cap.read()
                if not ret:
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue

                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    self.cap.release()
                    cv2.destroyAllWindows()
                    return
                elif key == ord('m'):
                    print("Returning to effect menu...")
                    self.cap.release()
                    cv2.destroyAllWindows()
                    break

                # Керування параметрами під час перегляду
                elif mode == '2':
                    if key == ord('-') and self.threshold > 10:
                        self.threshold -= 10
                        print(f"Sobel threshold: {self.threshold}")
                    elif key == ord('=') or key == ord('+'):
                        if self.threshold < 150:
                            self.threshold += 10
                            print(f"Sobel threshold: {self.threshold}")
                elif mode == '4':
                    if key == ord('1'):
                        self.kernel_size = 3
                        print("Low-pass kernel: 3x3")
                    elif key == ord('2'):
                        self.kernel_size = 5
                        print("Low-pass kernel: 5x5")
                    elif key == ord('3'):
                        self.kernel_size = 9
                        print("Low-pass kernel: 9x9")

                # Застосування обраного режиму
                if mode == '1':
                    processed = self.shift_frame(frame)
                elif mode == '2':
                    processed = self.sobel_edges(frame)
                elif mode == '3':
                    processed = self.yuv_contrast(frame)
                elif mode == '4':
                    processed = self.low_pass_filter(frame)
                else:
                    processed = frame

                cv2.imshow("Processed Video", processed)

            self.cap.release()
            cv2.destroyAllWindows()

# ВИБІР ДЖЕРЕЛА / ВИХІД
def main():
    while True:
        print("\nChoose video source:")
        print("1 - File (video.mp4)")
        print("2 - Webcam")
        print("q - Quit")
        choice = input("Enter 1, 2 or q: ")

        if choice == '1':
            vp = VideoProcessor('video.mp4')   # Обробка відеофайлу
            vp.process()
        elif choice == '2':
            vp = VideoProcessor(0)             # Обробка з вебкамери
            vp.process()
        elif choice == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

# ЗАПУСК ПРОГРАМИ
if __name__ == '__main__':
    main()
