# WAP the count of word in a given list

# using list and dict


lists=["blue","green","blue","red","red","red"]

word_count={}

for word in lists:

    if word in word_count:

        word_count[word]+=1

    else:

        word_count[word]=1

print(word_count)