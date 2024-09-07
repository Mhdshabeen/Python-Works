# read a number from user
# print fizz if only divisible by 3

# print buzz if only divisible by 5

# print kuzz if divisible by 7

# print buzzkuzz if divisible by 5 and 7

# print fizzkuzz if divisible by 3 and 7

# print fizzbuzzkuzz if divisible by 3, 5, and 7

# print fizzbuzz if divisible by both 3 and 5



num=int(input("Enter number :> "))

result=""

if num%3==0:

    result=result+"fizz"

if num%5==0:
    
    result=result+"buzz"

if num%7==0:

    result=result+"kuzz"

print(result)


