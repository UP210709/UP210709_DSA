#Primer problema: recorrer los datos dentro de una lista
def recorrerD(lista,mov):
    for i in range (mov):
        num=lista[-1]
        for j in range(len(lista)):
            lista[j],num=num,lista[j]

lista=[1,2,3,4,5,6,7,8,9]
recorrerD(lista,5)
print(lista)


#Segundo problema: Verificar que un prblema este balanceado (parrentesis correspondientes)
def balanceado(ecuacion):
    bal=0
    for i in range(len(ecuacion)):
        if ecuacion[i]=='(':
            bal+=1
        elif ecuacion[i]==')':
            bal-=1
        if bal<0:
            return False
    if bal!=0:
        return False
    else:
        return True

lista=['(())()','(()','())(','(a*+())b()']

for i in range(len(lista)):
    print(balanceado(lista[i]))