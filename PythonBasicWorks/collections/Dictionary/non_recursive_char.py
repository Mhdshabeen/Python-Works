# write a program to print the non recursive char


text="ABABCDE"

char_count={}

for char in text:

    if char in char_count:

        char_count[char]+=1

    else:

        char_count[char]=1

for k in char_count.keys():

    if char_count[k]==1:

        print(k)