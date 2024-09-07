

f_years=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\fileprograms\\years.txt","r")

f_leapyear=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\fileprograms\\leapyears.txt","w")

f_nonleapyear=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\fileprograms\\nonleapyears.txt","w")

for yr in f_years:

    year=int(yr.strip("\n"))

    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):

        f_leapyear.write(str(year)+"\n")

    else:

        f_nonleapyear.write(str(year)+"\n")