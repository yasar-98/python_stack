def Countdown(x) :
    myList=[]
    for i in range(x,-1,-1):
        myList.append(i)
    print(myList)

def Print_and_Return(myList) :
    if len(myList)==2:
        print(myList[0])
        return(myList[1])

def First_Plus_Length(myList):
    return myList[0]+len(myList)

def Value_Greater_than_Second(myList):
    NList=[]
    for i in range(0,len(myList),1):
        if myList[i]>myList[1]:
            NList.append(myList[i])
    print(len(NList))
    if len(NList)<2 :
        return False
    else:
        return NList

def length_value(siz,valu):
    myList=[]
    for i in range(0,siz,1):
        myList.append(valu)
    return myList

