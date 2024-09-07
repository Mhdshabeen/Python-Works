# read start limit and end limit from user and print all the odd number from start to end

start=int(input("Enter start_limit :> "))

end=int(input("Enter end_limit :> "))

while start<=end:

    if start%2!=0:

        print(start)

    start=start+1