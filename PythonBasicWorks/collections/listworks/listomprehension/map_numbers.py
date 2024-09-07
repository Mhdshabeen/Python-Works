# WAP to map the given numbers in list
# rule :> if number > 5 number+1, if number<5 number-1

lists=[6,7,3,4,8,9,2,10]

mapped_list=[num+1 if num>5 else num-1 for num in lists ] #[7, 8, 2, 3, 9, 10, 1, 11]

print(mapped_list)