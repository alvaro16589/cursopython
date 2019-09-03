op = 1
tt = 0
while op!= 0:
    op = int(input("Tiempo de tramo(min) = "))
    tt = tt + op
print("Tiempo total del viaje es {0}:{1} horas".format(tt//60,int((tt/60-float(tt//60))*60 )))   
