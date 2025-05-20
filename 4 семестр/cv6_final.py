import cv2
import numpy as np

#  Функції обробки
def shift_frame(frame):
    h, w = frame.shape[:2]
    M = np.float32([[1, 0, 100], [0, 1, 0]])  # Зсув по X на 100 пікселів
    return cv2.warpAffine(frame, M, (w, h))

def sobel_edges(frame, threshold):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = cv2.magnitude(sobelx, sobely)
    _, binary = cv2.threshold(magnitude, threshold, 255, cv2.THRESH_BINARY)
    return np.uint8(binary)

def yuv_contrast(frame):
    yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
    return cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)

def low_pass_filter(frame, ksize):
    return cv2.blur(frame, (ksize, ksize))

#  Головна обробка/фільтри
def process_video(source):
    threshold = 70
    kernel_size = 3

    while True:
        print("\nSelect processing mode:")
        print("1 - Horizontal Shift")
        print("2 - Sobel Edges (Натисніть -/+ для зміни порогу)")
        print("3 - YUV + Contrast")
        print("4 - Low-Pass Filter (Натисніть 1/2/3 для зміни маски)")
        print("m - Return to effect menu")
        print("q - Quit")
        mode = input("Enter choice: ")

        if mode == 'q':
            break

        cap = cv2.VideoCapture(source)  # Відкриваємо заново відео
        if not cap.isOpened():
            print("Cannot reopen video source")
            break

        while True:
            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Повертаємось на початок
                continue

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return
            elif key == ord('m'):
                print("Returning to effect menu...")
                cv2.destroyAllWindows()
                cap.release()
                break
            elif mode == '2':
                if key == ord('-') and threshold > 10:
                    threshold -= 10
                    print(f"Sobel threshold: {threshold}")
                elif key == ord('=') or key == ord('+'):
                    if threshold < 150:
                        threshold += 10
                        print(f"Sobel threshold: {threshold}")
            elif mode == '4':
                if key == ord('1'):
                    kernel_size = 3
                    print("Low-pass kernel: 3x3")
                elif key == ord('2'):
                    kernel_size = 5
                    print("Low-pass kernel: 5x5")
                elif key == ord('3'):
                    kernel_size = 9
                    print("Low-pass kernel: 9x9")

            if mode == '1':
                processed = shift_frame(frame)
            elif mode == '2':
                processed = sobel_edges(frame, threshold)
            elif mode == '3':
                processed = yuv_contrast(frame)
            elif mode == '4':
                processed = low_pass_filter(frame, kernel_size)
            else:
                processed = frame

            cv2.imshow("Processed Video", processed)

        cap.release()
        cv2.destroyAllWindows()

#  Вибір джерела відео/вихід
def main():
    while True:
        print("\nChoose video source:")
        print("1 - File (video.mp4)")
        print("2 - Webcam")
        print("q - Quit")
        choice = input("Enter 1, 2 or q: ")

        if choice == '1':
            process_video('video.mp4')
        elif choice == '2':
            process_video(0)
        elif choice == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
