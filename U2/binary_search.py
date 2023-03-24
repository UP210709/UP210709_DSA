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
    

lista=[-3,-2,-1,0,1,2,3]
print(binary_search(lista,2))