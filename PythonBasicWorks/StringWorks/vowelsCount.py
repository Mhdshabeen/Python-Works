# write  program to print the count of vowels in a paragraph

text="pneumonoultramicroscopicsilicovolcanoconiosis"

vowels="aeiou"

count=0

for char in vowels:

    digit=text.count(char)

    count=count+digit

print(count)

