def solve1(inputstr):
    lst =  [x.split(",") for x in inputstr.split("\n")]
    s = 0
    for pair in lst:
        x,y = str(pair[0]).split("-"),str(pair[1]).split("-")
        x[0],x[1] = int(x[0]),int(x[1])
        y[0],y[1] = int(y[0]),int(y[1])
        if (x[0] >= y[0] and x[1] <= y[1]) or (y[0] >= x[0] and y[1] <= x[1]):
            s+=1
    print(s)

def solve2(inputstr):
    lst =  [x.split(",") for x in inputstr.split("\n")]
    s = 0
    for pair in lst:
        x,y = str(pair[0]).split("-"),str(pair[1]).split("-")
        x[0],x[1] = int(x[0]),int(x[1])
        y[0],y[1] = int(y[0]),int(y[1])
        if y[0] <= x[1] and y[1] >= x[0] :    
            s+=1
    print(s)
