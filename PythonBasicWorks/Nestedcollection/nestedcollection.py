


arr=[[10,20],
     [30,20],
     [40,50]
    ]

# logic1

numbers1=[num for lst in arr for num in lst]

print(sum(numbers1))

# logic2
numbers=[]

for list in arr:

    for num in list:

        numbers.append(num)

print(sum(numbers))

        