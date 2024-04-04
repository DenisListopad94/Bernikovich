import requests


def create_new_post("api_url", post_data):
    global response
    try:
        response = requests.post(api_url, json=post_data)
        response.raise_for_status()  # Проверка на ошибки HTTP
        if response.status_code == 201:
            print("New post created successfully!")
            return response.json()  # Возвращает ответ сервера в формате JSON
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("Ошибка 404: Ресурс не найден.")
        elif response.status_code == 500:
            print("Ошибка 500: Внутренняя ошибка сервера.")
        else:
            print(f"Ошибка HTTP: {http_err}")
    except Exception as err:
        print(f"Произошла ошибка: {err}")
    return None


# Пример использования
api_url = "https://randomuser.me//api/posts"  # Замените на конкретный URL вашего API
post_data = {
    "title": "Новый пост",
    "content": "Содержание нового поста",
    "author": "Имя автора"
}

response_data = create_new_post(api_url, post_data)
if response_data:
    print("Response from server:", response_data)
