# object oriented programming

# class [blueprint, Design pattern, Template]
# object [ instance | real world entity]


class student:

    name:str
    age:int
    address:str
    contact:int
    course:str
    studid:str

    def set_student(self,name,age,address,contact,course,id):

        self.name=name
        self.age=age
        self.address=address
        self.course=course
        self.studid=id
        self.contact=contact

    def display_student(self):

        print(self.name,self.age,self.address,self.contact,self.course,self.studid)


# creating object of student class 

student_instance=student()

student_instance.set_student("shabeen",12,"Akkaraparmbil house",9207251721,"python",101)

display=student_instance.display_student()
