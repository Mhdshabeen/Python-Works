# WAP to remove the duplicate num from the list


list=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

orginal=list.copy()

for i in list:#1

    if list.count(i)>1:#2>1

        list.remove(i)

        list=orginal

print(list)
