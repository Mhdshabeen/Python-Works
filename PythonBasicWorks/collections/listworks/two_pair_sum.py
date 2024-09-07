# print pairs from the list which result 7 as the sum of pairs


arr=[2,3,4,5]

result=7

for i in range(0,len(arr)):

    for j in range(0,len(arr)):

        demo_resut=arr[i]+arr[j]

        if result==demo_resut:

            print(arr[i],arr[j])



