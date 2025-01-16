from Point_13 import Point_13
import matplotlib.pyplot as plt

def save_points_to_file(points, filename="points.txt"):
    """
    Зберігає список точок у файл.
    :param points: Список точок
    :param filename: Ім'я файлу
    """
    with open(filename, "w") as f:
        for i, point in enumerate(points, start=1):
            f.write(f"{i}: {point.x}; {point.y}\n")


def task():
    """Реалізація задачі варіанту 13"""
    # Створення трьох точок
    point1 = Point_13(10, 20)
    point2 = Point_13(-30, 40)
    point3 = Point_13(50, -70)

    # Обчислення відстані між першою та другою точками
    distance = point1.distance_to(point2)
    print(f"Відстань між точкою 1 {point1} і точкою 2 {point2}: {distance:.2f}")

    # Переміщення третьої точки на 40 одиниць вгору
    point3.move(0, 40)
    print(f"Точка 3 після переміщення: {point3}")

    # Візуалізація точок до і після змін
    points_before = [point1, point2, Point_13(50, -70)]
    points_after = [point1, point2, point3]

    plt.figure(figsize=(10, 5))

    # До змін
    plt.subplot(1, 2, 1)
    for point in points_before:
        plt.scatter(point.x, point.y, label=f"{point}")
    plt.title("До змін")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid()
    plt.legend()

    # Після змін
    plt.subplot(1, 2, 2)
    for point in points_after:
        plt.scatter(point.x, point.y, label=f"{point}")
    plt.title("Після змін")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid()
    plt.legend()

    plt.show()

    # Збереження точок у файл
    save_points_to_file(points_after)
    print("Координати точок збережено у файл 'points.txt'.")


if __name__ == "__main__":
    task()
