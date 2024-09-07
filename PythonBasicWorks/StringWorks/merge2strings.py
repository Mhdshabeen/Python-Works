# write a program to merge two string

# sample input1

# word1="PQR"
# word2="ABC"

#result=PAQBRC

#logic1 for sample input1

# merged_string=""

# for i in range(0,len(word1)):

#     merged_string=merged_string+word1[i]+word2[i]

# print(merged_string)

#result=PAQBRC



# sample input2

# word1="PQRST"
# word2="ABC"

#result=PAQBRCST

#sample input3

# word1="PQR"

# word2="ABCDE"

#result=PAQBRCDE


word1=input("enter string1:> ")

word2=input("Enter string2:> ")

# step1 : find smallest word

smallest_word= word1 if len(word1)<len(word2) else word2

# step2 initialize variable to store result

merged_string=""

# step3 create a for loop to itrate upto smallest word length

for i in range(0,len(smallest_word)):

    # step4 add the char at the i th index with merged string 

    merged_string=merged_string+word1[i]+word2[i]

# step5 using a for loop find which word is largest

if len(word1)>len(word2):

# step6 slice the balance of the largest word from legth of index of smallest word to end

    balace_word=word1[len(smallest_word):]

else:

    balace_word=word2[len(smallest_word):]

# step7 add the sliced string with the meged string to form the final output

merged_string=merged_string+balace_word

print(merged_string)
