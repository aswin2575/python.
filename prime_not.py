#prime or not
num=int(input ('Enter the number:'))
flag=0
if(num==1):
    flag=1
for i in range(2,int((num/2)+1)):
    if(num%i==0):
        flag=1
        break
if(flag==0):
    print('The number is prime')
else:
    print ('The number is not prime ')