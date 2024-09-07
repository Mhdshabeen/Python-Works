# First character: Uppercase alphabet
# Next two characters: Numbers (first digit between 1-9, second digit between 0-9)
# Optional single space
# Next four characters: Numbers (0-9)
# Last character: Number (1-9)

from re import fullmatch

passport_num=input("Enter passport num:> ")

pattern="[A-Z][1-9][\\d][\\s]?[\\d]{4}[1-9]"

matcher=fullmatch(pattern,passport_num)

print("valid " if matcher!=None else "invalid")