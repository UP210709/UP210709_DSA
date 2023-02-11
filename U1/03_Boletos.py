n=1000
x=0
dinero=0

while dinero<=n:
    x=x+1
    dinero=dinero+x

dinero=n-(dinero-x)
x=x-1

print(x," Boletos")
print("Te sobra ",dinero)