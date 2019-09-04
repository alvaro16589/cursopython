sec = int(input("Ingrese un número: "))
def printcol(sec,sw):
    a = []
    c = 0
    while True:
        a.append(sec)
        c += 1
        if sec==1:
            break
        if sec % 2 == 0:
            sec = sec // 2
        else:
            sec = sec * 3 + 1
    if sw == 1:
        print(a)
    else: 
        return c
printcol(sec,1)
for i in range(1,sec+1):
    print(i,"\t","*"*printcol(i,0))