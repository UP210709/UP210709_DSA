def operaciones(n1,n2,op):
    if op=="+":
        return n1+n2
    elif op=="-":
        return n1-n2
    elif op=="*":
        return n1*n2
    elif op=="/":
        return n1/n2
    
def importancia(op,pos):
    if op=="+" or op=="-":
        pri[1].append(1)
        pri[0].append(pos)
    elif op=="*" or op=="/" or op=="%":
        pri[1].append(2)
        pri[0].append(pos)
    elif op=="^":
        pri[1].append(3)
        pri[0].append(pos)
    elif op=="(" or op==")":
        pri[1].append(0)
        pri[0].append(pos)

Q="5 * ( 6 + 2 ) - 12 / 4"
operacion="5*(6+2)-12/4"
p=[5,6,2,'+',"*",12,4,"/","-"]
pri=[[],[]]
h=0

for i in range(int(len(p))):
    if type(p[i]) is str:
        importancia(p[i],i)

while(len(p)>1):
    h=h%int(len(p))
    if type(p[h]) is str:
        op=p.pop(h)
        n2=p.pop(h-1)
        n1=p.pop(h-2)
        h-=2
        p.insert(h,operaciones(n1,n2,op))
    h+=1

print(p)
print(pri)