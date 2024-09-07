
from re import fullmatch

f=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\RegularExpressions\\domain.txt","r")

pattern="[\\w\\W]+\\.com"

for gmail in f:

    domain=gmail.rstrip("\n")

    matcher=fullmatch(pattern,domain)

    if matcher!=None:

        print(domain)
