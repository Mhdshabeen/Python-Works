class operations():

    def perform_add(self,*args):

        # total=0

        # for arg in args:

        #     if isinstance(arg,(int,float)): # is instance function is used Return whether an object is an instance of a class or of a subclass thereof.

        #         total=total+arg
        # else we can use list coprihension tooo

        total=sum([arg for arg in args if isinstance(arg,(int,float))])

        return total
    
    def perform_max(self,*args):

        return max(args)
    

math=operations()

print(math.perform_add(10,20,70))

print(math.perform_add(10,40))

print(math.perform_max(40,20,30,70,50,80))