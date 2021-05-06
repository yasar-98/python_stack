for i in range(0,150,1):
    print(i)

for i in range(5,1000,5):
    print(i)

for i in range(1,100,1):
    if(i%5==0):
        print("Coding")
    if(i%10==0):
        print("Coding dojo")
    else:
        print(i)
s=0
for i in range(1,500000,2):
    s=s+i
print(s)

for i in range(2018,0,-4):
    print(i)

def Flexible_Counter(lowNum,highNum,mult):
    for i in range(lowNum,highNum+1,1):
        if(i%mult==0):
            print(i)
Flexible_Counter(2,9,3)