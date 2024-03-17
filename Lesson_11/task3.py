class Alive:
    def __init__(self, age, meal):
        self.age = age
        self.meal = meal

    def eat(self):
        pass

    def distance(self):
        if self.age >= 10 or self.meal <= 0:
            return False
        else:
            return True


class Fox(Alive):
    def eat(self, rabbit):
        rabbit.meal -= 1


class Rabbit(Alive):
    def eat(self, plant):
        Plant.meal -= 1

    def distance(self):
        pass


class Plant(Alive):
    def eat(self):
        pass

Fox = Fox(5, 10)
Rabbit = Rabbit(3, 5)
Plant = Plant(2, 20)

Fox.eat(Rabbit)
Rabbit.eat(Plant)

print(Fox.distance())  # Выводит True
print(Rabbit.distance())  # Выводит True
print(Plant.distance())  # Выводит True