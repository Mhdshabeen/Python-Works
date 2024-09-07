
num1=100

num2=200

# write a program to swap

# values befoe swapping num1=100 num2=200
# value after swapping num1=200 num2=100

print(f"value before swapping num1={num1} num2={num2}")

#logic

# 1 using temp variable

# temp=num1
# num1=num2
# num2=temp

#2 using addition

# num1=num1+num2 #num1= 100+200=300
# num2=num1-num2 #num2= 300-200= 100
# num1=num1-num2 #num1= 300-100=200


#3logic 

num1,num2=num2,num1

#4logic
print(f"value after swapping num1={num1} num2={num2}")
