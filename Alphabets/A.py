for i in range(0,4):
    if i==0:

        for k in range(0,9):

            if k%2!=0:

                print("*",end="")

            else:

                print(" ",end="")

        print("")

    elif i==2:

        for k in range(0,9):

            if k%2==0:
                print("*",end="")
            else:
                print(" ",end="")
        print("")

    elif i==1 or i==3:
        if i==1:
            change=2
        else:
            change=3
        for i in range(0,change):
            for j in range(0,10):

                if j==0 or j==8:
                    print("*",end="")

                else:
                    print(" ",end="")
                
            print("")

