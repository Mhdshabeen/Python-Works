

arr=[[11,12],
     [13,14],
     [15,16]
    ]

even_numbers=[num for lst in arr for num in lst if num%2==0]

print(sum(even_numbers))