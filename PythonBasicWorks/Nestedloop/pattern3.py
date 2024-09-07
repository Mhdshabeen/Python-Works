# @ @ @ @

# @ @ @

# @ @ 

# @


#logic1 

# for raw in range(1,6): #1,2

#     for col in range(1,7-raw): #1,6-1     1,6-2

#         print("@", end=" ")

#     print()

for raw in range(1,6):

    for col in range(5,raw-1,-1):

        print("@", end=" ")

    print()

