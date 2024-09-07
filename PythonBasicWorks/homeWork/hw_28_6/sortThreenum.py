#read three num from user and print in sorted order


num1=int(input("Enter num1 :>"))

num2=int(input("Enter num2 :>"))

num3=int(input("Enter num3 :>"))

# if num1<=num2 and num2<=num3:

#     print(f"{num1} , {num2} , {num3}")

# elif num1<=num3 and num3<=num2:

#     print(f"{num1} , {num3} , {num2}")
    
# if num2<=num1 and num1<=num3:

#     print(f"{num2} , {num1} , {num3}")

# elif num2<=num3 and num3<=num1:

#     print(f"{num2} , {num3} , {num1}")

# if num3<=num1 and num1<=num2:

#     print(f"{num3} , {num1} , {num2}")

# elif num3<=num2 and num2<=num1:

#     print(f"{num3} , {num2} , {num1}")



#logic 2


if num1>num2 and num1>num3:

    if num2>num3:

        print(num1,num2,num3)

    else:
        print(num1,num3,num2)

elif num2>num1 and num2>num3:

    if num1>num3:

        print(num2,num1,num3)

    else:

        print(num2,num3,num1)

elif num3>num1 and num3>num2:

    if num1>num2:

        print(num3,num1,num2)

    else:

        print(num3,num2,num1)

        