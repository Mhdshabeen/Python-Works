# WAP to remove the even numbers from the list

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

for i in numbers:

    if i%2==0:

        numbers.remove(i)


print(numbers)