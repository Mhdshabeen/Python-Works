# WAP to get second smallest element from the given list

numbers=[1,2,3,]

#numbers.sort(reverse=True)

smallest_num=float('inf')

second_smallest=float('inf') 

for i in numbers: 

    if i < smallest_num : 

        second_smallest=smallest_num 

        smallest_num=i#

    elif i < second_smallest and i> smallest_num:

        second_smallest=i

    

    
print(second_smallest)

