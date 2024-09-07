# write a prgm to print the given word is anagram or not

# source_word="listen"

# target_word="slient"

# sorted_source_word=sorted(source_word)

# sorted_target_word=sorted(target_word)

# print(sorted_source_word==sorted_target_word)

def is_anagram(word1,word2):

    sort_word1=sorted(word1)

    sort_word2=sorted(word2)

    return sort_word1==sort_word2

print(is_anagram("silent","listens"))