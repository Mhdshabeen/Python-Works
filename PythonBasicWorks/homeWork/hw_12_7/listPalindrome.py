# from the given list of objects print the palindromic strings


words=["madam","aba","bcb","hello","python"]

for i in range(0,len(words)):

    palindrome=words[i][::-1]

    if palindrome==words[i]:

        print(palindrome)

    



