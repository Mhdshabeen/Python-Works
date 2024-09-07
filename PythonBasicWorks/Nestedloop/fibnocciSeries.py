# write a prgm to print first 10 fibinocci series

# Eg:- 0 1 1 2 3 5 8 13 21

num=int(input("Enter num:> "))

previous=0

current=1

print(f"{previous} {current}",end=" ")

for i in range(1,num+1):

    next_num=previous+current

    print(f"{next_num}",end=" ")

    previous=current
    
    current=next_num

    # here we get 12 numbers including starting and previous

