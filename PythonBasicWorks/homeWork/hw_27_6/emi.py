# write a prgm to calculate 

# montly emi
#total payment
# total intrest payable

#equation=(p*r*(1+r)**n)/((1+r)**n)-1)
#r=(intrest_rate/12)/100

#read loan amount, tenure,intrest rate from user

loan_amount=int(input("Enter the loan amount :> ")) #read loan amont

tenure=int(input("Enter the period :> ")) #read months to back loan

intrest_rate=int(input("Enter the intrest rate :> ")) # read intreast rate at which loan taking

intrest_rate_in_month=(intrest_rate/12)/100 # covert intrest rate in year to monthly

emi=(loan_amount*intrest_rate_in_month*(1+intrest_rate_in_month)**tenure)/((1+intrest_rate_in_month)**tenure-1) # calculate emi amount

print(f"Montly emi ={emi}") # print montly emi to pay

total_amount=emi*tenure # Total amount to payback loan

print(f"total payable amount= {total_amount}") # display the amount to pay back

intrest=total_amount-loan_amount # calculate the how much intrest to pay total when complete the loan 

print(f"Intrest to pay ={intrest}") # display the intrest to pay