

class employee():

    name:str
    age:int
    empid:str
    department:str
    contact:int

    def __init__(self,name,age,empid,dept,contact):

        self.name=name
        self.age=age
        self.empid=empid
        self.department=dept
        self.contact=contact

    def display_employee(self):

        print(self.name,self.age,self.empid,self.department,self.contact)

employee_instance=employee("shabeen",22,"AME20CS016","HR",920725121)

employee_instance.display_employee()