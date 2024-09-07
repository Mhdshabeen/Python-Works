# write a python program to find the hcf

num1=int(input("Enter num1:> "))

num2=int(input("Enter num2:> "))

smallest=min([num1,num2])

print(smallest)

hcf=0

for i in range(1,smallest+1):

    if num1%i==0 and num2%i==0:

        hcf=i

print(hcf)
 

