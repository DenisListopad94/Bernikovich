import re
# Ваша строка
text = "Сегодняшняя дата 28-02-2022"

# Регулярное выражение для поиска даты в формате dd-mm-yyyy
date_pattern = r'\b\d{2}-\d{2}-\d{4}\b'

# Находим все совпадения с помощью регулярного выражения
dates = re.findall(date_pattern, text)

# Печатаем найденные даты
for date in dates:
    print(date)