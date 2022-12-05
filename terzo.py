def solve1(stringa):
    ls = [[x[:len(x)//2],x[len(x)//2:]] for x in stringa.split("\n")] 
    s = 0
    for lista in ls:
        u = "".join(set(lista[0]).intersection(set(lista[1])))
        print(u)
        if u.islower():
            s+=ord(u)-96
        else:
            s+=ord(u)-64+26

    print(s)

def solve2(stringa):
    ls = stringa.split("\n")
    lsg = []
    ltemp = []
    for x in range(len(ls)):
        if (x+1) % 3 == 0:
            ltemp.append(ls[x])
            lsg.append(ltemp)
            ltemp = []
        else:
            ltemp.append(ls[x])
    s = 0
    for gruppo in lsg:
        u = set(gruppo[0]).intersection(set(gruppo[1]))
        u = "".join(u.intersection(gruppo[2]))
        if u.islower():
            s+=ord(u)-96
        else:
            s+=ord(u)-64+26

    print(s)        
