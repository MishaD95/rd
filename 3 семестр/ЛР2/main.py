from functions import task1, task2, task3 

def main_menu():
  """
  Меню для вибору задач.
  """
  while True:
      print("\nВиберіть задачу:")
      print("1. Сума двох найбільших чисел")
      print("2. Кількість точок у заданій області")
      print("3. Дослідження ряду на збіжність")
      print("4. Вийти")
      choice = input("Ваш вибір: ")

      if choice == "1":
          task1()
      elif choice == "2":
          task2()
      elif choice == "3":
          task3()
      elif choice == "4":
          print("Вихід...")
          break
      else:
          print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
  main_menu()
