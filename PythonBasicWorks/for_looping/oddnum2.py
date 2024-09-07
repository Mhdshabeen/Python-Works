# write a prgm to print all odd num from start limit to end limit

# read start limit and end limit from user

start_limit=int(input("Enter start limit:> "))

end_limit=int(input("Enter the end limit:> "))

for i in range(start_limit,end_limit):

    if(i%2!=0):

        print(i)