
from re import finditer

text="ababbaab"
#     01234567

count=0

# count ab and position
matcher=finditer("ab",text)

for i in matcher:

    print(i.start(),"===",i.group())

    count+=1

print(count)