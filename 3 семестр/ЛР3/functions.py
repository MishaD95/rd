# functions.py
import numpy as np
import math


def power_a3(a):
    """Піднесення числа до куба"""
    return a ** 3


def power_a3_for_list(list_of_a):
    """Піднесення всіх чисел зі списку до куба"""
    return [power_a3(a) for a in list_of_a]


def process_matrix(filename):
    """
    Зчитування матриці з файлу, підрахунок параметрів і виконання операцій над матрицею.
    Повертає суму K-го рядка, добуток K-го рядка і змінену матрицю.
    """
    M = N = K = 0
    try:
        with open(filename, 'r') as f:
            # Зчитуємо параметри
            param_line = f.readline().split()
            M, N, K = map(int, param_line)

            if K < 1 or K > M:
                raise ValueError("Номер рядка K повинен бути в діапазоні від 1 до M.")

            # Зчитуємо матрицю
            matrix = np.loadtxt(filename, skiprows=1, max_rows=M)
    except Exception as e:
        print(f"Помилка при зчитуванні файлу: {e}")
        return None, None, None

    # Обчислення
    sum_k = np.sum(matrix[K - 1, :])
    prod_k = np.prod(matrix[K - 1, :])
    changed_matrix = matrix - np.ones((M, N))

    return sum_k, prod_k, changed_matrix
