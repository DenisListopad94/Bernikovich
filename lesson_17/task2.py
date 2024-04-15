# lesson17 task2
from django.contrib.sites import requests

url = 'https://newsapi.org/'

# Отправка GET запроса к серверу
response = requests.get('https://newsapi.org/')

# Проверка статуса ответа
if response.status_code == 200:
    # Вывод информации о экземпляре
    print("Информация об экземпляре:")
    print(response.json())  # Предполагается, что сервер возвращает данные в формате JSON
else:
    print("Не удалось получить информацию. Статус код:", response.status_code)