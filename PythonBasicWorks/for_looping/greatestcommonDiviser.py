# write a program to get the greatest common divisor of 2 numbers

# eg:- GCD(12,24):- 1,2,3,4,6,12 = 12
# GCD(10,20):- 1,2,5,10 = 10
# GCD(14,26):- 1,2


num1=int(input("Enter num1:> "))


num2=int(input("Enter num2:> "))

gcd=0

for i in range(1,num1+1):

    if num1%i==0 and num2%i==0:

        gcd=i

print(f"GCD({num1},{num2})= {gcd}")

