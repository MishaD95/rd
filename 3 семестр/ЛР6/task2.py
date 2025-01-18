import cv2
import numpy as np
import matplotlib.pyplot as plt

class OpenCVProcessor:
    def __init__(self, file_path):
        """
        Ініціалізація класу із завантаженням зображення.
        """
        self.image = cv2.imread(file_path)
        if self.image is None:
            raise ValueError("Не вдалося завантажити зображення. Перевірте шлях до файлу.")
        self.file_path = file_path

    def projective_transform(self):
        """
        Проективне перетворення (вертикальне).
        """
        rows, cols, ch = self.image.shape
        src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
        dst_points = np.float32([[0, 0], [cols - 1, 0], [cols // 4, rows - 1]])
        matrix = cv2.getAffineTransform(src_points, dst_points)
        self.image = cv2.warpAffine(self.image, matrix, (cols, rows))
        print("Проективне перетворення виконано.")

    def change_color_space(self):
        """
        Зміна кольорового простору на RGB.
        """
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        print("Зміна кольорового простору виконана.")

    def display_image(self):
        """
        Відображення зображення з використанням matplotlib.
        """
        plt.imshow(self.image)
        plt.axis('off')
        plt.show()

    def save_image(self, new_path):
        """
        Збереження зображення у файл.
        """
        print(f"Збереження зображення в {new_path}...")
        cv2.imwrite(new_path, cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR))
        print("Збережено.")
