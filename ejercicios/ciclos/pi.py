n = int(input("Ingrese el valor de n: "))
pi = 0.0
sw = 1
c, i = 0, 1
while c != n :
    if sw==1:
        pi = pi + float(1/i)
        sw = 0
    else:
        pi = pi - float(1/i)
        sw = 1
    i = i + 2
    c += 1
print("el valor de \'pi\' con ",n," elementos en su serie es: ",pi*4)
