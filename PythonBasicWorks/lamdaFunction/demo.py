


# def add(n1,n2):

#     return n1+n2

# print(add(100,200))

add=lambda n1,n2:n1+n2

# print(add(10,20))

sub=lambda n1,n2:n1-n2

# print(sub(30,20))

cube=lambda n1:n1**3

# print(cube(2))

max_two=lambda n1,n2:n1 if n1>n2 else n1

# print(max_two(20,10))

mi_two=lambda n1,n2:n1 if n1<n2 else n2

# print(mi_two(20,10))

last_digit_max=lambda n1,n2:n1 if n1%10>n2%10 else n2

# print(last_digit_max(127,872))

odd_even=lambda n:"even" if n%2==0 else "odd"

print(odd_even(17))