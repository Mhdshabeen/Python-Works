# read three number from user num1, num2, num3

# print largest among the three

num1=int(input("Enter num1 :> "))

num2=int(input("Enter num2 :> "))

num3=int(input("Enter num3 :> "))

result=""

if num1>=num2 and num1>=num3:

    result=result+"num1 is gratest"

elif num2>=num1 and num2>=num3:

    result=result+"num2 is greatest"

else:

    result=result+"num3 is gratest"

print(result)

