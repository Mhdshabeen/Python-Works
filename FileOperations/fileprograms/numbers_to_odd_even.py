


f_numbers=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\fileprograms\\numbers.txt","r")
f_even=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\fileprograms\\even.txt","w")
f_odd=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\fileprograms\\odd.txt","w")
number_list=[]

# for num in f_numbers:

#     # print(num)

#     number_list.append(num.strip("\n"))

for num in f_numbers:

    number=num.strip("\n")

    if int(num)%2==0:

        f_even.write(num)

    elif int(num)%2!=0:

        f_odd.write(num)
