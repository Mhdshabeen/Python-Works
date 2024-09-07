# WAP to get the odd numbers from a list to another list


numbers=[1,2,3,4,5,6,7,8,9]

odd_num=[]

for i in numbers:

    if i%2!=0:

        odd_num.append(i)

print(odd_num)