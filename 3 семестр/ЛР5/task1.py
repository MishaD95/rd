def PowerA3(a):
  """
  Обчислює третій ступінь числа A.
  :param a: число
  :return: A^3
  """
  return a ** 3


def calculate_powers(numbers):
  """
  Обчислює третій ступінь для списку чисел.
  :param numbers: список чисел
  :return: список третіх ступенів
  """
  return [PowerA3(num) for num in numbers]
