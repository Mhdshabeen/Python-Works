# WAP to get the count of odd and even numbers in a list

list=[2,5,7,9,3,5,1,4,8,13,25,32,57,84,92,17,18]

count_even=0

count_odd=0

for i in list:

    if i%2==0:

        count_even=count_even+1

    else:

        count_odd=count_odd+1

print(f"count of even= {count_even}\n" f"count of odd= {count_odd}")

