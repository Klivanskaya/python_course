import string
st = dir(string.ascii_lowercase)
print("Атрибуты модуля string по алфавиту в обратном порядке: " , st[:: - 1])
