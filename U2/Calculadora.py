from tkinter import Button, Tk, Frame,Entry,END
import math

class HoverButton(Button):
	def __init__(self, master, **kw):
		Button.__init__(self,master=master,**kw)
		self.defaultBackground = self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, e):
		self["background"] = self["activebackground"]

	def on_leave(self, e):
		self["background"] = self.defaultBackground

def operaciones(n1,n2=0,op=''):
    if op=="+":
        return n1+n2
    elif op=="-":
        return n1-n2
    elif op=="*":
        return n1*n2
    elif op=="/":
        return n1/n2
    elif op =="^":
        return n1**n2
    elif op=='sen': 
        return round(math.sin(math.radians(n1)),8)
    elif op=='cos':
        return round(math.cos(math.radians(n1)),8)
    elif op=='tan':
        return round(math.tan(math.radians(n1)),8)
    elif op=='atan':
        return round(math.degrees(math.atan(n1)),8)
    elif op=='acos':
        return round(math.degrees(math.acos(n1)),8)
    elif op=='asen':
        return round(math.degrees(math.asin(n1)),8)
    elif op=='log':
        return math.log10(n1)
    elif op=='aln':
         return math.e**math.log10(n1)

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
    elif op=='sen' or op=='cos' or op=='tan' or op=='acos' or op=='asen' or op=='atan' or op=='log':
        return 4
    elif op==")":
        return 5
    elif op=="(":
        return 0

def in2pos(p,stack=[],posfix=[]):
    i=1
    p.insert(0,'(')
    p.append(')')
    stack.append('(')
    for i in range (1,len(p)):
        if isNumeric(p[i]):
            posfix.append(float(p[i])) 
        elif importancia(p[i])==5:
            while importancia(stack[-1])>0:
                posfix.append(stack.pop())
            stack.pop()
            continue
        elif importancia(p[i]) > importancia(stack[-1]) or importancia(p[i])==0:
            stack.append(p[i])
        else:
            posfix.append(stack.pop())
            stack.append(p[i])

def pos2value(posfix=[]):
    h=0
    while(len(posfix)>1):
        h=h%int(len(posfix))
        if type(posfix[h]) is str:
            op=posfix.pop(h)
            if importancia(op)!=4:
                n2=posfix.pop(h-1)
                n1=posfix.pop(h-2)
                h-=2
                posfix.insert(h,operaciones(n1,n2,op))
            else:
                n1=posfix.pop(h-1)
                h-=1
                posfix.insert(h,operaciones(n1=n1,op=op))
        h+=1

def separa(ecuacion):
    operacion=''
    for i in range(len(ecuacion)):
        if not str(ecuacion[i]).isalnum() and ecuacion[i]!='.':
            if ecuacion[i]=='-' and not isNumeric(ecuacion[i-1]) or i==0 and ecuacion[i]=='-':    
                operacion=operacion+ecuacion[i]
            else:
                operacion=operacion+' '+ecuacion[i]+' '
        else:
            operacion=operacion+ecuacion[i]
    return operacion

def borrar_uno():
	global i 
	if i==-1:
		pass
	else:
		Resultado.delete(i,last =None)
		i-=1
		
def borrar_todo():
    global i
    Resultado.delete(0, END)	
    i=0

def obtener(dato,valor=1):
	global i
	i+=valor
	Resultado.insert(i, dato)

def operacion():
    global i

    ecuacion=str(Resultado.get())
    print(ecuacion)
    ecuacion=separa(ecuacion)
    p=ecuacion.split()

    stack=[]
    result=[]
    in2pos(p,stack,result)
    pos2value(result)
    print(result)
    Resultado.delete(0,END)
    Resultado.insert(0,result)
    longitud = len(result)
    i = longitud    

i = 0

ventana = Tk()
ventana.geometry('334x380')
ventana.config(bg= "white")
ventana.resizable(0,0)
ventana.title('Hitori Goto')

frame = Frame(ventana, bg ='black', relief = "raised")
frame.grid(column=0, row=0, padx=6, pady=3)
Resultado = Entry(frame,bg='#9EF8E8', width=25, relief='groove', font = 'Montserrat 16',justif = 'right')
Resultado.grid(columnspan=5 , row=0, pady=3,padx=1, ipadx=1, ipady=1) 

