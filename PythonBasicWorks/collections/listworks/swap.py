#WAP to swap last and first element in the list
#logic 1
numbers=[1,2,3,4,5]

temp1=numbers.pop()

temp2=numbers.pop(0)

numbers.append(temp2)

numbers.insert(0,temp1)

print(numbers)

# logic2

numbers2=[2,4,6,8,10]

numbers2[-1],numbers2[0]=numbers2[0],numbers2[-1]

print(numbers2)
