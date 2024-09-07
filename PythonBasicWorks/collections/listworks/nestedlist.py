# write a program to get the element of a list in nested list

numbers=[1,2,[3,[100,200],4],5,6]

print(numbers[2][1][0])

# write a program to append a value to nested list

numbers[2][1].append(500) #[100, 200, 500]

print(numbers) #[1, 2, [3, [100, 200, 500], 4], 5, 6]