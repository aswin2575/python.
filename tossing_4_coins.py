#tossing 4 coins
#print all pairs 
for i in range (1,3):
    for j in range(1,3):
        for k in range (1,3):
            for l in range (1,3):
                if i%2==1:
                    print('H',end='')
                else:
                    print('T',end='')
                if j%2==1:
                    print('H',end='')
                else:
                    print('T',end='')
                if k%2==1:
                    print('H',end='')
                else:
                    print('T',end='')
                if l%2==1:
                    print('H')
                else:
                    print('T')