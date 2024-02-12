if __name__ == "__main__":
    # Write your solution here
    # - Okay, boss!
    pass
class Crypto:
    # класс для криптовалюты

    def __init__(self, name: str, price: float, market_cap: float):
        """
            name: название криптовалюты
            price: цена криптовалюты
            market_cap: капитализация криптовалюты
        """
        self.name = name
        self._price = None
        self._market_cap = None
        self.price = price
        self.market_cap = market_cap

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("цена  должна быть больше нуля")
        self._price = value

    @property
    def market_cap(self) -> float:
        return self._market_cap

    @market_cap.setter
    def market_cap(self, value: float):
        if value <= 0:
            raise ValueError("капитализация должна быть больше нуля")
        self._market_cap = value


    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.name}, Цена: {self.price}, " \
               f"Капитализация: {self.market_cap}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(Название={self.name!r}, " \
               f"Цена={self.price}, Капитализация={self.market_cap})"


class Bitcoin(Crypto):
    """
    В классе Bitcoin унаследуем метод __str__ от базы  (Crypto),
    перегрузим метод __repr__, добавив к нему атрибут max_supply
    """

    def __init__(self, price: float, market_cap: float, max_supply: int):
        #max_supply: Максимальное количество монет
        super().__init__("Bitcoin", price, market_cap)
        self.max_supply = max_supply

    def mine_block(self, reward: float) -> float:
        """reward: Вознаграждение за майнинг блока

        Returns:
            Новая  капитализация битка """
        self.market_cap += reward
        return self.market_cap


class Ethereum(Crypto):
"""
В классе Ethereum унаследуем метод __str__,
перегрузим метод __repr__, добавив к нему  gas_limit
"""
    def __init__(self, price: float, market_cap: float, gas_limit: int):
        #gas_limit: Предел газа для выполнения транзакций в сети Ethereum.
        super().__init__("Ethereum", price, market_cap)
        self.gas_limit = gas_limit

    def execute_transaction(self, gas_used: int) -> float:
        """ Метод для выполнения транзакции в сети эфира
        gas_used: Количество использованного газа

        Returns:
             Новая капитализация эфира """
        transaction_fee = gas_used * self.price
        self.market_cap -= transaction_fee
        return self.market_cap


# Проверка
bitcoin = Bitcoin(49000, 6464964, 25752434834)
ethereum = Ethereum(2000, 5757648964, 616168468434964634)

print(bitcoin)
print(ethereum)


bitcoin.mine_block(655.25)
ethereum.execute_transaction(200)

print(bitcoin)
print(ethereum)