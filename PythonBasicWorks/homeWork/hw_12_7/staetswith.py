# print the words starting with fly 


words=["fly","flyaway","flask","flyout","flora"]

for i in range(0,len(words)):

    orginal=words[i].startswith("fly")

    if orginal==True:

        print(words[i])