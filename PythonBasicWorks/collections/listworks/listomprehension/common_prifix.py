# wAP to find the common prifix from the given words


lists=["fly","flow","flower","float"]

#step1: extract smallest word

#step2: check smallest isn't present in all other words

# step3: if not trim 1 word from smallest and check again

smallest_word=min(lists,key=len)

common_prifix=""

for w in lists:

    if(w!=smallest_word):

        if lists.index(w)<= len(lists) and w.startswith(smallest_word) :

            common_prifix=smallest_word

            pass

        else:

            smallest_word=smallest_word[:len(smallest_word)-1]

print(common_prifix)



