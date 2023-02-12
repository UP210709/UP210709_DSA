from random import randrange

print("Numero Secreto")
print("Selecione una dificultad , 1 = FACIL(1 al 100) 2 = INTERMEDIO(1 al 500) 3 = DIFICIL(1 al 1000)")
e = int(input())
b = True
d = 0

if e == 1:
    a = randrange(1, 100)
elif e == 2:
    a = randrange(1, 500)
elif e == 3:
    a = randrange(1, 1000)


while b == True: 
    c = int(input("Dime el numero secreto: "))
    if c == a:
        b = False
        print("Felicidades... Lo hiciste en", d, "Intentos")
    elif c > a:
        print("Abajo")
        d+=1
    elif c < a:
        print("Arriba")
        d+=1