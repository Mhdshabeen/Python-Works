

# valdate mobile number with country code mandratory

# mobile numbers only start with 6,7,8,9


from re import fullmatch

number=input("Enter mobile num:> ")

pattern="(91)\\s?[6-9]\\d{9}"

matcher=fullmatch(pattern,number)

print('valid' if matcher!=None else "invalid")