# write program to print the sum of digits in a number

num=int(input("Enter the number:> "))

sum=0

while num!=0:

    digit=num%10
    print(digit)
    sum=sum+digit
    num=num//10

print("sum=",sum)