# Write a progrm to find the factoriel using recursion



def factorial(n):
    if n==0:

        return 1
    else:
        return n*factorial(n-1)
    
num=int(input("Enter number:> "))


if num<0:

    print("factoriel is not definet for non negative integers")

else:
    result=factorial(num)
    print(f"The factorial of {num} is {result}")
