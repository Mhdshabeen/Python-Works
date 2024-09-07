

# validate gmailid

# username should bo of min 6-30 len

from re import fullmatch

gemil_id=input("Enter email id:>")

pattern="\\w[\\w\\._]*@gmail.com"

matcher=fullmatch(pattern,gemil_id)

print("invalid" if matcher==None else "valid")

#shabeensahzz313@gmail.com