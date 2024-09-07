
numbers=[0,4,8,10]

new_list=[]

for i in range(numbers[0],numbers[-1]+1):

    if i==0:

        new_list.append(i)

    elif i%2==0:

    #num=i*2

        new_list.append(i)

print(new_list)

missing=set(numbers).symmetric_difference(tuple(new_list))

print(list(missing))











    

