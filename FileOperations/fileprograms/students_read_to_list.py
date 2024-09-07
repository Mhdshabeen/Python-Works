

f=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\fileprograms\\students.txt",'r')

students=[]

for stud in f:

    students.append(stud.rstrip("\n"))

print(students)