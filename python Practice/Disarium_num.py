# write a prgm to check weather the given number is a diserium number or not

num=int(input("Enter num:> "))

temp=num

len_num=len(str(num))

sum=0

for i in range(len_num,0,-1):

    digit=num%10

    sum=sum+digit**i

    num=num//10

print(True if temp==sum else False)