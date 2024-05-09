#rollno,name,eng,mal,maths,science
data=[[1,'aswin',45,67,87,45],
      [2,'bilal',44,37,57,75],
      [3,'arjun',32,87,97,65],
      [4,'ansif',25,77,37,55]]
# print(data)
# for i in data:
#     print(i,i[1])
while(1):
    choice=int(input('1.Roll number\n2.Name\n3.MAX mark\n4.Min mark\nEnter the choice:'))
    match choice:
        case 1:
            roll=int(input('Enter the number:'))
            for student in data:
                if(student[0]==roll):
                    print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
                else:
                    print('Invalid')
        case 2:
            name=input('Enter the name:')
            for student in data:
                if(student[1]==name):
                    print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
                    break
                else:
                    print('INVALID')
                    break
        case 3:
            sub=input('Enter the subject:')
            sub=sub.lower()
            mark=0
            if sub=='english':
                for student in data:
                    if(student[2]>mark):
                        mark=student[2]
                for student in data:
                    if student[2]==mark:
                        print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
                break
            if sub=='malayalam':
                for student in data:
                    if(student[3]>mark):
                        mark=student[3]
                for student in data:
                    if student[3]==mark:
                        print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
                break
            if sub=='maths':
                for student in data:
                    if(student[4]>mark):
                        mark=student[4]
                for student in data:
                    if student[4]==mark:
                        print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
                break
            if sub=='science':
                for student in data:
                    if(student[5]>mark):
                        mark=student[5]
                for student in data:
                    if student[5]==mark:
                        print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
            else:
                print('Invalid')
        case 4:
            sub=input('Enter the subject:')
            sub=sub.lower()
            mark=100
            if sub=='english':
                for student in data:
                    if(student[2]<mark):
                        mark=student[2]
                for student in data:
                    if student[2]==mark:
                        print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
                break
            if sub=='malayalam':
                for student in data:
                    if(student[3]<mark):
                        mark=student[3]
                for student in data:
                    if student[3]==mark:
                        print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
                break
            if sub=='maths':
                for student in data:
                    if(student[4]<mark):
                        mark=student[4]
                for student in data:
                    if student[4]==mark:
                        print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
                break
            if sub=='science':
                for student in data:
                    if(student[5]<mark):
                        mark=student[5]
                for student in data:
                    if student[5]==mark:
                        print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
            else:
                print('Invalid')
        case _:
            print('invalid')


# for student in data:
#     if(student[0]==roll):
#         print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')


# for student in data:
#     roll=student[0]
#     match roll:
#         case 1:
#             print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
#         case 2:
#             print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
#         case 3:
#             print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
#         case 4:
#             print(f'Details \nName:{student[1]} English:{student[2]} Malayalam:{student[3]} Maths:{student[4]} Science:{student[5]}')
#         case _:
#             print("INVALID")