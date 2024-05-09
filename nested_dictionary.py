dict1={1 : {'name':'aswin','hin':45,'mal':67,'mat':87,'sci':45},
       2 : {'name':'bilal','hin':44,'mal':37,'mat':57,'sci':75},
       3 : {'name':'arjun','hin':32,'mal':87,'mat':97,'sci':65},
       4 : {'name':'ansif','hin':25,'mal':77,'mat':37,'sci':55}}

choice=int(input('1.Roll number\n2.Name\n3.Max Mark\n4.Min Mark\nEnter the choice:'))
match choice:
    case 1:
        #roll number
        roll=int(input('Enter the roll number:'))
        for i in dict1.keys():
            if i==roll:
                print('Details')
                print('-'*20)
                print('Name      :',dict1[i]['name'])
                print('Hindi     :',dict1[i]['hin'])
                print('Malayalam :',dict1[i]['mal'])
                print('Maths     :',dict1[i]['mat'])
                print('Science   :',dict1[i]['sci'])
                print('-'*20)
                total=dict1[i]['hin']+dict1[i]['mal']+dict1[i]['mat']+dict1[i]['sci']
                print('Total     :',total)
                print('-'*20)
                avg=total/len(dict1)
                print('Average   :',avg)
                print('-'*20)
                percent=(total*100)/(len(dict1)*100)
                print('Percentage:',percent)
                print('-'*20)
    case 2:
        #name
        name=input('Enter the name:')
        name=name.lower()
        for i in dict1.keys():
            if(dict1[i]['name']==name):
                print('Details')
                print('-'*20)
                print('Name      :',dict1[i]['name'])
                print('Hindi     :',dict1[i]['hin'])
                print('Malayalam :',dict1[i]['mal'])
                print('Maths     :',dict1[i]['mat'])
                print('Science   :',dict1[i]['sci'])
                print('-'*20)
    case 3:
        #maximum mark
        top=input('Enter the subject:')
        if top == 'hindi':
            mark=0
            for i in dict1.keys():
                if(dict1[i]['hin']>mark):
                    mark=dict1[i]['hin']
            for i in dict1.keys():
                if mark==dict1[i]['hin']:
                    print('Details')
                    print('-'*20)
                    print('Name      :',dict1[i]['name'])
                    print('Hindi     :',dict1[i]['hin'])
                    print('Malayalam :',dict1[i]['mal'])
                    print('Maths     :',dict1[i]['mat'])
                    print('Science   :',dict1[i]['sci'])
                    print('-'*20)
                    total=dict1[i]['hin']+dict1[i]['mal']+dict1[i]['mat']+dict1[i]['sci']
                    print('Total     :',total)
                    print('-'*20)
                    avg=total/len(dict1)
                    print('Average   :',avg)
                    print('-'*20)
        elif top == 'malayalam':
            mark=0
            for i in dict1.keys():
                if(dict1[i]['mal']>mark):
                    mark=dict1[i]['mal']
            for i in dict1.keys():
                if mark==dict1[i]['mal']:
                    print('Details')
                    print('-'*20)
                    print('Name      :',dict1[i]['name'])
                    print('Hindi     :',dict1[i]['hin'])
                    print('Malayalam :',dict1[i]['mal'])
                    print('Maths     :',dict1[i]['mat'])
                    print('Science   :',dict1[i]['sci'])
                    print('-'*20)
                    total=dict1[i]['hin']+dict1[i]['mal']+dict1[i]['mat']+dict1[i]['sci']
                    print('Total     :',total)
                    print('-'*20)
                    avg=total/len(dict1)
                    print('Average   :',avg)
                    print('-'*20)
        if top == 'maths':
            mark=0
            for i in dict1.keys():
                if(dict1[i]['mat']>mark):
                    mark=dict1[i]['mat']
            for i in dict1.keys():
                if mark==dict1[i]['mat']:
                    print('Details')
                    print('-'*20)
                    print('Name      :',dict1[i]['name'])
                    print('Hindi     :',dict1[i]['hin'])
                    print('Malayalam :',dict1[i]['mal'])
                    print('Maths     :',dict1[i]['mat'])
                    print('Science   :',dict1[i]['sci'])
                    print('-'*20)
                    total=dict1[i]['hin']+dict1[i]['mal']+dict1[i]['mat']+dict1[i]['sci']
                    print('Total     :',total)
                    print('-'*20)
                    avg=total/len(dict1)
                    print('Average   :',avg)
                    print('-'*20)
        if top == 'science':
            mark=0
            for i in dict1.keys():
                if(dict1[i]['sci']>mark):
                    mark=dict1[i]['sci']
            for i in dict1.keys():
                if mark==dict1[i]['sci']:
                    print('Details')
                    print('-'*20)
                    print('Name      :',dict1[i]['name'])
                    print('Hindi     :',dict1[i]['hin'])
                    print('Malayalam :',dict1[i]['mal'])
                    print('Maths     :',dict1[i]['mat'])
                    print('Science   :',dict1[i]['sci'])
                    print('-'*20)
                    total=dict1[i]['hin']+dict1[i]['mal']+dict1[i]['mat']+dict1[i]['sci']
                    print('Total     :',total)
                    print('-'*20)
                    avg=total/len(dict1)
                    print('Average   :',avg)
                    print('-'*20)
    case 4:
        #minimum marks
        min=input('Enter the subject:')
        if min == 'hindi':
            mark=100
            for i in dict1.keys():
                if(dict1[i]['hin']<mark):
                    mark=dict1[i]['hin']
            for i in dict1.keys():
                if mark==dict1[i]['hin']:
                    print('Details')
                    print('-'*20)
                    print('Name      :',dict1[i]['name'])
                    print('Hindi     :',dict1[i]['hin'])
                    print('Malayalam :',dict1[i]['mal'])
                    print('Maths     :',dict1[i]['mat'])
                    print('Science   :',dict1[i]['sci'])
                    print('-'*20)
                    total=dict1[i]['hin']+dict1[i]['mal']+dict1[i]['mat']+dict1[i]['sci']
                    print('Total     :',total)
                    print('-'*20)
                    avg=total/len(dict1)
                    print('Average   :',avg)
                    print('-'*20)
        elif min == 'malayalam':
            mark=100
            for i in dict1.keys():
                if(dict1[i]['mal']<mark):
                    mark=dict1[i]['mal']
            for i in dict1.keys():
                if mark==dict1[i]['mal']:
                    print('Details')
                    print('-'*20)
                    print('Name      :',dict1[i]['name'])
                    print('Hindi     :',dict1[i]['hin'])
                    print('Malayalam :',dict1[i]['mal'])
                    print('Maths     :',dict1[i]['mat'])
                    print('Science   :',dict1[i]['sci'])
                    print('-'*20)
                    total=dict1[i]['hin']+dict1[i]['mal']+dict1[i]['mat']+dict1[i]['sci']
                    print('Total     :',total)
                    print('-'*20)
                    avg=total/len(dict1)
                    print('Average   :',avg)
                    print('-'*20)
        if min == 'maths':
            mark=100
            for i in dict1.keys():
                if(dict1[i]['mat']<mark):
                    mark=dict1[i]['mat']
            for i in dict1.keys():
                if mark==dict1[i]['mat']:
                    print('Details')
                    print('-'*20)
                    print('Name      :',dict1[i]['name'])
                    print('Hindi     :',dict1[i]['hin'])
                    print('Malayalam :',dict1[i]['mal'])
                    print('Maths     :',dict1[i]['mat'])
                    print('Science   :',dict1[i]['sci'])
                    print('-'*20)
                    total=dict1[i]['hin']+dict1[i]['mal']+dict1[i]['mat']+dict1[i]['sci']
                    print('Total     :',total)
                    print('-'*20)
                    avg=total/len(dict1)
                    print('Average   :',avg)
                    print('-'*20)
        if min == 'science':
            mark=100
            for i in dict1.keys():
                if(dict1[i]['sci']<mark):
                    mark=dict1[i]['sci']
            for i in dict1.keys():
                if mark==dict1[i]['sci']:
                    print('Details')
                    print('-'*20)
                    print('Name      :',dict1[i]['name'])
                    print('Hindi     :',dict1[i]['hin'])
                    print('Malayalam :',dict1[i]['mal'])
                    print('Maths     :',dict1[i]['mat'])
                    print('Science   :',dict1[i]['sci'])
                    print('-'*20)
                    total=dict1[i]['hin']+dict1[i]['mal']+dict1[i]['mat']+dict1[i]['sci']
                    print('Total     :',total)
                    print('-'*20)
                    avg=total/len(dict1)
                    print('Average   :',avg)
                    print('-'*20)