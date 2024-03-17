import re

input_string = "Это строка с числами: 42 и -17, а также 3.14"
numbers = re.findall(r'-?\d+\.?\d*', input_string)

for number in numbers:
    number_float = float(number)
    print(number_float)
    print(-number_float)