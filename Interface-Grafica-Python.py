from tkinter import*
from tkinter import messagebox
import sys


##obrigatório inicializar##
res=0


##função de soma ##
def soma():

 num1 = float(caixaNumero1.get())
 num2 = float(caixaNumero2.get())
 res=num1+num2

 ##jogar valor no label declarado lá embaixo##
 lb["text"] = num1 + num2


##mensagem semelhante ao joptionpane##
 messagebox.showinfo("res",res)



##construção da janela##

app = Tk()

##title da janela##
app.title("Etec")

##dimensões da janela##
app.geometry("500x300")


##configuração do  1 label##
##ancho localização de acordo com bussola##
##place localização eixo x e y##
label1 = Label(app ,text='Digite o 1 número:',anchor=W).place(x=10,y=10)



##configuração da 1 caixa de txto##
##ancho localização de acordo com bussola##
##width - largura ##
##height - altura ##
##place localização eixo x e y##
caixaNumero1 = Entry(app)
caixaNumero1.place(x=10,y=30,width=200,height=20)


##configuração do  2 label##
##ancho localização de acordo com bussola##
##place localização eixo x e y##

label2 = Label(app , text='Digite o 2 número:',anchor=W).place(x=10,y=60)


##configuração da 2 caixa de txto##
##ancho localização de acordo com bussola##
##width - largura ##
##height - altura ##
##place localização eixo x e y##

caixaNumero2 = Entry(app)
caixaNumero2.place(x=10,y=80,width=200,height=20)


##command=ação , função ,metodo##
## comand é o nome da função sem aspas##
button1 = Button(app,text="Somar",command=soma).place(x=10,y=120,width=100,height=20)


##label para exibição dos dados##
Label(app, text="Resultado =").place(x=50, y=180)
lb=Label(app, text="")
lb.place(x=120, y=180)




##executar aplicação##
app.mainloop()