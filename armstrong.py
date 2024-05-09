n1=int(input("Enter the interval"))
n2=int(input())
for i in range(n1,n2):
    first=str(i)
    leng=len(first)
    sum=0
    for j in range(leng):
        sum=sum+int(first[j])**leng
    if(sum==int(first)):
        print(first)
    
    #another method
    # n=int(input("Enter start: "))
    # m=int(input("Enter end: "))
    # for i in range(n,m+1):
    #     j=i
    #     x=0
    #     l=len(str(i))
    #     while(j!=0):
    #         dig=j%10
    #         x=x+dig**l
    #         j=int(j/10)
    #     if(x==i):
    #         print(i)