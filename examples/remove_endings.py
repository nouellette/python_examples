import re

pattern = r'\b(\w+)(ing|ed|ly)\b'

def func(match):
    word, suffix = match.groups()
    return word

text = "He was running swiftly and he jumped excitedly."
print(re.sub(pattern, func, text))