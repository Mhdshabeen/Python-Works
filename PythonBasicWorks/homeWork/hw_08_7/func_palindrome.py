# create a function is_palindrome_number(num) to return true if the number is palindrome and false if the number is not


def is_palindrome_number(num):

    orginal=num

    reverse=""

    num_count=len(str(num))

    result=False

    for i in range(1,num_count+1):

        digit=num%10

        reverse=reverse+str(digit)

        if int(reverse)==orginal:

            result=True

            break

        num=num//10

    return result

print(is_palindrome_number(212))