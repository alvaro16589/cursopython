def invertir(x):
    a = int(x)
    invert = 0
    for  i in range(len(x),0,-1):
        invert = invert + ((10**(i-1) ) *( a%10))
        a = a//10
    return invert

num = input("Ingrese un número para invertir: ")
invert = ""
for i in num:
    invert = i + invert
print("El número invertido es : ",invert,invertir(num)) 


