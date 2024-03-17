
import re

s = "The cat sat on the mat and the other cat chased the mouse"
matches = re.findall(r'\b\w*cat\w*\b', s)

for match in matches:
    print(match)