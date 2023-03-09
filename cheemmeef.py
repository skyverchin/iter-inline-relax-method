import math
from tabulate import tabulate
from prettytable import PrettyTable

h = 1
n = 7
s = 2
t1 = 11
t2 = 120
e = 0.1

if 1 <= n <= 15:
    a = 3
    b = 4
elif 15 < n <= 30:
    a = 4
    b = 3 

k1 = (t2 - t1) / (b * b)
k2 = t1

t0y = k1 * pow(1,s) + k2
t2y = k1 * pow(2,s) + k2
t4y = k1 * pow(3,s) + k2

rows = 10
cols = 7

CycleArray = [[0 for j in range(cols)] for i in range(rows)]
TmpArray = [[0 for j in range(cols)] for i in range(rows)]

AbsArray = PrettyTable()
AbsArray.field_names = ["1", "2", "3", "4", "5", "6", "7"]
#AbsArray = []

MainArray = PrettyTable()
MainArray.field_names = ["k", "T11", "T21", "T12", "T22", "T13", "T23"]

p = 1 / 2 * (math.cos(math.pi / a) + math.cos(math.pi / b))     
w = 2 / (1 + math.sqrt(1 - pow(p,2)))

counter = -1

for i in range(rows):
    counter += 1
    if i == 0:
        for j in range(cols):   
            if j <= 2:
                CycleArray[i][j] = round((t1 + t2 + t0y + t0y) / 4, 2)
            elif j <= 4:
                CycleArray[i][j] = round((t1 + t2 + t2y + t2y) / 4, 2)
            else:
                CycleArray[i][j] = round((t1 + t2 + t4y + t4y) / 4, 2)
        CycleArray[i][0] = counter  
        MainArray.add_row(CycleArray[i])                
    else:
        for j in range(cols):
            if j == 1:             
                CycleArray[i][j] = round(w / 4 * (t0y + CycleArray[i-1][j+1] + t1 + CycleArray[i-1][j+2]) + (1 - w) * CycleArray[i-1][j], 2)
                TmpArray[i][j] = round(abs(CycleArray[i][j] - CycleArray[i-1][j]), 3)               
                
            if j == 2:
                CycleArray[i][j] = round(w / 4 * (t0y + CycleArray[i][j-1] + t1 + CycleArray[i-1][j+2]) + (1 - w) * CycleArray[i-1][j], 2)
                TmpArray[i][j] = round(abs(CycleArray[i][j] - CycleArray[i-1][j]), 3)
                    
            if j == 3:
                CycleArray[i][j] = round(w / 4 * (t2y + CycleArray[i-1][j+1] + t1 + CycleArray[i-1][j+2]) + (1 - w) * CycleArray[i-1][j], 2)
                TmpArray[i][j] = round(abs(CycleArray[i][j] - CycleArray[i-1][j]), 3)
                      
            if j == 4:
                CycleArray[i][j] = round(w / 4 * (t2y + CycleArray[i][j-1] + t1 + CycleArray[i-1][j+2]) + (1 - w) * CycleArray[i-1][j], 2)
                TmpArray[i][j] = round(abs(CycleArray[i][j] - CycleArray[i-1][j]), 3)
                     
            if j == 5:
                CycleArray[i][j] = round(w / 4 * (t4y + CycleArray[i][j-2] + t2 + CycleArray[i-1][j+1]) + (1 - w) * CycleArray[i-1][j], 2)
                TmpArray[i][j] = round(abs(CycleArray[i][j] - CycleArray[i-1][j]), 3)
                        
            if j == 6:
                CycleArray[i][j] = round(w / 4 * (t4y + CycleArray[i][j-2] + t2 + CycleArray[i][j-1]) + (1 - w) * CycleArray[i-1][j], 2)                    
                TmpArray[i][j] = round(abs(CycleArray[i][j] - CycleArray[i-1][j]), 3)
        if (TmpArray[i][1] and TmpArray[i][2] or TmpArray[i][3] and TmpArray[i][4] and TmpArray[i][5] or TmpArray[i][6]) <= e:   
            AbsArray.add_row(TmpArray[i])
            break
        
        CycleArray[i][0] = counter  
        MainArray.add_row(CycleArray[i])
        AbsArray.add_row(TmpArray[i]) 

#print("a = ", a," b = ",b)
#print("k1 = ", k1," k2 = ", k2)
#print("t0y = ", t0y," t2y = ", t2y," t4y = ", t4y)
#print("w = ", w," q = ", p)
print(MainArray)
AbsArray.del_row(0)
print(AbsArray)