# WAP to count the number of numbers


numbers=[1,2,3,4,5,1,1,2,3,4,5,2,3,4,4,5,5,6]

number_count={}

for w in numbers:

    if w in number_count:

        number_count[w]+=1

    else:

        number_count[w]=1

for k,v in number_count.items():

    print(f"{k}:>{v}")