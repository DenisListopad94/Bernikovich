distance = 1000


class Plane:
    Plane = 'Самолет'

    @classmethod
    def cost_of_transportation(Plane, cost_of_transportation, distance):
        pass


print(f"Время перевозки самолетом: {Plane.cost_of_transportation(distance)} часов")
print(f"Стоимость перевозки самолетом: {Plane.cost_of_transportation(distance)}")


class Train:
    Train = 'Поезд'

    @classmethod
    def transportation_time(Train, cost_of_transportation, distance):
        pass

    @classmethod
    def cost_of_transportation(Train, distance):
        pass


print(f"Время перевозки поездом: {Train.transportation_time} часов")
print(f"Стоимость перевозки поездом: {Train.cost_of_transportation()}")


class Car:
    Car = 'Автомобиль'

    @classmethod
    def cost_of_transportation(Car):
        pass

    @classmethod
    def transportation_time(Car, distance):
        pass


print(f"Время перевозки автомобилем: {Car.transportation_time(distance)} часов")
print(f"Стоимость перевозки автомобилем: {Car.cost_of_transportation()}")