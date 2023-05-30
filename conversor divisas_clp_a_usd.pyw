# -*- coding: utf-8 -*-


from tkinter import *

ventana = Tk()
ventana.geometry("400x300")
ventana.resizable(width=0, height=0)
ventana.title("CONVERSOR DIVISAS")
ventana.configure(bg="#C4F2FF")
#___________________________________________________
#valor dolar 30/05/2023, 1 dolar = 807.99 clp

def conversor_clp_dolar():
    valor_dolar = 807.99
    clp = txt_1.get()
    total = float(clp)/float(valor_dolar)
    total_redondeado = round(total, 2)
    txt_2.delete(0,END)
    txt_2.insert(0,total_redondeado)
    
def conversor_dolar_clp():
    valor_dolar_2=807.99
    dollar = txt_2.get()
    total_2 = float(dollar)*float(valor_dolar_2)
    total_redondeado_2= round(total_2, 2)
    txt_1.delete(0, END)
    txt_1.insert(0,total_redondeado_2)
    
    
divisa_1 = Label(ventana, text= "Peso Chileno")
divisa_1.place(x=40, y=70,width=100, height=30)
txt_1 = Entry(ventana,bg="pink")
txt_1.place(x=40, y=100, width=100, height=30)

divisa_2 = Label(ventana, text= "Dolar")
divisa_2.place(x=260, y=70,width=100, height=30)
txt_2 = Entry(ventana,bg="pink")
txt_2.place(x=260, y=100, width=100, height=30)

boton_clp_a_dolar= Button(ventana, text="Clp a Dolar",command=conversor_clp_dolar)
boton_clp_a_dolar.place(x=55, y=140, width=70, height=30)

conversor= Button(ventana, text="CONVERTIR")
conversor.place(x=160, y=140, width=70, height=30)

boton_dolar_a_clp= Button(ventana, text="Dolar a Clp", command=conversor_dolar_clp)
boton_dolar_a_clp.place(x=275, y=140, width=70, height=30)

resultado=Entry(ventana,bg="pink")
resultado.place(x=145 , y=180, width=100, height=30)





ventana.mainloop()


