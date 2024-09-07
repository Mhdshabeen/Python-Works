# WAP to swap the numbers in given pattern

# arr=[1,2,3,4,5,6,7]
#odd_pos=[2,4,6]
#revese=[6,4,2]

#final result=[1,6,3,4,5,2,7]


arr=[1,2,3,4,5,6,7,8,9,10,11]

# new_arr=arr.copy()

# odd_pos=[arr[i] for i in range(0,len(arr)) if i%2!=0]

# reverse_odd_pos=odd_pos[::-1] # 


left=1

length=len(arr)-1

if length%2!=0:

    right=length

else:

    right=length-1

while(left<right):

    arr[left],arr[right]=arr[right],arr[left]

    left+=2

    right-=2

print(arr)










        