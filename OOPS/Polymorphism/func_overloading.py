

def add_num(n1,n2):

    return n1+n2

def add_num(n1,n2,n3):

    return n1+n2+n3

print(add_num(100,200,200))

# here we cant use overloading becoz overloading means same name diff num of arguments here we can see two 
# functions defined add_num but this wont work once we write the second func the first function will be
# rewritten with the 2nd functions arguments so we cant call the first function to add two numbers 