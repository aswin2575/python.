# dices=[[1,2,3,4,5,6],
#        [1,2,3,4,5,6],
#        [1,2,3,4,5,6]]
# for dice in dices:
#     dices[5]
dice=[1,2,3,4,5,6]
total=0
for i in dice:
    for j in dice:
        for k in dice:
            if(i==j==k==6):
                print(i,j,k)
            total=total+1
propability=1/total
print(propability)
#print(total)
            