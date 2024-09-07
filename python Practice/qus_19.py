# Write a prgm to check weather the given number is a amsstrong or not

num=int(input("Enter number to check:>"))

orginal_num=num

total=0

length=len(str(num))

while(num!=0):

    digit=num%10

    total=total+digit**length

    num=num//10

if total==orginal_num:

    print(True)

else:
    print(False)
