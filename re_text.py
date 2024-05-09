import re
text="Email:abc@example.com,xyz@domain.com,pqr@company.co.uk\nPhone:123-456-7890,987.654.3210,999-888-7777\n"
def email(text):
    emails=re.match(r'Email:(\S+@\S+)',text)
    if emails:
        first_email = emails.group(1)
    print("The emails are:",end='')
    print(first_email)
def phone(text):
    #
    #replaces=re.sub(r'\.','',replaces)
    phone_numbers = re.findall(r'\b(?:\+?[1-9]\d{0,2}[-. ]?)?\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}\b', text)
    #replaces=re.sub(r'-','',phone_numbers)
    #phones=re.match(r'Phone:(\D)',replaces)
    cleaned_numbers = [number.replace('-', '').replace('.', '') for number in phone_numbers]
    #if phones:
    #    phn1=phones.group(1)
    print("phone numbers are :",end='')
    for number in cleaned_numbers:
        print(number + ',',end='')
    #print(phn1)
    #print(phones)
       # if phone_numbers:
        #    print("The phone numbers are:",end='')
         #   print(phone_numbers)
email(text)
phone(text)