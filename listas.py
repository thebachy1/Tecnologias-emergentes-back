lista=[]
n=int(input("Indica la cantidad de elementos en la lista\n"))
for i in range(0,n):
    values=int(input(str(i)+") Lista:"))
    lista.append(values)

def cubo(array):
    for i in range(len(array)-1):
        array[i]=array[i]**3

    return array

print("Dividir e imprimir lista: ",lista[:round(len(lista)/2)], lista[round(len(lista)/2):],'\n')
print("Imprimir el primer y ultimo valor de la lista: ",lista[0::len(lista)-1],'\n')

lista=lista+lista
print("Agregando valores al final de la lista: ",lista,'\n')

lista.sort()
print("Lista de menor a mayor: ",lista,'\n')
lista.reverse()
print("Lista de mayor a menor: ",lista,'\n')

lista=cubo(lista)
print("El cubo de la lista: ",lista,'\n')