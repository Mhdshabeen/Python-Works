

# validate pancard number

# first 3 char are alpha

# 4th place PCAFHT

# 5th alpha (first name of the applican surname)

# 4 digits

# 1 alpha

from re import fullmatch

pan_num=input("Enter pan number:> ")

pattern="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]"

matcher=fullmatch(pattern,pan_num)

print("invalid" if matcher==None else "valid")

