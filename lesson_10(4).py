class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом - вместимость копилки
        self.capacity = capacity
        self.coins = 0  # при создании копилки, число монет в ней равно 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        return self.coins + v <= self.capacity

    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.coins += v