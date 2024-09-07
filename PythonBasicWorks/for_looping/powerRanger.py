# write a program to find the power ranger of num
# eg:- 2=24 [2+22]
#3=369 [3+33+333]
#4=  [4+44+444+4444]


num=int(input("Enter the number:> "))

pattern=0 #3,33,33

total=0 #3+33+333

for i in range(1,num+1):#1,2,3

    pattern=pattern*10+num

    total=total+pattern

print(total)



