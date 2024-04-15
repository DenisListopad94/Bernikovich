import requests

def get_sorted_data(api_url, params, sort_key):
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        sorted_data = sorted(data, key=lambda x: x.get(sort_key))
        return sorted_data
    else:
        print("Failed to retrieve data from API")

        return None

# Пример использования
api_url = "https://example.com/api/news"
params = {"category": "business"}  # Параметры запроса, например, категория новостей
sort_key = "published_at data"  # Признак, по которому будем сортировать данные, например, дата публикации

sorted_news = get_sorted_data(api_url, params, sort_key)
if sorted_news:
    for news_item in sorted_news:
        print(news_item)  # Вывод отсортированных новостей
# params категория новостей
# sort key дата публикации новости