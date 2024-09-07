# create a function is amstong-number(number) to return true if the number is amstrong and false if number is not amstrong


def is_amstrong_number(num):

    orginal=num

    num_count=len(str(num))

    sum=0

    result=False

    for i in range(1,num_count+1):

        digit=num%10

        exponent=digit**num_count

        sum=sum + exponent

        if orginal==sum:

            result=True

            break

        num=num//10

    return result

print(is_amstrong_number(375))


        


    
