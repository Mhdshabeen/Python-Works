# write a program to select the obj from the list starting with vowels

words=["hello","hai","python","apple","eagle"]

vowels="aeiou"

for i in range(0,len(words)):

    if words[i].startswith("a") or words[i].startswith("e") or words[i].startswith("i") or words[i].startswith("o") or words[i].startswith("u"):


        print(words[i])


