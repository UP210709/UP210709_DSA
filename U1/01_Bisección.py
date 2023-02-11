def fnEcuacion1(x):     # x'2-8x+15
    r = float
    r = (x**2)-(8*x)+15
    return r

x1 = 4
x2 = 7
xm = float

Es = 0.0001
Er = abs(x2-x1)
i = 0

while Er > Es:
    xm = (x1+x2)/2
    y1 = fnEcuacion1(x1)
    y2 = fnEcuacion1(xm)
    if y1*y2 < 0:
        x2 = xm
    else:
        x1 = xm
    Er = abs(x2-x1)
    i = i+1

print(f"i= {i}, raiz = {xm}")