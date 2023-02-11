from random import randrange
matriz=[]
diagonal1=[]
diagonal2=[]
a=[]
t=4
p=0

while int(len(a))<(t*t):
    v=True
    n=randrange(1,50)
    for j in range(len(a)):
        if n==a[j]:
            v=False
    if v:
        a.append(n)

for i in range (t):
    matriz.append([])
    for j in range(t):
        matriz[i].append(a[p])
        p+=1

for i in range (len(matriz)):
    diagonal1.append(matriz[i][i])

for i in range (len(matriz)):
    diagonal2.append(matriz[i][-i-1])

print(matriz)
print(diagonal1)
print(diagonal2)
