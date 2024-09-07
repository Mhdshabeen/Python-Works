# write program to create function is_prime(number) to return true if the number is prime and false if no prime



def is_prime(num):

    result=True

    for i in range(2,num):

        if num%i==0:

            result=False

            break
    
    return result


print(is_prime(6))