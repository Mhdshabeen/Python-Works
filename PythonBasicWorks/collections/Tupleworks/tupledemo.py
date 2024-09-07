

number=(1,2,3,4,5)  # tuple is define using ()

print(number[0])  

# each elements have its own index position ,   
# duplicates allowed
# not updatable


numbers=[1,2,[3,(100,200),4],5,6] # i need a result [1,2,[3,(100,200,300),4],5,6]

numbers[2][1]=list(numbers[2][1]) # first changed tuple to list

numbers[2][1].append(300) # then appended 300 to list

numbers[2][1]=tuple(numbers[2][1]) # now changed list to tuple

print(numbers[2][1])

print(numbers) # printed numbers list


