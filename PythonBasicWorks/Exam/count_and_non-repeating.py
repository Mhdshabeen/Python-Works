\


numbers=["red","red","blue","blue","blue","green"]

orginal=numbers.copy()

unique_list=[]

for i in numbers:
    
    count=numbers.count(i)

    print(f"{i}={count}")

    while numbers.count(i)>1:

        numbers.remove(i)

# non repeating numbers

for j in orginal:

    if orginal.count(j)==1:

        unique_list.append(j)

print(f"list of non repeaing numbers={unique_list}")

print(numbers)





    