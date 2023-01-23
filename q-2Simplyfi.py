n=int(input("Enter test cases"))
arr=[]
while(n==0):
    x=int(input("Total no. of players between Gihun And Ali"))
    y=int(input("Enter the height of both them"))
    count=0
    for i in range (x):
        arr.append(int(input("enter the height of ith person",i)))
        if (arr[i]>y):
            count+=1
    n-=1
    print(count)





