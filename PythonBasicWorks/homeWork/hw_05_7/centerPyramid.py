# write a program to print

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

raw=int(input("Enter number of raws:> "))

# loop to iterate for each row
for i in range(1,raw+1):

# loop to print spaces before stars
    for j in range(0,raw-i):

        print(" ",end=" ")

# loop to print stars in each row (2 * i - 1)
    for j in range(1,2*i):

        print("*",end=" ")

    print()