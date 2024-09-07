

# variable Name

# first character must be lphabet from k-m

#second leter must be number divisible by 3

# followed by any number of alphabeets,numbers and @ 

from re import fullmatch

text=input("Enter name:")

pattern="[k-m][3,6,9][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,text)

print("valid" if matcher!=None else "Invalid")

