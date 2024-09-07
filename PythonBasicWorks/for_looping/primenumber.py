# write a program to check weather the given number is prime number or not

#logic 1


num=int(input("Enter number:> "))

is_prime=True

for i in range(2,num):

    if(num%i==0):

        is_prime=False

        break

print(f"{num} is prime" if is_prime==True else f"{num} not a prime")

