#write a program to calculate the montly emi if
#loan-amount (p)
#tenure (n)        ( time period of loan in yrs or month) 
#intrest_rate (r) covert per anuam to per montly using intrest per month= intrestrate/12/100



#equation=(p*r*(1+r)**n)/((1+r)**n)-1)
#r=(intrest_rate/12)/100

loan_amount=200000 # setloan amount

tenure=120 #set tenure in months

intrest_rate=9 # set intrestrate

intrest_rate_per_month=(intrest_rate/12)/100 # covert the intrest rate from intrest per annum to intrest per month

emi=(loan_amount*intrest_rate_per_month*(1+intrest_rate_per_month)**tenure)/((1+intrest_rate_per_month)**tenure-1) #intrast calculation using equation
   
print(f"Your montly emi={emi}")   

# Total payable amount

total_payable_amount=emi*tenure
print(f"Total payable amount={total_payable_amount}")


#total intrest payable on the loan amount
#equation= loanamount * intrest rate per anum * tenure


total_intrest_payable=total_payable_amount-loan_amount

print(f"total intrest payable on the loan amount on loan ={total_intrest_payable}")
