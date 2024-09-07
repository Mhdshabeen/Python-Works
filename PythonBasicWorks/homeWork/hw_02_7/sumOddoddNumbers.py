# write a prgm to print sum of all odd numbers from start limit to end limit

start=int(input("Enter start limit:> "))

end=int(input("Enter end limit:> "))

total=0

while start<=end:

    if start%2!=0:

        total=total+start

    start=start+1

print(f"sum of numbers = {total}")
