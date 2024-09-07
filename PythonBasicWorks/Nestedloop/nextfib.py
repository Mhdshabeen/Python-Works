# print next fibinocci number

#14


number=int(input("Enter number:> "))

previous=0

current=1

next=previous+current

while (next<= number):

    next=previous+current

    previous=current

    current=next

    if next==number or number>next:

        fib=next+previous

        break

print(fib)