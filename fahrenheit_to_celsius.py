fahrenheit=int(input('Enter the fahrenheit temperature:'))
def convert(temp):
    celsius=float(int(int(temp-32)*5)/9)
    return celsius

def truncate(n,decimal=2):
    multiplier=10**decimal
    return int(n*multiplier)/multiplier
t1=convert(fahrenheit)
rounded=truncate(t1)
print('Celsius temperature is ',rounded)