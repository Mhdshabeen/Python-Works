# read a number and extract digits grom number

# smple input num=123
# output :
    #1
    #2
    #3

num=int(input("Enter num to extract digits:> "))

sum=0

while (num!=0):

    digit1=num%10 #sample num=123  then digit=123%10=3
    print(digit1) #display 3
    num=num//10 #num=123//10=12

 

