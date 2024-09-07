# must start with alph or underscore
# cannot start with number
# A variable name should only contain alphanum or underscore
#variable names are case sensitive

from re import fullmatch

text_input=input("Enter name:")

pattern="[a-zA-Z][a-zA-Z0-9_]*" # * is used to represend optional it may come number of times or else no contain

matcher=fullmatch(pattern,text_input)

if matcher==None:

    print("invalid")

else:

    print("valid")
