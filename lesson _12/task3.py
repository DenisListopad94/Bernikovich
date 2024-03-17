import re

phone_numbers = ["8123456789", "91234567890", "7123456789", "91234567"]

for number in phone_numbers:
    if re.match(r"^[89]\d{9}$", number):
        print(f"Номер {number} корректен")
    else:
        print(f"Номер {number} некорректен")