

class grandparent:

    def m1(self):
        
        print("Grandparent class m1 method")

class parent:

    def m2(self):

        print("parent class m2 method")

class child(parent,grandparent):

    def m3(self):

        print("Child class m3 method")

child_instance=child()

child_instance.m2()