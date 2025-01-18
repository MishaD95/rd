from PIL import Image

class PillowProcessor:
    def __init__(self, file_path):
        """
        Ініціалізація класу із завантаженням зображення.
        """
        self.image = Image.open(file_path)
        self.file_path = file_path

    def display_info(self):
        """
        Відображення інформації про зображення.
        """
        print(f"Формат: {self.image.format}")
        print(f"Розмір: {self.image.size}")
        print(f"Режим: {self.image.mode}")

    def create_thumbnail(self):
        """
        Створення зменшеної копії зображення.
        """
        thumbnail_size = (100, 100)
        self.image.thumbnail(thumbnail_size)
        print("Створено зменшену копію зображення.")

    def save_image(self, new_path):
        """
        Збереження зображення у файл.
        """
        self.image.save(new_path)
