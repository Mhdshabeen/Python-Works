# Write program to count the number of elements present in an array

array=list(map(str,input("Enter array elements by space:> ").split()))

num_element={}

for i in array:

    if "number of elements" in num_element:

        num_element["number of elements"]+=1

    else:

        num_element["number of elements"]=1

print(array)

print(num_element)

# logic 2

print(len(array))