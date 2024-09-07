


from re import finditer

text="abc123 @K#7Ldefhij36kxB@$yzX!*"

# pattern="[abd]" #check for a,b or d

# pattern="[a-k]" #chech for alphabets from a to k

# pattern="[a-z]" # check for all lower case alphabets

# pattern="[A-Z]" # check for all upprcase alphabets

# write a pattern to match all alphabets

# pattern="[a-zA-z]"

# pattern="[0-9]" # check for digits

# write a patttern to get all alpha and numbers

# pattern="[a-zA-Z0-9]" #check for all alphanum characters

# pattern="[^0-9]" # check for all char excluding num

# pattern="[^a-zA-Z0-9]" # check for all char other than alphanum

pattern="[\s]" # check for space


matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())