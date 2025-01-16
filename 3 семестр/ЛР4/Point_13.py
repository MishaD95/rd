import math

class Point_13:
    """Клас для опису точки на площині"""
    # Змінна класу для підрахунку кількості створених екземплярів
    instances_count = 0

    def __init__(self, x=0, y=0):
        """
        Ініціалізує точку з координатами x та y.
        Якщо координати не у межах [-100, 100], встановлює їх у 0.
        """
        self._x = x if -100 <= x <= 100 else 0
        self._y = y if -100 <= y <= 100 else 0
        Point_13.instances_count += 1

    def __del__(self):
        """Деструктор, що повідомляє про видалення екземпляра"""
        Point_13.instances_count -= 1
        print(f"Точка ({self._x}, {self._y}) видалена.")

    @property
    def x(self):
        """Геттер для координати x"""
        return self._x

    @x.setter
    def x(self, value):
        """Сеттер для координати x"""
        self._x = value if -100 <= value <= 100 else 0

    @property
    def y(self):
        """Геттер для координати y"""
        return self._y

    @y.setter
    def y(self, value):
        """Сеттер для координати y"""
        self._y = value if -100 <= value <= 100 else 0

    @classmethod
    def get_instances_count(cls):
        """Повертає кількість створених екземплярів"""
        return cls.instances_count

    def move(self, dx, dy):
        """Зсуває координати точки на dx по x і dy по y"""
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """Обчислює відстань до іншої точки"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        """Повертає рядкове представлення точки"""
        return f"({self.x}, {self.y})"
