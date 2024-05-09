dict1={'ASI21CS039' : {'name':'aswin','hin':'A','mal':'B+','mat':'A+','sci':'B'},
       'ASI21CS042' : {'name':'bilal','hin':'B+','mal':'A+','mat':'D','sci':'B+'},
       'ASI21CS032' : {'name':'arjun','hin':'A+','mal':'C','mat':'A+','sci':'A+'},
       'ASI21CS026' : {'name':'ansif','hin':'A','mal':'A','mat':'A','sci':'A'}}
#GRADING SYSTEM points
#A+ = 95-100    10
#A  = 90-94     9
#B+ = 80-89     8
#B  = 70-79     7
#C+ = 60-69     6
#C  = 50-59     5
#D  = 40-49     4
#F  = 0-39      3

flag=0
id=input('Enter the student id:')
id=id.upper()
for studentid in dict1.keys():
    if id==studentid:
        flag=1
        data=[]
        data.append(dict1[studentid]['hin'])
        data.append(dict1[studentid]['mal'])
        data.append(dict1[studentid]['mat'])
        data.append(dict1[studentid]['sci'])
        leng=len(data)
        tot=0
        for i in range(leng):
            if data[i]=='A+':
                tot=tot+10
            elif data[i]=='A':
                tot=tot+9
            elif data[i]=='B+':
                tot=tot+8
            elif data[i]=='B':
                tot=tot+7
            elif data[i]=='C+':
                tot=tot+6
            elif data[i]=='C':
                tot=tot+5
            elif data[i]=='D':
                tot=tot+4
            elif data[i]=='F':
                tot=tot+3
            else:
                print("INVALID")
        avg=tot//leng
        match avg:
            case 10:
                avg_gra='A+'
            case 9:
                avg_gra='A'
            case 8:
                avg_gra='B+'
            case 7:
                avg_gra='B'
            case 6:
                avg_gra='C+'
            case 5:
                avg_gra='C'
            case 4:
                avg_gra='D'
            case 3:
                avg_gra='F'
            case _:
                print('Invalid')
        print('Student Details')
        print('-'*60)
        print('Name\tHindi\tMalayalam\tMaths\tScience\tAvg_Grade\n')
        print(dict1[studentid]['name'],'\t',dict1[studentid]['hin'],'\t',dict1[studentid]['mal'],'\t\t',dict1[studentid]['mat'],'\t',dict1[studentid]['sci'],'\t',avg_gra)
        break
if flag==0:
    print('Invalid student id')