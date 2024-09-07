from re import fullmatch

f=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\RegularExpressions\\registration.txt","r")

pattern="(KL)(\\s)?(?!00)[0-9]{2}(\\s)?[A-z]{1,2}\\s?(?!0000)[0-9]{4}"

count=0

for regnum in f:

    registration=regnum.rstrip("\n")

    matcher=fullmatch(pattern,registration)

    if matcher!=None:

        count+=1

        print(registration)

print(count)