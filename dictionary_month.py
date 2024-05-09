dict={1:'january',2:'february',3:'march',4:'april',5:'may',6:'june',7:'july',8:'august',9:'september',10:'october',11:'november',12:'december'}
# choice=int(input("Enter the month:"))
# print(dict[choice])
print(dict.keys())
print(dict.values())
for i in dict.keys():
    print(i,'||',dict[i])
dict[13]='invalid'
for i in dict.keys():
    print(i,'||',dict[i])
del dict[13]
for i in dict.keys():
    print(i,'||',dict[i])
for i in dict.keys():
    if(i%2==0):
        print(i,'||',dict[i])

    #print(dict[i])
# for i in dict.values():
#     print(i)
# name='aswin'
# age=21
# print('My name is',name,'I am ',age)