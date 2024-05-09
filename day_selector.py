while(1):
    print('0.Sunday\n1.Monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\n6.Saturday\nEnter the day number:',end='')
    day=int(input())
    match day:
        case 0:
            print('Sunday')
        case 1:
            print('Monday')
        case 2:
            print('Tuesday')
        case 3:
            print('Wednesday')
        case 4:
            print('Thursday')
        case 5:
            print('Friday')
        case 6:
            print('Saturday')
        case _:
            print('Invalid Day')