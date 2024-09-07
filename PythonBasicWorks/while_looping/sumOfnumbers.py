# write aa program to print the sum of given range of numbers 

# read the starting and ending range of numbers fro user


start=int(input("Enter the starting :> "))

end=int(input("enter to where much :> "))

sum=0

while start<=end: 

    sum=sum+start

    start+=1

print(sum)
