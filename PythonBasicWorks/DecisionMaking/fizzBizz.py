# read a number from user and 
# print fizz if number is divisible by 3
# print bizz is number is divisible by 5
# print fizzbizz if the number is divisible by 15


num=int(input("Enter the number > "))

if num%15 ==0:

    print("fizzbuzz")

elif num%5 ==0:

    print("buzzz")

elif num%3 ==0:

    print("fizz")

else:

    print("Not divisible by 3 , 5 or 15")

