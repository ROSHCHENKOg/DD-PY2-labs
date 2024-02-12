
class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    # для доступа к имени книги
    @property
    def name(self):
        return self._name

    # для доступа к автору книги
    @property
    def author(self):
        return self._author

    # была ошибка, не работала, нажал ПКМ и он сам исправил и написал сэттеры. приятно:))
    # ВОСсТАНИЕ МАШИН СКОРО!!! ыаыаыаыа ЫААЫАыаыаыаы
    @author.setter
    def author(self, value):
        self._author = value

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"



class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        # Вызываем родителя, чтобы иниц. название и автора
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    # для установки количества страниц с проверками
    @pages.setter
    def pages(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Количество страниц должно быть целым")
        if value <= 0:
            raise ValueError("Количество страниц не может быть меньше нуля")
        self._pages = value


    def __str__(self):
        # Переопределяем метод для бумажной книги
        return f"Бумажная {super().__str__()}. Количество страниц: {self.pages} стр."


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
            return self._duration

    @duration.setter
    def duration(self, value):
        # для установки  продолжительности с проверками
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше нуля")
        self._duration = value

    def __str__(self):
        return f"Аудио {super().__str__()}. Продолжительность: {self.duration} часов"




# Проверка
book = Book("Название книжки", "Кто-то это написал")
paper_book = PaperBook("Название книжки", "Кто-то это написал", 1224152573523434345)
audio_book = AudioBook("Название книжки", "Кто-то это написал", 606515616156)

print(book)
print(paper_book)  # Вывод информации о бумажной книге
print(audio_book)  # Вывод информации об аудиокниге


"""
В задании говорилось:

" подумайте когда методы __str__ и __repr__ могут быть унаследованы,
а когда перегружены в дочерних классах. И исправьте это"

Как я понимаю тут не одно решение и надеюсь то, что накалякал сверху корректно :)
"""
