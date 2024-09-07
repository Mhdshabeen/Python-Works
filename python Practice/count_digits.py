

num=int(input("Enter num:> "))

digit_count={}

for i in str(num):

    if i in digit_count:

        digit_count[i]+=1

    else:

        digit_count[i]=1

print(digit_count)


