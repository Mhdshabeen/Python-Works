
f_open=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\fileprograms\\news.txt","r")

word_list=[w for line in f_open for w in line.strip("\n").split(" ")]

# for line in f_open:

#     word=line.strip("\n")

#     words=word.split(" ")

#     for w in words:

#         word_list.append(w)

word_count={w:word_list.count(w) for w in word_list if w!="" }

# print(word_count)


srt=sorted(word_count,key=lambda key:word_count.get(key),reverse=True)

print(srt)

