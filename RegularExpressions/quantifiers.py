
from re import finditer

text="ab12xyz678#$pqr123cdef"

# pattern="[a-z]{3}" # check for consicutive three char

# write a pattern to identify the 3 cosicutive digits

# pattern="[0-9]{3}" # check for 3 consicutive numbers

# pattern="[c-h]|[t-z]" # check for char in between c-h or t-z

pattern="[a-z]{3}|[0-9]{3}" # check for 3 consicutive alphaobets or numbers

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())