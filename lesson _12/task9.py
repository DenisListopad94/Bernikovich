import re

# Список строк для замены
strings = [
    "Привеееееет",
    "Ооооочень мнооого букв",
    "Буквы всюдуууууууууу"
]

# Функция для замены последовательности одинаковых букв на одну
def replace_multiple_letters(string):
    return re.sub(r'(\w)\1+', r'\1', string)

# Применяем замену ко всем строкам
result_strings = [replace_multiple_letters(string) for string in strings]

# Выводим результат
for result in result_strings:
    print(result)