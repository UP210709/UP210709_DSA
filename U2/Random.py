from random import randrange

def verificar(num,lista=[]):
    for i in range (len(lista)):
        if lista[i]==num:
            return True
    return False

def llenar(lista=[]):
    for i in range (100):
        num=randrange(100,500)
        while verificar(num,lista):
            num=randrange(100,500)
        lista.append(num)

def acomodar(lista=[]):
    v=True
    i=int(len(lista))-1
    while v:
        v=False
        for j in range (i):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
                v=True
        i-=1

def quicksort(lista,primero,ultimo):
    central=(primero+ultimo)//2
    pivote=lista[central]
    i=primero
    j=ultimo
    p=True
    
    while i<=j or p:
        p=False
        while lista[i]<pivote:
            i+=1
        while lista[j]>pivote:
            j-=1
        if i <= j:
            lista[i],lista[j]=lista[j],lista[i]
            i+=1
            j-=1
    if(primero<j):
        quicksort(lista,primero,j)
    if(i<ultimo):
        quicksort(lista,i,ultimo)
        
def binary_search(lista,num):
    LI=0
    LS=int(len(lista))-1
    mit=(LI+LS)//2
    i=1

    while LI<=LS:
        if lista[mit]<num or lista[mit]>num:
            if lista[mit]<num:
                LI=mit+1
            else:
                LS=mit-1
            mit=(LI+LS)//2
            i+=1
        else:
            break

    if lista[mit]==num:
        return mit, i
    else:
        return -1, i

lista=[]
num=randrange(100,500)
l=0

llenar(lista)
print(lista,'\n')

final=int(len(lista))-1
quicksort(lista,0,final)

#acomodar(lista)

print(lista,'\n')

for i in range(10):
    for j in range(10):
        print(lista[l],end=" ")
        l+=1
    print('')

print(binary_search(lista,num))