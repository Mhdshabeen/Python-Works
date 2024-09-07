 # wite a prgm  to return the username and the domain seprately from a email

email="hshsb@gmail.com"

index_pos=email.index("@")

username=email[:index_pos]

domain=email[index_pos:]

print(f"Domine= {domain}\n" f"username= {username}")

