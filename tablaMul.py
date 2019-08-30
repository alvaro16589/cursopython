#la tabla de multiplicar
a = int(input("Se imprimirá la tabla de multiplicar de : "))
for i in range (1,11):
    if a*i <10:
        print(a, " x ", i ," =  ", a*i,"\t\t", a+1, " x ", i ," =  ", (a+1)*i,"\t", a+2, " x ", i ," =  ", (a +2)*i,"\t" ,a+3, " x ", i ," =  ", (a+3)*i )
    else:
        print(a, " x ", i ," =  ", a*i,"\t", a+1, " x ", i ," =  ", (a+1)*i,"\t", a+2, " x ", i ," =  ", (a +2)*i,"\t" ,a+3, " x ", i ," =  ", (a+3)*i )