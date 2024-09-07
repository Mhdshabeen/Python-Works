


numbers=[10,11,12,34,43,54,19,78,42]

# print number of objects in numbers

count=len(numbers)

print(f"number of objects in numbers= {count}")

# print even numbers from this numbers

total=0

for i in range(0,count):
# print total of numbers
    total=total+numbers[i]

    if numbers[i]%2==0:

        print(numbers[i])

print(f"Total of numbers = {total}")

# print total of odd numbers
total_odd=0

for i in range(0,count):

    if numbers[i]%2!=0:

        total_odd=total_odd+numbers[i]

print(f"Total of odd = {total_odd}")



