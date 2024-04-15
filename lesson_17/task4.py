import requests


def get_news_titles(api_url, params):
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        # Предполагая, что заголовки новостей находятся в поле 'titles' в JSON-ответе
        titles = [news['title'] for news in data['news']]
        return titles
    else:
        print("Failed to retrieve data from API")
        return None


# Пример использования
api_url = "https://example.com/api/news"
params = {"category": "business"}  # Параметры запроса, например, категория новостей

news_titles = get_news_titles(api_url, params)
if news_titles:
    for title in news_titles:
        print(title)  # Вывод заголовков новостей
