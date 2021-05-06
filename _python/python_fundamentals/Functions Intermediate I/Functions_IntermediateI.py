import random
def randInt(min=0 , max=0 ):
    if max!=0 and min!=0:
        num = random.random()*max-min
    elif max!=0:
        num = random.random()*max
    elif min!=0:
        num = random.random()*100-min
    else:
        num = random.random()*100
    return num

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))

