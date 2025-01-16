from lab3 import task1, task2 

def main_menu():
    """
    Меню для вибору задач.
    """
    while True:
        print("\nВиберіть задачу:")
        print("1. Обчислення периметра трикутників")
        print("2. Обробка матриці")
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
    main_menu()
