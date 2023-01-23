n=int(input("Enter test cases:"))
arr=[]
for j in range(n):
    x=int(input("Total no. of players between Gihun And Ali:"))
    y=int(input("Enter the height of both them:"))
    count=0
    for i in range (x):
        arr.append(int(input("enter the height of ith person:")))
        if (arr[i]>y):
            count+=1
    print("minimum no. of player to get shot",count)





