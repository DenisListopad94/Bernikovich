import re

# Текст, в котором требуется найти URL
text = "Это пример текста с URL-адресами: http://www.example.com/path/to/page?a=1&b=2 и https://www.example.com"

# Регулярное выражение для поиска URL
url_pattern = re.compile(r'(https?://)?(www\.)?[\w\.-]+\.\w+(/\S*)?')

# Используем findall для поиска всех URL в тексте
urls_found = url_pattern.findall(text)

# Выводим найденные URL-адреса
for url_match in urls_found:
    url = ''.join(url_match)
    print(url)