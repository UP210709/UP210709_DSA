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
    elif op=="(" or op==")":
        return 0

q="5 * ( 6 + 2 ) - 12 /"
p=q.split()
stack=[]
infix=[]

p.insert(0,'(')
p.append(')')

for i in range (len(p)):
    if isNumeric(p[i]):
        infix.append(p[i])

print(infix)