# Python program to print the elements of an array present on odd position


array=["are","my","yle","name","falg","is","gtre","azees"]

array_len=len(array)

while array_len>=0:

    if array_len%2!=0:

        print(array[array_len])

    array_len-=1