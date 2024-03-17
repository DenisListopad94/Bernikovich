import random


class TransportAgency:
    def __init__(self):
        self.branches = ["Город1", "Город2", "Город3"]  # Пример филиалов
        self.transport_types = {
            "автомобильный": {"стоимость": 10, "скорость": 60},
            "железнодорожный": {"стоимость": 5, "скорость": 40},
            "воздушный": {"стоимость": 20, "скорость": 200}
        }
        self.orders = []

    def calculate_cost(self, weight, distance, transport_type):
        cost_per_unit_weight = self.transport_types[transport_type]["стоимость"]
        return cost_per_unit_weight * weight * distance

    def calculate_time(self, distance, transport_type):
        speed = self.transport_types[transport_type]["скорость"]
        return distance / speed

    def place_order(self, from_branch, to_branch, weight, transport_preference):
        distance = random.randint(100, 500)  # Пример расстояния между городами
        cost = self.calculate_cost(weight, distance, transport_preference)
        time = self.calculate_time(distance, transport_preference)

        order_details = {
            "откуда": from_branch,
            "куда": to_branch,
            "масса груза": weight,
            "вид транспорта": transport_preference,
            "стоимость доставки": cost,
            "время доставки (часы)": time
        }

        self.orders.append(order_details)

    def get_income_by_transport_type(self):
        income_by_transport = {"автомобильный": 0, "железнодорожный": 0, "воздушный": 0}

        for order in self.orders:
            income_by_transport[order["вид транспорта"]] += order["стоимость доставки"]

        return income_by_transport

    def get_average_delivery_time_by_transport_type(self, air=None, railway=None):
        delivery_times_by_transport = {"car": [],
                                       railway: [],
                                       air: []}

        for order in self.orders:
            delivery_times_by_transport[order["вид транспорта"]].append(order["время доставки (часы)"])

        average_delivery_times = {}
        for transport in delivery_times_by_transport:
            average_delivery_times[transport] = sum(delivery_times_by_transport[transport]) / len(
                delivery_times_by_transport[transport])

        return average_delivery_times


#пример использования:
agency = TransportAgency()
agency.place_order("Город1", "Город2", 1000, "железнодорожный")
agency.place_order("Город2", "Город3", 500, "воздушный")

print("Доход по видам транспорта:", agency.get_income_by_transport_type())
print("Среднее время доставки по видам транспрота:", agency.get_average_delivery_time_by_transport_type())