dat = int(input("Ingrese un  valor: "))
div = []
for i in range(1,dat+1):
    if dat%i==0:
        div.append(i)
print("Los divisores son: ", div)