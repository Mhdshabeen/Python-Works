# Write a pgm to check the given number is a harshad number or not

num=int(input("Enter num:> "))

temp=num

sum_num=0


while num>0:

    digit=num%10
    
    sum_num=sum_num+digit
    
    num=num//10

print(True if temp%sum_num==0 else False)
