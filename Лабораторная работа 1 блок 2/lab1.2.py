import doctest

class Meat_na_mangale:
    """
    Абстрактный класс, который описывает объект жарки шашлыка.
    """
    def __int__(self, kol_skewers: int, kg_meat: float):
        """
        Создание и подготовка к жарке шашлыка

        :param kol_skewers: Количество шампуров
        :param kg_meat: Общий вес мяса

        Пример:
        >>> shashlik = Meat_na_mangale(3,2.5)
        """

# условия для шампуров
        if not isinstance(kol_skewers, int) or kol_skewers <= 0:
            raise ValueError("Количество шампуров должно быть положительным целым числом")
        self.kol_skewers: int = kol_skewers

# условия для мяса
        if not isinstance(kg_meat, (int,float)) or kg_meat <=0:
            raise ValueError("Общий вес мяса должен быть положительным")
        self.kg_meat: float = kg_meat

# добавление шампура
    def add_new_skewers(self, new_skewers: int) -> None:
        """
        Метод, которы добавляет ещё шампур
        :param new_skewers: Дополнительный шампур
        :return: None
        """

# добавление мяса
    def add_meat(self, plus_kg:float) -> None:
        """
        Метод добавления ещё мяса
        :param plus_kg: Добавление мяса
        :return: None
        """

if __name__ == "__main__":
    doctest.testmod()

