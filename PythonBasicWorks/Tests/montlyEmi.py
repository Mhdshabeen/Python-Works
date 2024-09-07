# read the amount, tenure intrest and print the following

# montly emi
# total intrest payble
#  total payment


amount=float(input("enter the amount:> "))
tenute=float(input("enter the tenure:> "))
intrest=float(input("enter the intrest:> "))

intrest_in_month=float(intrest/12/100)

emi:float=(amount*intrest_in_month*(1+intrest_in_month)**tenute)/((1+intrest_in_month)**tenute-1)

print(f"Emi= {emi}")

total=emi*tenute

print(f"total= {total}")

intrest_payable=total-amount

print(f"total intrest payable= {intrest_payable}")