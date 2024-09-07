# find the amsteong numbers in a given range of intervel

input=1000 #int(input("Enter the limit:> "))


for i in range(1,input+1):

    store_num=i

    length=len(str(i))

    total=0

    while i!=0:

        digit=i%10

        total=total+digit**length

        i=i//10

    if total==store_num:

        print(store_num)






