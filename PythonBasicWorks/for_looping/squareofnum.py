# write a program to print square of  all num from start limit ato end limit and find thir sum


start_limit=int(input("Enter start limit:> "))

end_limit=int(input("Enter the end limit:> "))

end_limit=end_limit+1

total=0

for i in range(start_limit,end_limit):

    square=i**2

    print(f"square of {i} = {square}")

    total=total+square

print(f"sum of squares= {total}")