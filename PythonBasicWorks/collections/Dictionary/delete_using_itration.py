

# WAP to delete place from the dict using itration if it present in hr dict

student={"name":"shabeen","place":"kottappuram","course":"science"}

orginal=student.copy()

for i in orginal:

    if i=="place":

        student.pop(i)

print(student)