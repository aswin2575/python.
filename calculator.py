def addition(first,second):
    sum=first+second
    print('sum is',sum)
def substraction(first,second):
    sub=first-second
    print('sub is',sub)
def multiplication(first,second):
    mul=first*second
    print('mul is',mul)
def division(first,second):
    div=float(first/second)
    print('div is',div)
while(1):
    n1=int(input('Enter the numbers\n'))     #inputs first number
    n2=int(input())     #inputs second number
    choice=int(input('enter the choice\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n'))
    match choice:
        case 1:
            addition(n1,n2)
        case 2:
            substraction(n1,n2)
        case 3:
            multiplication(n1,n2)
        case 4:
            division(n1,n2)