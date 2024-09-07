# write a program to print the sum of digits

#note: do not consider prime numbers while adding


num=int(input("Enter number:> "))

count=len(str(num))

sum=0

adding="0"

for i in range(1,count+1):

    digit=num%10

    prime=True

    for j in range(2,digit):

        if(digit%j==0):

            prime=False

            break
        
    if prime==False:

        sum=sum+digit

        adding=adding+"+"+str(digit)    

    num=num//10

print(f"{adding} = {sum}")
