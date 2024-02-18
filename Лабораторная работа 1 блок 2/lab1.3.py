import doctest
class Substance_concentration:
    """
    Абстрактный класс, описывающий объект концентрации вещества в стакане.
    """

    def __int__(self,substance_level: float, water_level: float):

        """
        Создание и подготовка к работе объекта концентрации вещества в стакане.

        :param substance_level: Количество вещества в стакане
        :param water_level: количество воды в стакане

        Пример:
        >>> kol_substance_in_stakan = Substance_concentration(22.7, 3.04)
        """

        if not isinstance(substance_level, (int, float)) or substance_level < 0:
            raise  ValueError("Количество вещества должно быть положительным числом")
        self.substance_level: float = substance_level

        if not isinstance(water_level, (int, float)) or water_level < 0:
            raise  ValueError("Количество воды должно быть положительным числом")
        self.water_level: float = water_level

    def add_element(self, substance_rate: float) -> None:
        """
        Метод описывающий добавление нового элемента в вещество, для повищения концентрации

        :param substance_rate: Скорость смещивания нового элемента с веществом

        Пример:
        >>> kol_substance_in_stakan.add_element(0.2)
        """

        ...
    def add_water(self, water_rate: float) -> None:
        """
        Метод описывающий добавление воды в стакан.

        :param water_rate: Скорость смещивания воды с раствором

        Пример:
        >>> kol_substance_in_stakan.add_water(0.01)
        """
        ...
if __name__ == "__main__":
    doctest.testmod()

