# main.py
from functions import power_a3_for_list, process_matrix

def task1():
    """Задача 1: обчислення кубів чисел зі списку."""
    try:
        in_num = int(input("Введіть кількість елементів: "))
        in_data = [int(input(f"{i+1}-й елемент: ")) for i in range(in_num)]
        print("Числа, піднесені до куба:", power_a3_for_list(in_data))
    except ValueError:
        print("Помилка: введіть правильне ціле число.")

def task2():
    """Задача 2: обробка матриці."""
    filename = input("Введіть назву файлу з матрицею: ")
    sum_k, prod_k, changed_matrix = process_matrix(filename)
    if sum_k is not None:
        print(f"Сума K-го рядка: {sum_k}")
        print(f"Добуток K-го рядка: {prod_k}")
        print(f"Змінена матриця:\n{changed_matrix}")

def main():
    """Головний цикл вибору задач."""
    while True:
        print("\nВиберіть задачу:")
        print("1. Піднести числа до куба")
        print("2. Обробити матрицю")
        print("3. Вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            print("Вихід...")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
