import re

text = "Некоторые слова содержат букву 'b', а некоторые - нет"

words_with_b = re.findall(r'\b\w*b\w*\b', text)

print(words_with_b)