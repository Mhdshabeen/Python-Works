for i in range(0,5):

    if i==0 or i==4:
        for k in range(0,9):

            if k%2!=0 and k!=1:

                print("*",end="")

            else:

                print(" ",end="")

        print("")

    elif i==1 or i==3:

        for i in range(0,2):
            if i==1:
                print("*",end="")

            else:

                print(" ",end="")

        print("")


    elif i==2:

        for i in range(0,3):
            print("*")
