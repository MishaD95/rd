# -*- coding: utf-8 -*-
from task1 import PillowProcessor
from task2 import OpenCVProcessor
import sys
sys.path.append("D:\\Pa")
22

def safe_input(prompt):
    """
    Безпечний ввід тексту з обробкою UnicodeDecodeError.
    """
    try:
        return input(prompt)
    except UnicodeDecodeError:
        print("Помилка з введенням тексту. Будь ласка, введіть текст повторно.")
        sys.exit(1)

def main():
    print("Програма запущена. Введіть вибір.")  # Повідомлення про запуск програми
    while True:
        print("\nВиберіть задачу:")
        print("1. Завдання 1: Робота з Pillow")
        print("2. Завдання 2: Робота з OpenCV")
        print("3. Вийти")
        choice = safe_input("Ваш вибір: ")  # Використання safe_input
        print(f"Введення завершено. Обрано завдання: {choice}")  # Відображення вибору

        if choice == "1":
            file_path = safe_input("Введіть шлях до зображення: ")
            print(f"Ви ввели шлях: {file_path}")  # Вивід шляху для перевірки
            try:
                processor = PillowProcessor(file_path)
                processor.display_info()
                processor.create_thumbnail()
                processor.save_image("output_pillow.png")
                print("Зображення збережено як output_pillow.png")
            except Exception as e:
                print(f"Помилка: {e}")
        elif choice == "2":
            file_path = safe_input("Введіть шлях до зображення: ")
            print(f"Ви ввели шлях: {file_path}")  # Вивід шляху для перевірки
            try:
                processor = OpenCVProcessor(file_path)
                processor.projective_transform()
                processor.change_color_space()
                processor.display_image()
                processor.save_image("output_opencv.png")
                print("Зображення збережено як output_opencv.png")
            except Exception as e:
                print(f"Помилка: {e}")
        elif choice == "3":
            print("Завершення програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
