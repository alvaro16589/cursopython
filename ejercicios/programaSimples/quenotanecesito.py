c1 = int(input("Ingrese nota de certamen 1: "))
c2 = int(input("Ingrese nota de certamen 2: "))
nl = int(input("Ingrese nota de laboratorio: "))
print("Necesita nota de ",int(round(((60*3)-(3*nl*0.3)-(c1*0.7)-(c2*0.7))/0.7,0))," en el certamen 3")