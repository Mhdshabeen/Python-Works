# WAP to move the numbers in a givn tuple and add new numbers


numbers=(1,2,(3,4),5,6)

#print(numbers[2])

list1=list(numbers[2])

list1.insert(0,2.5)

numbers=list(numbers)

print(numbers)

numbers[2]=tuple(list1)

print(numbers)

numbers = tuple(numbers)

print(numbers)
