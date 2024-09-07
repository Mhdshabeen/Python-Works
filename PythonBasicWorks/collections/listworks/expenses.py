# find cound of obj in expences








expences=[10000,20000,30000,40000,50000,60000,70000]

total=0

count=len(expences)
# print all expences
for i in range(0,count):
    
    print(expences[i])
# print total of expences
    total=total+expences[i]
# print expences greater than 25000
for i in range(0,count):

    if expences[i]>25000:

        print(expences[i], end=" ")
    
print()
    
print(f"Total= {total}")

# average ecpence
avg_expence=total/count

print(f"Average expence={avg_expence}")



    