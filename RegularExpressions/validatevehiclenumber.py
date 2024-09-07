

# keral vehicle number validation

# first start with KL

# second 2 digits

# Third one or 2 alphabets

# followed by 1-4 numbers

from re import fullmatch

text="KL00AB2345"

pattern="(KL)(-)?[1-9][0-9](-)?[A-Z]{1,2}(-)?[0-9]{4}"

matcher=fullmatch(pattern,text)

print("invalid" if matcher==None else "valid")