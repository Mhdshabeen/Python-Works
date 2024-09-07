# print the factorial of the given nummber

num=int(input("Enter number to find factorial:> "))

total=1

for i in range(1,num+1):

    total=total*i

print(f"{num}! = {total}")

