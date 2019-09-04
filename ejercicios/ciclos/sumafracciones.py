frac,sum,i= 5,0,0
print("Potencia\tFracción\t\tSuma")
while frac > 0.000001:
    i +=1
    frac = 1/(2**i)
    sum += frac   
    print("{0}\t\t{1}\t\t\t{2:<100}".format(i,frac,sum))