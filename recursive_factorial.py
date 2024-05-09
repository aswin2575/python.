def fact(x):
    if(x<=1):
        return x
    else:
        x=x*fact(x-1)
        return x
n=int(input('Enter the number:'))
val=fact(n)
print(val)