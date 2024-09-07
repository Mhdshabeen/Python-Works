

from re import finditer


text="abc !3YiU2@*"

# pattern="\d" # equal to [0-9]

# pattern="\D" # similar to [^0-9] exclude digits

# pattern="\w" # similar to[a-zA-Z0-9]

# pattern="\W" # similar to [^a-zA-Z0-9]

# pattern="\s" #find spaces in string

pattern="\S" #exclude spaces in string



matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())