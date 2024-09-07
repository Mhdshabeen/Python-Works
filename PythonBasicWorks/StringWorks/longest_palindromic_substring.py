# longest palindromic substring from given string

#text="ababba"

# a
# b
# aba
# bb
#abba

#text="RACECAR"

#R
#A
#C
#E
#CEC
#ACECA
#RACECAR


text="racecar"

longest_palindrom_string=""

for i in range(0,len(text)):

    left=i

    right=i

    while ( left>=0 and right<len(text) and text[left]==text[right]):

        current_palindrom_string=text[left:right+1]

        if len(current_palindrom_string)>len(longest_palindrom_string):

            longest_palindrom_string=current_palindrom_string

        left-=1

        right+=1


print(longest_palindrom_string)



    

       







