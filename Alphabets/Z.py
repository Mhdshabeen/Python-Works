for i in range(0,3):
    if i==0 or i==2:
        for k in range(0,10):

            if k%2==0:
                print("*",end="")
            else:
                print(" ",end="")
        print("")
    

    else:

        for j in range(8,0,-1):

            if j%2!=0:

                for i in range(0,j):

                    print(" ",end="")

                print("*",end="")
                print("")
        