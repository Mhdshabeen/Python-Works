# sum of n numbers=> n(n+1)/2

# find missing positive integer number

arr=[0,1,2,3,4,5]

n=len(arr)

sum_of_n=n*(n+1)/2

current_sum=sum(arr)

missing_num=sum_of_n-current_sum

print(int(missing_num))



# logic 2

# pr=arr[0]

# curr=arr[1]

# for i in range(0,len(arr)):

#     missing=int()

#     diff=curr-pr

#     if diff<=1:

#         pr=curr

#         curr+=1

#     elif diff!=0:

#         missing=pr+1

#     else:

#         missing=curr+1

# print(missing)

    

    

