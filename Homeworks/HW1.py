import random
matrix= [[1,1,1],[1,1,1],[1,1,1]] 
for i in range(3):
    for j in range(3):
        while True:
            x=0
            randomnumber=random.randint(2,100)
            if randomnumber==2:
                matrix[i][j]=randomnumber
                break
            else:
                for k in range (2, randomnumber):
                    if randomnumber%k==0:
                        x=1
                        continue
                if x==1:
                    continue
                else:   
                    matrix[i][j]=randomnumber
                    break        
print(matrix)