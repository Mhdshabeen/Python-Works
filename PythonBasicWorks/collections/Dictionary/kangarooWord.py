# WAP to print word is kangaroo word or not

source_word="REGULATE"

target_word="RULE"

source_word_count={}

for char in source_word:

    if char in source_word_count:

        source_word_count[char]+=1

    else:

        source_word_count[char]=1

is_kangaroo=True

for char in target_word:

    if char in source_word_count and source_word_count.get(char)>0:

        source_word_count[char]-=1

    else:

        is_kangaroo=False

print(is_kangaroo)


