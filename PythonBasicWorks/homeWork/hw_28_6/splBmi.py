# read height and weight from the user and calculate bmi

#print under weight if bmi<19

#print normal weight if bmi is range of 19-25

#print over weight if bmi is range of 25-30

#print obsity if bmi>30

weight=float(input("Enter weight (kg):> "))

height=float(input("Enter height (cm):> "))

height_in_meter=(height/100)**2

bmi=weight/height_in_meter

result=""

if bmi<19:

    result= result+"under weight"

elif bmi>=19 and bmi<25:

    result=result+"normal weight"

elif bmi>=25 and bmi<30:

    result=result+"Over weight"

elif bmi>=30:

    result=result+"Obesity"

print(f"Bmi = {bmi}")

print(result)