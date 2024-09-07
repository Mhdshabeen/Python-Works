# create a function is_fibinocci-number(num) to return true if the number is febinocci and false if not fibinocci

def is_fibinocci_number(num):

    previous=0

    current=1

    next=current+previous

    result=False

    while (next<=num):

        next=current+previous

        previous=current

        current=next

        if next==num:

            result=True

    return result


print(is_fibinocci_number(34))

