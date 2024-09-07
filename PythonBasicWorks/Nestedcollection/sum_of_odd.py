 
arr=[[11,12]
    ,[13,14]
    ,[15,16]
    ,[17,18]
    ]

odd_numbers=[num for lists in arr for num in lists if num%2!=0]

print(sum(odd_numbers))