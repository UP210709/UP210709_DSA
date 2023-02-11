p=str(input("Give me a word: "))
PC=True
p2=""

for i in range (len(p)):
    if p[i].isspace:
        continue
    else:
        p2=p[i]

for i in range (int(len(p2))//2):
    if p2[i]!=p2[-i-1]:
        PC=False

if PC:
    print("Es palindromo")
else:
    print("No es palindromo")