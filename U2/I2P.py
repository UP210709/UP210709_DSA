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

q="5 * ( 6 + 2 ) - 12 / 4"
p=q.split()
stack=[]
posfix=[]
i=1

p.insert(0,'(')
p.append(')')
stack.append('(')

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

print(posfix)
print(stack)