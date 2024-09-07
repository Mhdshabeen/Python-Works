# WAP to print the unique numbers from a given list

numbers=[1,2,3,4,5,1,4,7,9,3,0,4]
newlist=[]
for i in numbers:

    if numbers.count(i)==1:

        newlist.append(i)

print(newlist)

        