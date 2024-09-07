# program to convert temp in celcius to temp n fh


#equation is (celcius*(9/5)+32)

#read temp in celsius from user

temp_in_celcius=(int)(input("Enter the temp (C) :>"))

temp_in_fh=(temp_in_celcius*(9/5))+32

print(f"Temp to fh = {temp_in_fh}")