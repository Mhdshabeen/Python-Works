#write a bmi program 

# read height and weight from user

# bmi=> (weight in kg/height in meter square)

weight=int(input("Enter the weight(kg):> ")) # read weight

height=int(input("Enter the height(cm):> ")) # read height

height_in_msqr=(height/100)**2 # convert height to meter square

bmi=(weight/height_in_msqr) # calulate bmi

print(f"Resulted bmi is = {bmi}") #display result