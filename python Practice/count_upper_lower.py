# write a prgm to count the lower case and upper case letters in a string

string=input("Enter string:> ")

string_case_count={"upper":0,"lower":0}

for alph in string:

    if alph.isupper():

        string_case_count["upper"]+=1

    elif alph.islower():

        string_case_count["lower"]+=1

print(string_case_count)

        

        

