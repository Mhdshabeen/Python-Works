

# Mathematical Functions
# ----------------------------------------

# abs(x): Returns the absolute value of x.

x = -5
result = abs(x)
print(result)  # Output: 5

# divmod(a, b): Returns the quotient and remainder of a divided by b as a tuple.

a = 10
b = 3
result = divmod(a, b)
print(result)  # Output: (3, 1)

# pow(base, exp): Returns the base raised to the power of exp.

base = 2
exp = 3
result = pow(base, exp)
print(result)  # Output: 8

# round(x, n=None): Rounds x to the nearest integer or to n decimal places.

x = 3.14159
result1 = round(x)
result2 = round(x, 2)
print(result1)  # Output: 3
print(result2)  # Output: 3.14

# max(iterable, *args): Returns the largest item in an iterable or the largest of given arguments.

numbers = [1, 5, 3, 9, 2]
result = max(numbers)
print(result)  # Output: 9

# min(iterable, *args): Returns the smallest item in an iterable or the smallest of given arguments.

numbers = [1, 5, 3, 9, 2]
result = min(numbers)
print(result)  # Output: 1



# Sequence Functions
# -----------------------------------------------------


# len(x): Returns the length of a sequence (e.g., string, list, tuple).

my_list = [1, 2, 3, 4]
length = len(my_list)
print(length)  # Output: 4

# sum(iterable, start=0): Returns the sum of elements in an iterable.

my_list=[1,2,3,4,5]
sum=sum(my_list)
print(sum) # Output: 15

# sorted(iterable, key=None, reverse=False): Returns a new sorted list from the iterable.

numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 1, 3, 4, 5, 9]

# reversed(seq): Returns a reversed iterator over the sequence.

my_list = [1, 2, 3, 4]
reversed_list = reversed(my_list)
for item in reversed_list:
    print(item)  # Output: 4 3 2 1



# Type Conversion Functions
# -------------------------------------------------------------

# int(x): Converts x to an integer.

x = "10"
result = int(x)
print(result)  # Output: 10

# float(x): Converts x to a floating-point number.

x = "3.14"
result = float(x)
print(result)  # Output: 3.14

# str(x): Converts x to a string.

x = 123
result = str(x)
print(result)  # Output: "123"

# bool(x): Converts x to a Boolean value.

x = 0
result = bool(x)
print(result)  # Output: False

# list(x): Converts x to a list.

x = "hello"
result = list(x)
print(result)  # Output: ['h', 'e', 'l', 'l', 'o']

# tuple(x): Converts x to a tuple.

x = [1, 2, 3]
result = tuple(x)
print(result)  # Output: (1, 2, 3)

# set(x): Converts x to a set.

x = [1, 2, 3, 2, 1]
result = set(x)
print(result)  # Output: {1, 2, 3}

# dict(x): Converts x to a dictionary.

x = [("a", 1), ("b", 2)]
result = dict(x)
print(result)  # Output: {'a': 1, 'b': 2}



# Other Functions
# --------------------------------------------------------------


# all(iterable): Returns True if all elements in the iterable are true.

my_list = [True, True, True]
result = all(my_list)
print(result)  # Output: True

# any(iterable): Returns True if any element in the iterable is true.

my_list = [False, False, True]
result = any(my_list)
print(result)  # Output: True

# enumerate(iterable, start=0): Returns an iterator of tuples, each containing an index and 
# the corresponding value from the iterable.

my_list = ["apple", "banana", "orange"]
for index, fruit in enumerate(my_list):
    print(index, fruit)

# zip(*iterables): Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the iterables.

names = ["Alice", "Bob", "Charlie"]

ages = [25, 30, 28]
for name, age in zip(names, ages):
    print(name, age)

# filter(function, iterable): Returns an iterator of elements from the iterable for which the function returns True.

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
for num in even_numbers:
    print(num)

# map(function, iterable, ...): Returns an iterator of the results of applying the function to 
# each element of the iterable.

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
for num in squared_numbers:
    print(num)

# reduce(function, iterable, initializer=None): Applies a function to successive elements 
# of an iterable and returns a single value.

from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)


