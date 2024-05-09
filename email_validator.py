import re
text=input("Enter the email id\n")
def checker(text):
    pattern=r'.*@email.com'
    match=re.match(pattern,text)
    if match:
        print(' ' + '',text + 'is correct')
    else:
        print(' ',text + 'is not correct')
checker(text)