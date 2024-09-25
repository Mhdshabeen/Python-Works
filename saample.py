
# width = 20
# print ('HackerRank'.center(width,'-'))

width=130
for row in range(1,25):

    string=""

    if row%2!=0:

        for i in range(1,row+1):

            string=string+"*"

       
        print(string.center(width," "),end="\t")
            

        print("")
   


