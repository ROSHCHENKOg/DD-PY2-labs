# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class dog:
    def __init__(self, breed: str, years_old: int):
        """
              Создание и подготовка к работе объекта "собака"

              :breed: Порода собаки
              :years_old: Возраст собаки

              Примеры:
              >>> Ralph = dog ("Немецкая Овчарка", 4)  # инициализация экземпляра класса
        """
        if not isinstance(breed, str):
            raise TypeError('Порода собаки не может быть числом')
        self.breed = breed

        if years_old <= 0:
            raise ValueError('Собака не может быть моложе 0 лет')
        if not isinstance(years_old, int):
            raise TypeError('Возраст необходимо записать числом')
        self.years_old = years_old

    def eat(self, food: str):
        """
            Собака собиарется поесть

            :food: Еда, которую собака собирается съесть

            :return: Сообщение о том, что собака съела {food}

            Примеры:
            >>> Ralph = dog ("Немецкая Овчарка", 10)
            >>> Ralph.eat("колбаса, которая упала со стола")

            #Хватит есть всякую ерунду!!! Мы тебе дорогой корм покупаем...# (Это микро прикол, это не к заданию!)
        """
        ...

    def count_of_balls (self, balls: int):
        """
        Количество мячиков у собаки

        :balls: Количество мячиков

        :return: Сообщение о кол-ве мячиков у собакена

        Примеры:
            >>> Ralph = dog ("Немецкая Овчарка", 10)
            >>> Ralph.count_of_balls(4)
            """
        ...


class CalendarEvent:
    """
        Класс, описывающий событие в календаре

        :title: Заголовок события
        :day_of_event: Дата события
        :time: Продолжительность события

        Примеры:
        >>> Christmas = CalendarEvent("Рождество", 25.12, 2)  # инициализация экземпляра класса
    """

    def __init__(self, title: str, day_of_event: float, time: int):
        if not isinstance(title, str):
            raise TypeError('Заголовок события не может являться числом')
        self.title = title

        if not isinstance(day_of_event or time, float):
            raise TypeError('Дату и продолжительность необходимо записать числом')
        if day_of_event <= 0:
            raise ValueError('ДАта события не может быть меньше 0')
        if time <= 0:
            raise TypeError('Продолжительность события не может быть меньше 0')
        self.day_of_event = day_of_event
        self.time = time

    def meme(self):
        """
      Функция которая проверяет выпалает ли событие на 3 сентября

      :return: "Я календарь переверну" #Если это 3 сентября, если нет, то ничего

      Примеры:
      >>> Christmas = CalendarEvent("Рождество", 25.12, 2)
      >>> Christmas.meme()
          """
        ...

    def is_ongoing(self, current_day: float) -> bool:
        """
        Функция, которая позволит проверить, идет ли событие в данный момент

        :current_day: Текущая дата

        :return: bool: True, если событие сегодня, иначе False

        Примеры:
        >>> Christmas = CalendarEvent("Рождество", 25.12, 2)
        >>> Christmas.is_ongoing(12.12)
        """
        ...

class Cryptocurrency:
    """
    Класс, описывающий криптовалюту. #ААА КРипта хайп Дэб СПИННЕР ДЭБ

        :name: Название валюты
        :symbol: Символьный код (BTC, ETH)
        :price: цена криптовалюты
        :circulating_supply: Общее количество монет

        Примеры:
        >>> BTC = Cryptocurrency ('Bitcoin', 'BTC', 42000, 15151551561)
    """

    def __init__(self, name: str, symbol: str, price: float, circulating_supply: float):

        if not isinstance(name, str):
            raise TypeError('Название необходимо записать буквами')
        self.name = name
        if not isinstance(symbol, str):
            raise TypeError('Тикер необходимо записать буквами')
        self.symbol = symbol

        if price < 0 or circulating_supply < 0:
            raise ValueError("Цена и общее количество должны быть неотрицательными.")
        self.price = price
        self.circulating_supply = circulating_supply


    def update_price(self, new_price: float):
        """
        Обновить цену крипты

        :new_price: Новая цена криптовалюты

        Примеры:
        >>> BTC = Cryptocurrency ('Bitcoin', 'BTC', 42000, 15151551561)
        >>> BTC.update_price(42.500)
        """
        ...

    def buy_coins(self, amount: float):
        """
        Купить крипту

        :amount: Количество монет которых купили

        :return: Было куплено N монет
        Примеры:
        >>> BTC = Cryptocurrency ('Bitcoin', 'BTC', 42000, 15151551561)
        >>> BTC.buy_coins(1)
        """
        ...



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()