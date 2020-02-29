import os

def allTriangles(base):
    numOfT = 0
    if base == 1:
        return numOfT

    elif base == 2:
        numOfT += 1
        return numOfT 
    
    else:
        for item in range(0, base):
            numOfT += item 
        numOfT += 1
        return numOfT

while True:
    try:
        base = int(input("Base Length: "))
        os.system('cls')
        print("That can form %s triangles" % (allTriangles(base)))

    except:
        print("Invalid Input")
    
    
