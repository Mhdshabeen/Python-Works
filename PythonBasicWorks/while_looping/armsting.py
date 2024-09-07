# print the given number is amtrong or not


num=int(input("Enter num:> "))

store_num=num

total=0

num_count=len(str(num))

while (num!=0):

    digit=num%10

    exponent=digit**num_count

    total=total+exponent

    num=num//10

if(store_num==total):

    print(f"Given number is amstrong= {total}")

else:

    print(f"given number '{store_num}' is not a amstrong number")