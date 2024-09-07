# WAP to check the string is an kagaroo string or not


# parent="chickens"  # input("enter the parent word:> ") #chicken

# child= "cchen"#input("enter word to check:>") #hen

# is_kangaroo=False

# for i in range(0,len(child)):

#     word=child[i]

#     if child.count(word)<=parent.count(word) : #h

#         is_kangaroo=True

#     else:

#         is_kangaroo=False




# print(f"'{child}' is a kangaroo word " if is_kangaroo== True else f"'{child}' is not a kangaroo word")


parent="chicken"

Child="henn"

parent_letters={}

for i in parent:

    if i in parent_letters:

        parent_letters[i]+=1

    else:

        parent_letters[i]=1

is_kangaroo=True

for letter in Child:

    if letter in parent_letters and parent_letters.get(letter)>0:

        parent_letters[letter]-=1

    else:

        is_kangaroo=False

print(is_kangaroo)








