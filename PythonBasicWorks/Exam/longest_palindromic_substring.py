# WAP to get the longest palindromic substring from the given string


text="racecar"

longest_palindrome=""

for i in range(0,len(text)):

    left=i
    
    right=i

    while(left>=0 and right<len(text)) and (text[left]==text[right]):

        current_string=text[left:right+1]

        if len(current_string)>len(longest_palindrome):

            longest_palindrome=current_string

        left-=1

        right+=1

print(longest_palindrome)