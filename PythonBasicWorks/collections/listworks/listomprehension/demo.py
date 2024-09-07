# syntax:
#       listname=[return iteration condition]

# eg:> square=[n**2 for n in list ]


list=[1,2,3,4,5,6,7,8]

#square of all numbers in list
square=[n**2 for n in list ]

#square of odd numbers in list
odd_square=[n**2 for n in list if n%2!=0]

# print even numbers from list
even_num=[n for n in list if n%2==0]

# print odd numbers from list
odd_num=[n for n in list if n%2!=0]

#sum of of odd numbers



print(square)

print(odd_square)

print(even_num)

print(odd_num)