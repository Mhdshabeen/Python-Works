
class person:

    def __init__(self,name,age,gender):

        self.name=name
        self.age=age
        self.gender=gender

    def display(self):

        return f"{self.name} {self.age} {self.gender}"
    

class employee(person):

    def __init__(self, name, age, gender,eid,department,salary):
        super().__init__(name, age, gender)

        self.eid=eid
        self.department=department
        self.salary=salary

    def display(self):
        print(super().display() ,self.eid,self.department,self.salary)
        # print()

employee_inheritance=employee("hari",40,"male","AME20CS016","CSE",50000)

employee_inheritance.display()