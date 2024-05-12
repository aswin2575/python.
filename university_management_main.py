import random
#Student details
dict1={'ASI21CS039' :{'first_name':'aswin','last_name':'babu','dob':'26-03-2003','phone':9061453710,'mail':'aswinbabu@gmail.com','degree':'BTECH CSE','batch':'2021-2025'},
       'ASI21CS042' :{'first_name':'bilal','last_name':'basheer','dob':'03-05-2002','phone':9064573710,'mail':'bilalvb@gmail.com','degree':'BTECH CIVIL','batch':'2020-2024'},
       'ASI21CS032' :{'first_name':'arjun','last_name':'ka','dob':'17-07-2003','phone':9456453710,'mail':'arjunka@gmail.com','degree':'BTECH ME','batch':'2022-2026'},
       'ASI21CS026' :{'first_name':'ansif','last_name':'mshamsu','dob':'23-09-2003','phone':9061453758,'mail':'ansifmshamsu@gmail.com','degree':'BTECH CSE','batch':'2021-2025'}}

course={'CSE':{'core':['CST302','CST304','CST306','CSL362'],'nocredit':['HUT300','CST308']},
        'CIVIL':{'core':['CET302','CET304','CET306','CEL362'],'nocredit':['HUT300','CET308']},
        'ME':{'core':['MET302','MET304','MET306','MEL362'],'nocredit':['HUT300','MET308']}}

subject={'CST302':{'name':'compiler_design','credit':4},
         'CST304':{'name':'computer_graphi','credit':4},
         'CST306':{'name':'algorithm_analy','credit':4},
         'CSL362':{'name':'computer_python','credit':3},
         'HUT300':{'name':'common_economic','credit':3},
         'CST308':{'name':'computer_viva__','credit':1},
         'CET302':{'name':'civil_design___','credit':4},
         'CET304':{'name':'civil_graphics_','credit':4},
         'CET306':{'name':'civil_analysis_','credit':4},
         'CEL362':{'name':'civil_python___','credit':3},
         'CET308':{'name':'civil_viva_____','credit':1},
         'MET302':{'name':'mech_design____','credit':4},
         'MET304':{'name':'mech_graphics__','credit':4},
         'MET306':{'name':'mech_analysis__','credit':4},
         'MEL362':{'name':'mech_python____','credit':3},
         'MET308':{'name':'mech_viva______','credit':1},}

while(1):
    choice=int(input('1.Student details\n2.Add new student\n3.Course details\n4.Timetable\n5.Exit\nEnter the choice:'))
    if choice==1:
        reg=input("Enter the reg number:")
        for reg_no in dict1.keys():
            if reg_no==reg:
                print('Details:')
                print('-'*50)
                print('Name         :',dict1[reg_no]['first_name'],'',dict1[reg_no]['last_name'])
                print('Date of birth:',dict1[reg_no]['dob'])
                print('Phone Number :',dict1[reg_no]['phone'])
                print('Email        :',dict1[reg_no]['mail'])
                print('Degree       :',dict1[reg_no]['degree'])
                print('Batch        :',dict1[reg_no]['batch'])
    elif choice==2:
        #adding new user 
        register_num=input('Enter the register number:')
        firstname=input('Enter the first name:')
        lastname=input('Enter the last name:')
        dob=input('Enter the date of birth:')
        cell=int(input('Enter the phone number:'))
        email=input('Enter the email address:')
        deg=input('Enter the degree:')
        batchh=input('Enter the batch:')
        temp={}
        temp['first_name']=firstname
        temp['last_name']=lastname
        temp['dob']=dob
        temp['phone']=cell
        temp['mail']=email
        temp['degree']=deg
        temp['batch']=batchh
        dict1[register_num]=temp
    elif choice==3:
        while(1):
            cchoice=int(input('1.Computer Science\n2.Civil\n3.Mechanical\n4.exit\nEnter the choie:'))
            if cchoice==1:
                print('-'*30)
                print('Computer Science')
                print('Core subjects')
                for i in course['CSE']['core']:
                    print(subject[i]['name'],'credit:',subject[i]['credit'])
                print('Less credit subjects')
                for i in course['CSE']['nocredit']:
                    print(subject[i]['name'],'credit:',subject[i]['credit'])
                print('-'*30)
            elif cchoice==2:
                print('-'*30)
                print('Civil')
                print('Core subjects')
                for i in course['CIVIL']['core']:
                    print(subject[i]['name'],'credit:',subject[i]['credit'])
                print('Less credit subjects')
                for i in course['CIVIL']['nocredit']:
                    print(subject[i]['name'],'credit:',subject[i]['credit'])
                print('-'*30)
            elif cchoice==3:
                print('-'*30)
                print('Mechanical')
                print('Core subjects')
                for i in course['ME']['core']:
                    print(subject[i]['name'],'credit:',subject[i]['credit'])
                print('Less credit subjects')
                for i in course['ME']['nocredit']:
                    print(subject[i]['name'],'credit:',subject[i]['credit'])
                print('-'*30)
            elif cchoice==4:
                break
    elif choice==4:
        while(1):
            tchoice=int(input('1.Computer science\n2.Civil\n3.Mechanical\n4.Exit\nEnter the choice:'))
            if tchoice==1:
                print('-'*30)
                print('Computer Science Timetable')
                print('Day\t\t1st\t\t\t2nd\t\t\t3rd\t\t\t4th\t\t\t5th\t\t\t6th\t\t\t7th')
                temp=[]
                for sub in course['CSE']['core']:
                    temp.append(sub)
                for sub in course['CSE']['nocredit']:
                    temp.append(sub)
                print(f'Mon\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
                print(f'Tue\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
                print(f'Wed\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
                print(f'Thu\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
                print(f'Fri\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
            elif tchoice==2:
                print('-'*30)
                print('Civil Timetable')
                print('Day\t\t1st\t\t\t2nd\t\t\t3rd\t\t\t4th\t\t\t5th\t\t\t6th\t\t\t7th')
                temp=[]
                for sub in course['CIVIL']['core']:
                    temp.append(sub)
                for sub in course['CIVIL']['nocredit']:
                    temp.append(sub)
                print(f'Mon\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
                print(f'Tue\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
                print(f'Wed\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
                print(f'Thu\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
                print(f'Fri\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
            elif tchoice==3:
                print('-'*30)
                print('Mechanical Timetable')
                print('Day\t\t1st\t\t\t2nd\t\t\t3rd\t\t\t4th\t\t\t5th\t\t\t6th\t\t\t7th')
                temp=[]
                for sub in course['ME']['core']:
                    temp.append(sub)
                for sub in course['ME']['nocredit']:
                    temp.append(sub)
                print(f'Mon\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
                print(f'Tue\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
                print(f'Wed\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
                print(f'Thu\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
                print(f'Fri\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}\t\t{subject[random.choice(temp)]["name"]}')
            elif tchoice==4:
                break
    elif choice==5:
        break    