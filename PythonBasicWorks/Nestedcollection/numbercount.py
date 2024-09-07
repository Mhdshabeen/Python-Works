# WAP to count the numbers in a list

numbers=[11,23,11,23,45,33,45,11]

number_cont={num:numbers.count(num) for num in numbers}

print(number_cont)