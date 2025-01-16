import math

def TriangleP(a, h):
    """
    Обчислює периметр рівнобедреного трикутника за основою a і висотою h.
    :param a: Основа трикутника
    :param h: Висота, проведена до основи
    :return: Периметр трикутника
    """
    # Знаходимо бічну сторону за теоремою Піфагора
    b = math.sqrt((a / 2) ** 2 + h ** 2)
    perimeter = a + 2 * b
    return perimeter

def task1():
    """
    Введення основи і висоти трикутника, обчислення периметрів.
    """
    try:
        n = 3  # Кількість трикутників
        for i in range(n):
            print(f"Трикутник {i + 1}:")
            a = float(input("Введіть основу (a): "))
            h = float(input("Введіть висоту (h): "))
            result = TriangleP(a, h)
            print(f"Периметр трикутника: {result:.2f}")
    except ValueError:
        print("Помилка: введіть коректні числові значення.")
        

import numpy as np

def process_matrix(file_path):
    """
    Обробляє матрицю:
    1. Рахує кількість елементів у кожному рядку, менших за середнє арифметичне.
    2. Обчислює обернену матрицю.
    :param file_path: Шлях до текстового файлу з матрицею
    :return: None
    """
    try:
        # Завантаження матриці з файлу
        matrix = np.loadtxt(file_path, delimiter=' ')
        print("Матриця:")
        print(matrix)

        # Кількість елементів у рядках, менших за середнє арифметичне
        for i, row in enumerate(matrix):
            mean_value = np.mean(row)
            count_less_than_mean = np.sum(row < mean_value)
            print(f"Рядок {i + 1}: середнє = {mean_value:.2f}, менших за середнє = {count_less_than_mean}")

        # Перевірка на квадратність матриці
        if matrix.shape[0] != matrix.shape[1]:
            print("\nОбернену матрицю знайти неможливо, оскільки матриця не квадратна.")
            return

        determinant = np.linalg.det(matrix)
        if determinant == 0:
            print("\nОбернену матрицю знайти неможливо, оскільки визначник дорівнює 0.")
            return

        # Обчислення оберненої матриці
        transposed_matrix = matrix.T
        inverse_matrix = transposed_matrix * determinant
        print("\nОбернена матриця:")
        print(inverse_matrix)

    except Exception as e:
        print(f"Помилка: {e}")

def task2():
    """
    Виклик обробки матриці з файлу.
    """
    file_path = input("Введіть шлях до файлу з матрицею: ")
    process_matrix(file_path)
