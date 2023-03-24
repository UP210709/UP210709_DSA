def B_D(num,lista=[]):
    for i in range(len(lista)):
        if lista[i]==num:
            return i
    return None

def B_O(num,lista=[]):
    i=0
    while i<len(lista) and lista[i]<=num:
        if lista[i]==num:
            return i
        i+=1
    return None

lista1=[-5,2,3,6,1,9,14]
lista2=[-3,0,5,7,9,10,14]

value1=8
value2=9

print(B_D(value1,lista1))
print(B_D(value2,lista1))

print(B_O(value1,lista2))
print(B_O(value2,lista2))