# read a year from user and print century year if year eds with 2 zero else print non century year

year=int(input("Enter the year :> "))

if year%100 ==0:

    print(f"The given year is century year")

elif year%100 !=0:

    print(f"The year is a non century year")