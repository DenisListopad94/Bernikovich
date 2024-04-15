import requests

def create_new_post(api_url, post_data):
    response = requests.post(api_url, json=post_data)
    if response.status_code == 201:
        print("New post created successfully!")
        return response.json()  # Возвращает ответ сервера в формате JSON
    else:
        print("Failed to create new post.")
        return None

# Пример использования
api_url = "https://restcountries.com//api/posts"  # Замените на конкретный URL вашего API
post_data = {
    "title": "Новый пост",
    "content": "Содержание нового поста",
    "author": "Имя автора"
}

response_data = create_new_post(api_url, post_data)
if response_data:
    print("Response from server:", response_data)

