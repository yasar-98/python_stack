def Biggie_Size(myList):
    for i in range(0,len(myList),1):
        if(myList[i]>=0):
            myList[i]="big"
    print(myList)
    return myList

def Count_Positives(myList):
    c=0
    for i in range(0,len(myList),1):
        if(myList[i]>0):
            c+=1
    myList[-1]=c
    print(myList)
    return myList

def Sum_Total(myList):
    s=0
    for i in range(0,len(myList),1):
        s+=myList[i]
    print(s)
    return s

def average(myList):
    s=0
    avg=0
    for i in range(0,len(myList),1):
        s+=myList[i]
    avg=s/len(myList)
    print(avg)
    return avg

def length(myList):
    l=0
    for i in range(0,len(myList),1):
        l+=1
    print(l)
    return l

def minimum(myList):
    mini=myList[0]
    for i in range(0,len(myList),1):
        if myList[i]<mini:
            mini=myList[i]
    print(mini)
    return mini

def maximum(myList):
    maxi=myList[0]
    for i in range(0,len(myList),1):
        if myList[i]>maxi:
            maxi=myList[i]
    print(maxi)
    return maxi

def Ultimate_Analysis(myList):
    y={'sumTotal': Sum_Total(myList), 'average': average(myList), 'minimum': minimum(myList), 'maximum': maximum(myList), 'length': length(myList) }
    print(y)
    return y

def Reverse_List(myList):
    size = len(myList)
    c=size-1
    for i in range(0,size):
        if c<i:
            break
        myList[c],myList[i] =myList[i], myList[c]
        
        c-=1

    print(myList)
    return myList
Reverse_List([37,-2,1,9])
