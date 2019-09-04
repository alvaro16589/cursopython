from math import factorial as fac
dif, i, ant, eu = 5.0, 0, 0.0, 0.0
while dif > 0.0001:
    eu = eu + 1 / fac(i)
    dif = eu - ant
    ant = eu
    i += 1
print ("el numero de eule obtenido: {0}".format(eu))