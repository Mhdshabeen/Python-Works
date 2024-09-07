

# validate date 01-03-2021 0r 3/5/2030

from re import fullmatch

text="10/10-2021"

pattern="(0?[1-9]|1[0-9]|2[0-9]|3[0-1])(-|/)?(0?[1-9]|1[0-2])(-|/)?[0-9]{4}"

matcher=fullmatch(pattern,text)

print("invalid" if matcher==None else "valid")