# write a prgm to print the sum of cube of digits


num=int(input("Enter num:> "))

sum=0



while num!=0:

    digit=num%10

    cube=digit**3

    sum=sum+cube
    
    num=num//10

print(sum)

