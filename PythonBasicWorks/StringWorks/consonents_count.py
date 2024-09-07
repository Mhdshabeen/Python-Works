# write a program to print the number of consonents in a paragraph

# consonents means char other than vowels

text="pneumonoultramicroscopicsilicovolcanoconiosis"

check="aeiou"

v_count=0

for char in text: #a

    if check.count(char)!=0:

        v_count+=1

print(v_count)

c_count=int(len(text))-v_count# count of cosonents

print(c_count)



