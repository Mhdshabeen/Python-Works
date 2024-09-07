# WAP to find the missing number from the given list

numbers=[0,1,3,4,5]

left=numbers[0]

right=int()

missin_num=float('inf')

for i in range(1,len(numbers)):

    right=i

    diff=right-left

    left=right

    if diff!=1:

        missin_num=numbers[left]+1

    else:

        missin_num=numbers[right]+1

        

print(missin_num)