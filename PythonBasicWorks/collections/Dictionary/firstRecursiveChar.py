#WAP to print first recursive character in the given word

text="BACDDA"

recursive_count={}

for w in text:

    if w in recursive_count: 

        print(w)

        break

    else:

        recursive_count[w]=1

print(recursive_count)

