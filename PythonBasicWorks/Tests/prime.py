# write a program to print the iven number is a prime or not

num=int(input("Enter the num:> "))

prime=True

for i in range(2,num):

    if num%i==0:

        prime=False

print(F"{num} is prime" if prime==True else f"{num} is not prime")
