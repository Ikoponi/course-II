"""Пример реализации наследования в предметной области "Автомобили"."""

from __future__ import annotations


class Vehicle:
    """Базовый класс для описания транспортного средства.

    Attributes:
        brand: Марка автомобиля.
        model: Модель автомобиля.
        year: Год выпуска.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """Инициализирует базовые данные транспортного средства.

        Args:
            brand: Марка автомобиля.
            model: Модель автомобиля.
            year: Год выпуска автомобиля.
        """
        self.brand: str = brand
        self.model: str = model
        self.year: int = year

    def __str__(self) -> str:
        """Возвращает строку для пользователя."""
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """Возвращает строку для разработчика."""
        return (
            f"{self.__class__.__name__}(brand={self.brand!r}, "
            f"model={self.model!r}, year={self.year!r})"
        )

    def get_category(self) -> str:
        """Возвращает категорию транспортного средства.

        Returns:
            Категория транспортного средства.
        """
        return "Транспортное средство"

    def calculate_annual_tax(self) -> float:
        """Вычисляет базовый годовой налог.

        Returns:
            Базовая сумма налога.
        """
        return 5000.0


class Truck(Vehicle):
    """Дочерний класс для грузового автомобиля.

    Наследует поведение класса Vehicle и расширяет его
    специфичными для грузовика атрибутами.
    """

    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        cargo_capacity_tons: float,
        vin_code: str,
    ) -> None:
        """Инициализирует грузовой автомобиль.

        Args:
            brand: Марка автомобиля.
            model: Модель автомобиля.
            year: Год выпуска.
            cargo_capacity_tons: Грузоподъемность в тоннах.
            vin_code: Идентификационный номер автомобиля (VIN).
        """
        super().__init__(brand, model, year)
        self.cargo_capacity_tons: float = cargo_capacity_tons
        # Инкапсуляция: VIN сделан непубличным, так как это чувствительный идентификатор.
        self.__vin_code: str = vin_code

    def __str__(self) -> str:
        """Возвращает строковое представление грузовика для пользователя."""
        return (
            f"{self.brand} {self.model} ({self.year}), "
            f"грузоподъемность: {self.cargo_capacity_tons} т"
        )

    def __repr__(self) -> str:
        """Возвращает строку представления грузовика для разработчика."""
        return (
            f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, "
            f"year={self.year!r}, cargo_capacity_tons={self.cargo_capacity_tons!r}, "
            f"vin_code={'***hidden***'!r})"
        )

    def get_category(self) -> str:
        """Возвращает категорию транспортного средства.

        Returns:
            Категория транспортного средства.
        """
        return "Грузовой автомобиль"

    def calculate_annual_tax(self) -> float:
        """Вычисляет годовой налог для грузовика.

        Причина перегрузки:
            Для грузовых автомобилей налог зависит от грузоподъемности.
            Базовая логика Vehicle.calculate_annual_tax не учитывает
            этот параметр, поэтому метод перегружен.

        Returns:
            Сумма годового налога для грузовика.
        """
        base_tax: float = super().calculate_annual_tax()
        extra_tax: float = self.cargo_capacity_tons * 1200.0
        return base_tax + extra_tax

    def get_masked_vin(self) -> str:
        """Возвращает маскированный VIN-код.

        Returns:
            Маскированная версия VIN-кода.
        """
        if len(self.__vin_code) < 4:
            return "***"
        return f"{'*' * (len(self.__vin_code) - 4)}{self.__vin_code[-4:]}"


def main() -> None:
    """Демонстрация работы классов Vehicle и Truck."""
    truck: Truck = Truck(
        brand="Volvo",
        model="FH16",
        year=2022,
        cargo_capacity_tons=18.5,
        vin_code="YV2RT60A7LA123456",
    )

    print(str(truck))
    print(repr(truck))
    print(f"Категория: {truck.get_category()}")
    print(f"Годовой налог: {truck.calculate_annual_tax()}")
    print(f"VIN: {truck.get_masked_vin()}")


if __name__ == "__main__":
    main()