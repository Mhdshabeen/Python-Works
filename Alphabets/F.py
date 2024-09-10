for i in range(0,4):

    if i==0 or i==2:
        for k in range(0,10):

            if k%2==0:
                print("*",end="")
            else:
                print(" ",end="")
        print("")

    elif i==1 or i==3:

        if i==3:
            change=3
        else:
            change=2

        for i in range(0,change):
            print("*")
