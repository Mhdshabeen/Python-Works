# Python program to print the duplicate elements of an array


array=list(input("Enter elements of array:> ").split())

for i in array:

    if array.count(i)>1:

        print(i)