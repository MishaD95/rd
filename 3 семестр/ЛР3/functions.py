def sum_of_two_largest(a, b, c):
    """
    Знаходить суму двох найбільших чисел із трьох.
    :param a: Перше число
    :param b: Друге число
    :param c: Третє число
    :return: Сума двох найбільших чисел
    """
    return a + b + c - min(a, b, c)

def task1():
    """
    Введення трьох чисел і обчислення суми двох найбільших.
    """
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        c = float(input("Введіть третє число: "))
        result = sum_of_two_largest(a, b, c)
        print(f"Сума двох найбільших чисел: {result}")
    except ValueError:
        print("Помилка: введіть коректні числа.")


import math

def count_points_in_area(points, radius):
    """
    Рахує кількість точок, які потрапляють у задану область (31 варіант).
    :param points: Список точок [(x1, y1), (x2, y2), ...]
    :param radius: Радіус кола
    :return: Кількість точок у заданій області
    """
    count = 0
    for x, y in points:
        # Умови для попадання точки в жовту область (31 варіант)
        if x >= 0 and y >= 0 and (x**2 + y**2) <= radius**2:
            count += 1
    return count

def task2():
    """
    Введення координат точок і радіуса, перевірка попадання точок у задану область.
    """
    try:
        n = int(input("Введіть кількість точок: "))
        radius = float(input("Введіть радіус кола: "))
        points = []
        for i in range(n):
            x, y = map(float, input(f"Введіть координати точки {i+1} (x y): ").split())
            points.append((x, y))
        result = count_points_in_area(points, radius)
        print(f"Кількість точок у жовтій області: {result}")
    except ValueError:
        print("Помилка: введіть коректні значення.")


import math

def series_sum(x, epsilon, g):
    """
    Обчислює суму ряду ∑ (x^(3n)) / (2n + 1)!
    Умови завершення: |u_n| < ε або |u_n| > g
    :param x: Значення x
    :param epsilon: Малий параметр ε
    :param g: Граничне значення g
    :return: Сума ряду
    """
    n = 0
    term = x**(3 * n) / math.factorial(2 * n + 1)
    total_sum = term

    while abs(term) >= epsilon and abs(term) <= g:
        n += 1
        term = x**(3 * n) / math.factorial(2 * n + 1)
        total_sum += term

    return total_sum

def task3():
    """
    Введення параметрів ряду, обчислення його суми.
    """
    try:
        x = float(input("Введіть x: "))
        epsilon = float(input("Введіть ε (наприклад, 1e-5): "))
        g = float(input("Введіть g (наприклад, 1e5): "))
        result = series_sum(x, epsilon, g)
        print(f"Сума ряду: {result}")
    except ValueError:
        print("Помилка: введіть коректні числа.")

