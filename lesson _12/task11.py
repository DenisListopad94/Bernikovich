import re

# Текст, в котором требуется найти HTML теги
html_text = "<html><head><title>Заголовок</title></head><body><h1>Пример страницы</h1><p>Это абзац текста.</p></body></html>"

# Регулярное выражение для поиска HTML тегов
html_tags_pattern = re.compile(r'<[^>]+>')

# Используем findall для поиска всех HTML тегов в тексте
html_tags_found = html_tags_pattern.findall(html_text)

# Выводим найденные HTML теги
for tag in html_tags_found:
    print(tag)