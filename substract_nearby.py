#check which numbers has the most difference
#first number should be less than the second number
#only nearby numbers should be considered

n=int(input("Enter the no.of elements:"))
str2=['']*n
for i in range(0,n):
     str2[i]=input()
# for i in range(n):
#     print(str[i])
max=0
#str1=['7','8','9','12','9','0']
leng=len(str2)
for i in range(1,leng):
    num1=int(str2[i-1])
    num2=int(str2[i])
    if(num1 <num2):
        sub=num2 - num1
        if(sub>max):
            max=sub
print(max)