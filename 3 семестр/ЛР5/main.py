import tkinter as tk
from task1 import calculate_powers
from task2 import plot_results

def task1_menu():
    """
    Задача 1: Обчислення третього ступеня чисел.
    """
    print("Задача 1: Обчислення третього ступеня чисел.")
    try:
        numbers = [float(x) for x in input("Введіть числа через пробіл: ").split()]
        results = calculate_powers(numbers)
        print("Третій ступінь чисел:", results)
    except ValueError:
        print("Помилка: введіть лише числові значення.")


def task2_menu():
    """
    Задача 2: Побудова графіка y[k].
    """
    print("Задача 2: Побудова графіка.")
    try:
        U = float(input("Введіть U: "))
        T = float(input("Введіть T: "))
        K = float(input("Введіть K: "))
        T0 = float(input("Введіть T0: "))
        n_steps = int(input("Введіть кількість кроків: "))
        plot_results(U, T, K, T0, n_steps)
        print("Графік збережено у файлі image.png")
    except ValueError:
        print("Помилка: введіть коректні дані.")


def main_menu():
    """
    Головне меню програми.
    """
    root = tk.Tk()  # Ініціалізація графічного вікна
    root.title("lab5_2-322-v13-Dikhtiarenko-Misha")  

    while True:
        print("\nВиберіть задачу:")
        print("1. Обчислення третього ступеня чисел")
        print("2. Побудова графіка y[k]")
        print("3. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            task1_menu()
        elif choice == "2":
            task2_menu()
        elif choice == "3":
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    root.mainloop()


if __name__ == "__main__":
    main_menu()
