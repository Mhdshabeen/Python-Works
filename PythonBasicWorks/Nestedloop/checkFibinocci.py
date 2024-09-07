#Write a program to check the given number is present in febinocci series or not


#logic1

number=int(input("Enter number:> "))

previous=0

current=1

next=previous+current

isfib=False

if number==0 or number==1 :

    isfib=True

else:

    while (next<=number):

        next=previous+next

        if next==number:

            isfib=True

            break

        previous=current

        current=next

print(f"{number} is fib " if isfib==True else f"{number} is not fibinocci")

# readnum=float(input("Enter number:> "))

# prev=0

# current=1

# num=0

# for i in range(1,35):

#     next_num=prev+current

#     if readnum==next_num:

#         num=next_num

#     prev=current

#     current=next_num

# print(f"{readnum} is fibinocci" if num==readnum else f"{readnum} is not fibinocci")