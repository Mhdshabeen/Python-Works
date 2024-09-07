

text="hello hai hai hello how hello"

words=text.split(" ")

# print(words)

word_count={w:words.count(w) for w in words}

print(word_count)