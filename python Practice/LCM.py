# write a prgm to find the LCM

num1=int(input("Enter num1"))

num2=int(input("Enter num2 "))

lcm=0

for i in range(1,num1*num2):

    if i%num1==0 and i%num2==0:

        lcm=i

        break

print(lcm)