# write a prgm to print sum of digits

#sample input = 5234= 5+2+3+4=14

#sample input = 1334= 3+3+4=10

#sample input= 1213 = 2+3=5

#do not cosider 1 when adding

num=int(input("Enter number:> "))

count=len(str(num))

sum=0

for i in range(1,count+1):

    digit=num%10

    if digit!=1:

        sum=sum+digit

    num=num//10

print(f"sum of the digits = {sum}")

