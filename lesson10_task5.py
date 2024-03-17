class Fraction:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1

    def get_input(self):
        self.numerator = int(input("Введите числитель: "))
        self.denominator = int(input("Введите знаменатель: "))

    def display_fraction(self):
        print(f"{self.numerator}/{self.denominator}")

    def add_fraction(self, other_fraction):
        result_numerator = (self.numerator * other_fraction.denominator) + (other_fraction.numerator * self.denominator)
        result_denominator = self.denominator * other_fraction.denominator
        print(f"Сумма дробей: {result_numerator}/{result_denominator}")

    def simplify_fraction(self):
        common_divisor = self.gcd(self.numerator, self.denominator)
        if common_divisor != 1:
            self.numerator //= common_divisor
            self.denominator //= common_divisor
            print(f"Упрощенная дробь: {self.numerator}/{self.denominator}")

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a