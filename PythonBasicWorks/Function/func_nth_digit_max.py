# write a prgm to create function that return number with nth digit max

# input 2 parameters

# eg:> nth_digit_max(123,991) return 123 becoz 3 is the nth max digit


def nth_digit_max(num1,num2):

    return num1 if num1%10 > num2%10 else num2

print(nth_digit_max(135,456))


# def nth_digit_max(num1,num2):

#     cout_num1=len(str(num1))

#     count_num2=len(str(num2))

#     for i in range(1,2):

#         digit1=num1%10

#         break
#     for j in range(1,2):

#         digit2=num2%10

#         break

#     if (digit1>digit2):

#         result=num1

#     else:

#         result=num2

#     return result



