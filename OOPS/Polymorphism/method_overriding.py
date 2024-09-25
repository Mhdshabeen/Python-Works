

# 2 rules
# require min two classes

class parent():

    def mobile(self):

        print("samsung")

    def bike(self):

        print("Dominar")


class child(parent): # here child inherit the attributes of parent

    def mobile(self): # when child buy new bike it override the parent method

        print("Iphone")


child_instance=child()

child_instance.mobile()

    