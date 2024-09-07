# read three numbers from user num1, num2, num3

# print the second greatest number of three


num1=int(input("Enter num1 :> "))

num2=int(input("Enter num2 :> "))

num3=int(input("Enter num3 :> "))


# Logic 1 to get 2nd largest among three numbers

result=""

# assume that we have 3 numbers 1 , 2 and 3 if 1 want to be the second greatest then 1 should be greater than 2 and less than -
# 3 or 1 should be greater than 3 and less than 2 apply this for all numbers then we can find the second largest of 3

if num1>=num2 and num1<=num3:

    result=result+"num1 is second greatest"

elif num1>=num3 and num1<=num2:

    result=result+"num1 is second greatest"

if num2>num1 and num2<=num3:

    result=result+"num2 is second greatest"

elif num2>=num3 and num2<=num1:

    result=result+"num2 is second greatest"

if num3>=num1 and num3<=num2:

    result=result+"num3 is second largest"

elif num3>=num2 and num3<=num1:

    result=result+"num3 is second largest"

print(result)



#logic 2


# if num1>num2 and num1>num3:

#     if num2>num3:

#         print(f"second largest is num2 : {num2}")

#     else:
#         print(f"second largest is num3 : {num3}")

# elif num2>num1 and num2>num3:

#     if num1>num3:

#         print(f"second largest num1 : {num1}")

#     else:

#         print(f"second largest num3 : {num3}")

# elif num3>num1 and num3>num2:

#     if num1>num2:

#         print(f"second largest is num1: {num1}")

#     else:

#         print(f"second largest is num2 : {num2}")

        