# write a prg to create a simple calculator

def add(num1,num2):

    return num1+num2

def sub(num1,num2):
    return num1 - num2

def division(num1,num2):
    return num1/num2

def multiply(num1,num2):
    return num1*num2

print("""Operations in calculator: \n 1.Add \n 2.sub \n 3.division \n 4.multipy""")

select=int(input("Select operation:> "))

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))

if select==1:
    print(add(num1,num2))

elif select==2:
    print(sub(num1,num2))

elif select==3:
    print(division(num1,num2))

elif select==4:
    print(multiply(num1,num2))

elif select>4:
    print("Invalid input")
