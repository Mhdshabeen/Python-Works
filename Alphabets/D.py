for i in range (0,7):

    if i==0 or i==6:

        for j in range(0,7):

            if j%2==0:

                print("*",end="")

            else:

                print(" ",end="")

        print("")

    elif i==1 or i==5:

        for j in range(0,9):

            if j==0 or j==8:

                print("*",end="")

            else:

                print(" ",end="")

        print("")

    elif i==2 or i==4 or i==3:

        for j in range(0,10):

            if j==0 or j==9:

                print("*",end="")

            else:

                print(" ",end="")

        print("")

