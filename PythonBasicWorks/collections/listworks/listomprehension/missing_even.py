# sum of n even numbers=n*(n+1)

arr=[0,2,4,6,8]

n=len(arr)

sum_of_even=n*(n+1)

current_sum=sum(arr)

missing=sum_of_even-current_sum

print(missing)