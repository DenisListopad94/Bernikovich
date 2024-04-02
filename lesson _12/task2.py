import re

strings = ["zzz", "abzcdefzgh", "xyz123z456"]

for string in strings:
    if re.search(r'z...z', string):
        print(string)
