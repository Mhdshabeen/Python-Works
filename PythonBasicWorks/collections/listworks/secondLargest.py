# WAP to get the second largest number from the list using method


list=[4.2,8,5,11,15,18,12,10,2,20,40,33,19]

list.sort(reverse=True)

#print(list[1])

# WAP to get the second largest number from the list without using method

list2=[12,2,5,7,1,11,10,4]

largest=0

second_largest=0

for i in list2:

    if i > second_largest and i > largest:

        second_largest=largest

        largest=i

    elif i> second_largest and i< largest:

        second_largest=i

print(second_largest)

