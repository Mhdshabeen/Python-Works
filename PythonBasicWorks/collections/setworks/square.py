# WAP to get the square of elements ith set


main_set={2,5,3,8,9,6,4,7}

orginal=main_set.copy()

new_set=set()

for i in orginal:

    element=main_set.pop()

    square=element**2

    new_set.add(square)

#print(new_set)

new_set=list(new_set)

#print(new_set)

new_set.sort()

# print(new_set)

new_set=set(new_set)

print(new_set)