#fila 1
ButtonP1 = HoverButton(frame, text= "(", borderwidth=2, height=2, width=5, font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="yellow", bg ='hot pink',  anchor="center", command=lambda: obtener('('))  
ButtonP1.grid( column= 0 ,row=1, pady=1,padx=3)
ButtonP2 = HoverButton(frame, text= ")", height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow",bg ='hot pink', anchor="center",command=lambda: obtener(')'))  
ButtonP2.grid(column =1 , row=1, pady=1,padx=1)
Button_borrar = HoverButton(frame, text= "⌫", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg = 'hot pink',  anchor="center",command=lambda: borrar_uno())  
Button_borrar.grid(column =2, row=1, pady=2,padx=2)
ButtonCsc = HoverButton(frame, text= "Asen", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink', anchor="center",command=lambda: obtener('asen(',5))  
ButtonCsc.grid(column =3, row=1, pady=1,padx=1)
Button_borrar = HoverButton(frame, text= "C", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2, relief = "raised", activebackground="yellow", bg ='hot pink', anchor="center",command=lambda: borrar_todo())  
Button_borrar.grid(column =4, row=1, pady=2,padx=2)

#fila 2
ButtonLn= HoverButton(frame, text= "Log",height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink', anchor="center",command=lambda: obtener('log(',4))  
ButtonLn.grid( column= 0 ,row=2, pady=1,padx=1)
ButtonAln = HoverButton(frame, text= "aLog", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow",bg ='hot pink', anchor="center",command=lambda: obtener('alog(',5))  
ButtonAln.grid(column =1 , row=2, pady=1,padx=1)
ButtonExp = HoverButton(frame, text= "^", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow",bg ='hot pink',  anchor="center",command=lambda: obtener('^'))  
ButtonExp.grid(column =2, row=2, pady=1,padx=1)
ButtonSec = HoverButton(frame, text= "Acos", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink',  anchor="center",command=lambda: obtener('acos(',5))  
ButtonSec.grid(column =3, row=2, pady=2,padx=2)
ButtonDiv = HoverButton(frame, text= "/", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink',  anchor="center",command=lambda: obtener('/'))  
ButtonDiv.grid(column =4, row=2, pady=2,padx=2)

#fila 3
Button7 = HoverButton(frame, text= "7",height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow",bg ='hot pink',  anchor="center",command=lambda: obtener(7))  
Button7.grid( column= 0 ,row=3, pady=1,padx=1)
Button8 = HoverButton(frame, text= "8", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow",bg ='hot pink', anchor="center",command=lambda: obtener(8))  
Button8.grid(column =1 , row=3, pady=1,padx=1)
Button9 = HoverButton(frame, text= "9", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow",bg ='hot pink',  anchor="center",command=lambda: obtener(9))  
Button9.grid(column =2, row=3, pady=1,padx=1)
ButtonCot = HoverButton(frame, text= "Atan", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink',  anchor="center",command=lambda: obtener('atan(',5))  
ButtonCot.grid(column =3, row=3, pady=2,padx=2)
Button_por = HoverButton(frame, text= "x", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink',  anchor="center",command=lambda: obtener('*'))  
Button_por.grid(column =4, row=3, pady=2,padx=2)

#fila 4
Button4 = HoverButton(frame, text= "4", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow",bg ='hot pink', anchor="center",command=lambda: obtener(4))  
Button4.grid(column =0 , row=4, pady=1,padx=1)
Button5 = HoverButton(frame, text= "5",height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow",bg ='hot pink',  anchor="center",command=lambda: obtener(5))  
Button5.grid( column= 1, row=4, pady=1,padx=1)
Button6 = HoverButton(frame, text= "6", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow",bg ='hot pink',  anchor="center",command=lambda: obtener(6))  
Button6.grid(column =2, row=4, pady=1,padx=1)
ButtonTan = HoverButton(frame, text= "Tan", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink',  anchor="center",command=lambda: obtener('tan(',4))  
ButtonTan.grid(column =3, row=4, pady=2,padx=2)
ButtonMenos = HoverButton(frame, text= "-", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink',  anchor="center",command=lambda: obtener('-'))  
ButtonMenos.grid(column =4, row=4, pady=2,padx=2)

#fila 5
Button1 = HoverButton(frame, text= "1", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink',  anchor="center",command=lambda: obtener(1))  
Button1.grid(column =0, row=5, pady=2,padx=2)
Button2 = HoverButton(frame, text= "2", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink',  anchor="center",command=lambda: obtener(2))  
Button2.grid(column =1, row=5, pady=2,padx=2)
Button3 = HoverButton(frame, text= "3", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink',  anchor="center",command=lambda: obtener(3))  
Button3.grid(column =2, row=5, pady=2,padx=2)
ButtonCos = HoverButton(frame, text= "Cos", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink',  anchor="center",command=lambda: obtener('cos(',4))  
ButtonCos.grid(column =3, row=5, pady=2,padx=2)
ButtonMas = HoverButton(frame, text= "+", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink',  anchor="center",command=lambda: obtener('+'))  
ButtonMas.grid(column =4, row=5, pady=2,padx=2)

#fila 6
Button00 = HoverButton(frame, text= "00", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink', anchor="center",command=lambda: obtener('00',2))  
Button00.grid(column =0, row=6, pady=1,padx=1)
Button0 = HoverButton(frame, text= "0", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink', anchor="center",command=lambda: obtener(0))  
Button0.grid(column =1, row=6, pady=1,padx=1)
ButtonPunto = HoverButton(frame, text= ".", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink', anchor="center",command=lambda: obtener('.'))  
ButtonPunto.grid(column =2, row=6, pady=1,padx=1)
ButtonSen = HoverButton(frame, text= "Sen", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink', anchor="center",command=lambda: obtener('sen(',4))  
ButtonSen.grid(column =3, row=6, pady=1,padx=1)
Button_igual = HoverButton(frame, text= "=", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="yellow", bg ='hot pink', anchor="center",command=lambda: operacion())  
Button_igual.grid(column =4, row=6, pady=1,padx=1)
ventana.mainloop()