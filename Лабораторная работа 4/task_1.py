class Vehicle:
    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
        brand (str): Марка транспортного средства.
        model (str): Модель транспортного средства.
        year (int): Год выпуска.
        mileage (float): Пробег в километрах.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float = 0.0):
        """
        Конструктор базового класса Vehicle.

        Аргументы:
            brand (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска.
            mileage (float): Пробег в километрах (по умолчанию 0.0).
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f"{self.brand} {self.model} ({self.year}), пробег: {self.mileage} км"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление транспортного средства."""
        return f"Vehicle(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, mileage={self.mileage!r})"

    def drive(self, distance: float) -> None:
        """
        Увеличивает пробег транспортного средства на заданное расстояние.

        Аргументы:
            distance (float): Расстояние в километрах.
        """
        self.mileage += distance
        print(f"Пробег увеличен на {distance} км. Текущий пробег: {self.mileage} км.")


class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.

    Атрибуты:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска.
        mileage (float): Пробег в километрах.
        num_doors (int): Количество дверей.
    """

    def __init__(self, brand: str, model: str, year: int, num_doors: int, mileage: float = 0.0):
        """
        Конструктор дочернего класса Car.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска.
            num_doors (int): Количество дверей.
            mileage (float): Пробег в километрах (по умолчанию 0.0).
        """
        super().__init__(brand, model, year, mileage)
        self.num_doors = num_doors

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{self.brand} {self.model} ({self.year}), {self.num_doors} дверей, пробег: {self.mileage} км"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление легкового автомобиля."""
        return f"Car(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, num_doors={self.num_doors!r}, mileage={self.mileage!r})"

    def honk(self) -> None:
        """Издает звук сигнала."""
        print("Би-бип!")

    def drive(self, distance: float) -> None:
        """
        Перегруженный метод для увеличения пробега.
        Добавляет проверку на максимальное расстояние за одну поездку.

        Аргументы:
            distance (float): Расстояние в километрах.
        """
        if distance > 1000:
            print("Ошибка: расстояние за одну поездку не может превышать 1000 км.")
        else:
            super().drive(distance)


class Truck(Vehicle):
    """
    Дочерний класс для грузовых автомобилей.

    Атрибуты:
        brand (str): Марка грузовика.
        model (str): Модель грузовика.
        year (int): Год выпуска.
        mileage (float): Пробег в километрах.
        max_load (float): Максимальная грузоподъемность в тоннах.
    """

    def __init__(self, brand: str, model: str, year: int, max_load: float, mileage: float = 0.0):
        """
        Конструктор дочернего класса Truck.

        Аргументы:
            brand (str): Марка грузовика.
            model (str): Модель грузовика.
            year (int): Год выпуска.
            max_load (float): Максимальная грузоподъемность в тоннах.
            mileage (float): Пробег в километрах (по умолчанию 0.0).
        """
        super().__init__(brand, model, year, mileage)
        self.max_load = max_load

    def __str__(self) -> str:
        """Возвращает строковое представление грузового автомобиля."""
        return f"{self.brand} {self.model} ({self.year}), грузоподъемность: {self.max_load} т, пробег: {self.mileage} км"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление грузового автомобиля."""
        return f"Truck(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, max_load={self.max_load!r}, mileage={self.mileage!r})"

    def load_cargo(self, weight: float) -> None:
        """
        Загружает груз в грузовик.

        Аргументы:
            weight (float): Вес груза в тоннах.
        """
        if weight > self.max_load:
            print(f"Ошибка: грузоподъемность превышена. Максимальная грузоподъемность: {self.max_load} т.")
        else:
            print(f"Груз весом {weight} т успешно загружен.")

    def drive(self, distance: float) -> None:
        """
        Перегруженный метод для увеличения пробега.
        Добавляет проверку на минимальное расстояние для грузовиков.

        Аргументы:
            distance (float): Расстояние в километрах.
        """
        if distance < 10:
            print("Ошибка: грузовики не могут ездить на расстояния менее 10 км.")
        else:
            super().drive(distance)


