for i in range(0,5):
    if i==0 or i==2 or i==4:

        for k in range(0,7):

            if k%2==0:
                print("*",end="")
            else:
                print(" ",end="")
        print("")

    elif i==1 or i==3:
        for i in range(0,2):
            for j in range(0,10):

                if j==0 or j==8:
                    print("*",end="")

                else:
                    print(" ",end="")
                
            print("")