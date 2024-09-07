# write a program to print the sum of all elements in an array

array=list(map(int,input("Enter numbers using space").split()))

sum=sum(array)

print(sum)


# logic 2

total=0

for i in array:

    total=total+i

print(total)