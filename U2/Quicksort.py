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

lista=[4,5,6,9,8,7,2,3,1]
final=int(len(lista))-1
quicksort(lista,0,final)
print(lista)