def operaciones(n1,n2,op):
    if op=="+":
        return n1+n2
    elif op=="-":
        return n1-n2
    elif op=="*":
        return n1*n2
    elif op=="/":
        return n1/n2
    
def isNumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def importancia(op):
    if op=="+" or op=="-":
        return 1
    elif op=="*" or op=="/" or op=="%":
        return 2
    elif op=="^":
        return 3
    elif op==")":
        return 4
    elif op=="(":
        return 0

def i2p(p,stack=[],posfix=[]):
    i=1
    while i<int(len(p)):
        if isNumeric(p[i]):
            posfix.append(float(p[i])) 
        elif importancia(p[i])==4:
            while importancia(stack[-1])>0:
                posfix.append(stack.pop())
            stack.pop()
        elif importancia(p[i]) >= importancia(stack[-1]) or importancia(p[i])==0:
            stack.append(p[i])
        else:
            posfix.append(stack.pop())
            stack.append(p[i])
        i+=1

Q="5 * ( 6 + 2 ) - 12 / 4"
p=Q.split()

stack=[]
posfix=[]

p.insert(0,'(')
p.append(')')
stack.append('(')

i2p(p,stack,posfix)

h=0
while(len(posfix)>1):
    h=h%int(len(posfix))
    if type(posfix[h]) is str:
        op=posfix.pop(h)
        n2=posfix.pop(h-1)
        n1=posfix.pop(h-2)
        h-=2
        posfix.insert(h,operaciones(n1,n2,op))
    h+=1

print(posfix)
