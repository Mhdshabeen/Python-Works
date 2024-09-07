# Python program to print the elements of an array present on even position

array=["my","father","name","and","is","was","shabeen","azees"]

array_len=len(array)

for i in range(0,array_len):

    if i%2==0:

        print(array[i])