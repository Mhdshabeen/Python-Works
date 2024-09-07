# write a program to check the given number is a palindrome or not


number=int(input("Enter number:> "))

store=number

result=0


while number!=0:

    digit=number%10

    result=result*10+digit

    number=number//10

    
    
print(result)

print("palindrome" if result==store else "not palindrome")





#logic 2
# num=int(input("Enter number:>"))

# store=num

# reverse=""

# while num!=0:

#     digit=num%10
#     reverse=reverse+str(digit)
#     num=num//10

# sting_to_int=int(reverse)

# if sting_to_int==store:

#     print("palindrome")

# else:
    
#     print("not palindrome")





