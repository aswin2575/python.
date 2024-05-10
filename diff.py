def diff(num1,num2,num3):
    if num1>num2 and num1>num3:
        max=num1
    elif num2>num3:
        max=num2
    else:
        max=num3
    print(max)
    mean=(num1+num2+num3)/3
    print(mean)
    differ=max-mean
    return differ
num1=int(input('Enter the numbers:'))
num2=int(input())
num3=int(input())
value=diff(num1,num2,num3)
print(value)