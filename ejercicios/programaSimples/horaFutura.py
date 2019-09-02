hac = int(input("Hora actual : "))
ch = int(input("Cantidad de horas: "))
print("En ",ch," horas, el reloj marcará las ", (hac+ch)%24)