# def fib(n):
#     if (n==1 and n==2):
#         return 
#     else:
#         print(sg)
#         sg=sg + fib(n-1)
#         return sg
# print('0\n1')
# val=fib(5)
# print(val)

# str1=int(['0','1'])
# n=int(input("Enter the number of elements:"))
# for i in range(2,n):
#     str1.append(int(str1[-1]) + int(str1[-2]))
# print(str1)
# def fib(str1,n):
    
def fibonacci(n):
    if(n<=1):
        return n
    else:
        return (fibonacci(n-1)) + (fibonacci(n-2))
    
n1=int(input("Enter the number of elements:"))
if n1==0:
    print('error')
else:
    for i in range(n1):
        result=fibonacci(i)
        print(result)