from re import finditer

text="hellopythonhrloopythonhellopython"

matcher=finditer("python",text)

count=0

for m in matcher:

    print(m.start(),"==",m.group())

    count+=1


print(count)