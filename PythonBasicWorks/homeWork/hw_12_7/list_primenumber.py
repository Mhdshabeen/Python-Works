# write a program to check the number is prime or not in the given list

numbers=[10,11,12,13,14,20,21]


for i in range(0,len(numbers)):

    for j in range(2,numbers[i]):#2,21

        if numbers[i]%j==0:

            is_prime=False

            break

    print(numbers[i] if is_prime==True else "")

            

