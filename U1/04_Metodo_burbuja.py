a = [5,2,7,9,3,4,6]

print(a)

for i in range(0, len(a)-1):
    for j in range(0,len(a)-1 - i):
        x=a[j]
        y=a[j+1]
        if x>y:
            a[j]=y
            a[j+1]=x

print(a)