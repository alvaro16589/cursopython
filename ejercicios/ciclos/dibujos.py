op=1
print("···············································································")
print(".                                 MENÚ                                        .")
print(".  1> Dibujar un rectángulo                                                   .")
print(".  2> Dibujar un triángulo                                                    .")
print(".  3> Dibujar un Hexágono                                                     .")
print(".  0> Salir                                                                   .")
print("···············································································")
while op!=0:
    op = int(input("QUE OPCIÓN DEL MENÚ DESEA EJECUTAR  :> "))
    if op == 1:
        print("Dibujar un rectangulo:".center(105))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(100))
        alto = int(input("Alto : "))
        anch = int(input("Ancho : "))
        for i in range(alto):
            print("*"*anch)
    elif op == 2:
        print("Dibujar un triángulo:".center(105))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(100))
        al = int(input("Alto : "))
        for i in range(al+1):
            print("*"*i)
    elif op == 3:
        print("Dibujar un hexágono:".center(105))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(100))
        lado = int(input("Lado : "))
        for i in range((lado*2)-1):
            if i>=lado:
                print(" "*(i-(lado-2))+"*"*((lado*2-2)-i)+"*"*lado+"*"*((lado*2-2)-i))
            else:
                print(" "*(lado-i)+"*"*i+"*"*lado+"*"*i)