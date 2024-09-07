

# validate kerala karnataka and tamilnadu vehicle numbers

from re import fullmatch

vehiclenumber="50BN1234"

pattern="(KL|TN|KA)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,vehiclenumber)

print("invalid" if matcher==None else "valid")