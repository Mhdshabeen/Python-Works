# write a program to print sum of even numbers for start limit to end limit

start_limit=int(input("Enter start limit:> "))

end_limit=int(input("Enter the en limit:> "))

total=0

for i in range(start_limit,end_limit):

    if(i%2==0):

        total=total+i

print(total)