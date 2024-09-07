# write a program to read student name and 3 marks mark1, mark2, and mark3
# also print total mark and avg mark


stud_name=input("Enter student name : ")

mark1=int(input("Enter mark1 = ")) #input will be taken as string so specify the input as int

mark2=int(input("Enter mark2 = ")) #input will be taken as string so specify the input as int

mark3=int(input("Enter mark3 = ")) #input will be taken as string so specify the input as int

total_mark=mark1+mark2+mark3 # if we dont coverted the input to int type from reading itself convert when doing operations

avg_mark=total_mark/3 #average of the 3 marks

print(f"Total mark of the student {stud_name} = {total_mark}") # print total sum of 3 marks

print(f"Average mark = {avg_mark}") # print the avg of 3 marks


