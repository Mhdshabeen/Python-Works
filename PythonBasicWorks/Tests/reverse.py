# write a program to reverse num

num=int(input("enter number:> "))

num_count=len(str(num))

reverse=""

for i in range(1,num_count+1):

    digit=num%10

    reverse=reverse+str(digit)

    num=num//10

print(int(reverse))

