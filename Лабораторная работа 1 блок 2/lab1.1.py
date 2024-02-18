# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Apple_tree:
    def __init__(self, sort_apple:str, quantity_apple:int, garden_apple: float):
        """
        Создание и подготовка к работе объекта "Яблоня"

        :param sort_apple: Сорт яблони
        :param quantity_apple: количество  созревших яблонь
        :param garden_apple: площадь,занимаема в саду сада

        Примеры:
        >>> apple = Apple_tree ('Gala',5,0.5) #инициализация экземплеря класса
        """
# условия для ввода сорта яблонь
        if not isinstance(sort_apple, (str)):
            raise TypeError ("Сорт яблони должен быть типа string")
        if sort_apple ==' ':
            raise ValueError("Сорт не может быть пустой строкой")
        self.sort_apple = sort_apple

# условия для ввода количества яблоневых деревьев
        if not isinstance(quantity_apple, (int)):
            raise TypeError("Количество яблонь должно быть int")
        if quantity_apple < 0:
            raise ValueError ("Количество яблонь не может быть отрицательным числом")
        self.quantity_apple = quantity_apple

 # условия для ввода плошади, занимаемой деревьми в саду
        if not isinstance(garden_apple,(int, float)) or garden_apple <=0:
            raise  TypeError ("Площадь должна быть положительным числом")
        self.garden_apple: float = garden_apple

# добавление площади
    def add_new_garden(self, new_garden: float) -> None:
        """
        Метод для добавления площади сада
        :param new_garden: Дополнительная площадь

        Пример:
        >>> apple = Apple_tree ('Gala',5,0.5)
        >>> apple.add_new_garden(5.0)
        """

# сбор урожая
    def harvest_apple (self, harvest_count: int) -> None:
        """
        Метод сбора яблок.

        :param harvest_count: Количество собираемых яблок

        Пример:
        >>> apple = Apple_tree ('Gala',5,0.5)
        >>> apple.harvest_apple(15)
        """

if __name__ == "__main__":
    doctest.testmod()
