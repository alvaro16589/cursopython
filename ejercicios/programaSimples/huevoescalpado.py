from math import pi,log
t0 = float(input("Ingrese la temperatura inicial del huevo: ")) 
m = int(input("El huevo es grande (1) o pequeño (0) : "))
if m == 1:
    m = 67
else: 
    m = 47
tiempo = round((((m**(2/3))*3.7*(1.038**(1/3)))/((5.4*10**-3)*(pi**2)*((4*pi/3)**(2/3))))*log(0.76*((t0-100)/(70-100))),1)
print("El tiempo máximo para que el huevo este listo es de ",tiempo," segundos lo que equivale a ",tiempo/60," minutos.")