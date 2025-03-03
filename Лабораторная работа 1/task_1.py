# TODO Написать 3 класса с документацией и аннотацией типов
# TODO работоспособность экземпляров класса проверить с помощью doctest

import doctest

class Tree:
    def __init__(self, height: float, age: int, species: str):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах
        :param species: Вид дерева

        Примеры:
        >>> tree = Tree(10.5, 50, "Дуб")  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст дерева должен быть положительным числом")
        self.age = age

        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть типа str")
        self.species = species

    def grow(self, years: int) -> None:
        """
        Увеличение возраста дерева на заданное количество лет.

        :param years: Количество лет, на которое увеличивается возраст дерева
        :raise ValueError: Если количество лет отрицательное, то вызываем ошибку

        Примеры:
        >>> tree = Tree(10.5, 50, "Дуб")
        >>> tree.grow(10)
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть типа int")
        if years < 0:
            raise ValueError("Количество лет должно быть положительным числом")
        ...

    def get_height_in_meters(self) -> float:
        """
        Возвращает высоту дерева в метрах.

        :return: Высота дерева в метрах

        Примеры:
        >>> tree = Tree(10.5, 50, "Дуб")
        >>> tree.get_height_in_meters()
        10.5
        """
        return self.height


if __name__ == "__main__":
    doctest.testmod()


class Car:
    def __init__(self, brand: str, fuel_level: float, max_speed: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param fuel_level: Уровень топлива в баке (в литрах)
        :param max_speed: Максимальная скорость автомобиля (в км/ч)

        Примеры:
        >>> car = Car("Audi", 50.0, 200.0)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть типа str")
        self.brand = brand

        if not isinstance(fuel_level, (int, float)):
            raise TypeError("Уровень топлива должен быть типа int или float")
        if fuel_level < 0:
            raise ValueError("Уровень топлива не может быть отрицательным")
        self.fuel_level = fuel_level

        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть типа int или float")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        self.max_speed = max_speed

    def refuel(self, amount: float) -> None:
        """
        Заправка автомобиля.

        :param amount: Количество топлива для заправки (в литрах)
        :raise ValueError: Если количество топлива отрицательное, то вызываем ошибку

        Примеры:
        >>> car = Car("Audi", 50.0, 200.0)
        >>> car.refuel(20.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Количество топлива должно быть типа int или float")
        if amount < 0:
            raise ValueError("Количество топлива должно быть положительным числом")


    def drive(self, distance: float, speed: float) -> None:
        """
        Поездка на автомобиле.

        :param distance: Расстояние поездки (в километрах)
        :param speed: Скорость движения (в км/ч)
        :raise ValueError: Если скорость превышает максимальную или топлива недостаточно, то вызываем ошибку

        Примеры:
        >>> car = Car("Audi", 50.0, 200.0)
        >>> car.drive(100, 80)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if distance < 0:
            raise ValueError("Расстояние должно быть положительным числом")

        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость должна быть типа int или float")
        if speed < 0:
            raise ValueError("Скорость должна быть положительным числом")
        if speed > self.max_speed:
            raise ValueError("Скорость превышает максимальную скорость автомобиля")
        ...


if __name__ == "__main__":
    doctest.testmod()

    class Facebook:
        def __init__(self, username: str, friends_count: int):
            """
            Создание и подготовка к работе объекта "Facebook"

            :param username: Имя пользователя
            :param friends_count: Количество друзей

            Примеры:
            >>> fb = Facebook("user123", 100)  # инициализация экземпляра класса
            """
            if not isinstance(username, str):
                raise TypeError("Имя пользователя должно быть типа str")
            self.username = username

            if not isinstance(friends_count, int):
                raise TypeError("Количество друзей должно быть типа int")
            if friends_count < 0:
                raise ValueError("Количество друзей не может быть отрицательным числом")
            self.friends_count = friends_count

        def add_friend(self) -> None:
            """
            Добавление нового друга.

            Примеры:
            >>> fb = Facebook("user123", 100)
            >>> fb.add_friend()
            """
            ...

        def post_status(self, status: str) -> None:
            """
            Публикация нового статуса.

            :param status: Текст статуса

            Примеры:
            >>> fb = Facebook("user123", 100)
            >>> fb.post_status("Новый статус")
            """
            if not isinstance(status, str):
                raise TypeError("Статус должен быть типа str")
            ...


    if __name__ == "__main__":
        doctest.testmod()