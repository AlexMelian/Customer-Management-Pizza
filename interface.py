from tkinter import Button, Label, Grid, Entry, Pack, DISABLED, Listbox, Tk, Frame, StringVar, Scrollbar, IntVar, Toplevel



code_error = {
    1:"Debe colocar solamente números en la cantidad de pizzas",
    2:"error2",
    3:"error3",
    4:"error4"
}


def Confirm_Order(Muza, Cala, Napo):
    try:
        Name = NameEntry.get()
        Subt = Subtotal.get()
    except:
        print("Ocurrió un error")
    else:
        text_window = "Confirma Muzza:{}  Napo: {}  Cala: {}\n Costo total {} a nombre de {}".format(Muza, Napo, Cala, Subt, Name)
        window_error = Toplevel(raiz)
        window_error.title("Confirm")
        Label(window_error, text = text_window).pack()
        Button(window_error, text = "Aceptar", command =lambda: accepted(Muza, Napo, Cala, Subt, Name)).pack()
        Button(window_error, text = "Aceptar", command =lambda: window_error.destroy).pack()
        window_error.geometry("400x80")
        window_error.grab_set()
        window_error.transient(raiz)
        raiz.wait_window(window_error)

def acepted(Muza, Napo, Cala, Subt, Name):


def test(n):
    print("funca ", n)


def Calculate_Price(Nmuza, Ncala, Nnapo):
    Total = Nmuza*100 + Nnapo*120 + Ncala*140
    return Total

def hCalculate(n):
    print("llama la funcion")
    try:
        Muza = MuzzaEntry.get()
        Cala = CalabresaEntry.get()
        Napo = NapolitanaEntry.get()

    except:
        print("Ocurririo un error")
        Errors(1)
    else:
        x = Calculate_Price(Muza, Cala, Napo)
        Subtotal.set(x)
        if n==0:
            Confirm_Order(Muza, Cala, Napo)

def Errors(n):
    text_error = code_error[n]
    window_error = Toplevel(raiz)
    window_error.title("Error")
    Label(window_error, text = text_error).pack()
    Button(window_error, text = "Aceptar", command =lambda: window_error.destroy).pack()
    window_error.geometry("400x50")
    window_error.grab_set()
    window_error.transient(raiz)
    raiz.wait_window(window_error)

raiz = Tk()
NameEntry = StringVar()
NumberPizzaEntry = IntVar()
Subtotal = IntVar()
MuzzaEntry = IntVar()
NapolitanaEntry = IntVar()
CalabresaEntry = IntVar()
NumberOfOrder = IntVar(value=1)
#raiz.iconbitmap('./pizza.ico')
raiz.title("ProyectoPizza")
raiz.geometry("600x400")
MiFrame=Frame()
#MiFrame.pack(fill="both")
MiFrame.pack()
#Mi label
Label(MiFrame,text="Muzzarela:").grid(row=0,column=0)
Label(MiFrame,text="Napolitana:").grid(row=1,column=0)
Label(MiFrame,text="Calabresa:").grid(row=2,column=0)
Label(MiFrame,text="Nombre del cliente:").grid(row=3,column=0)
Label(MiFrame,text="Cantidad de pizzas:").grid(row=4,column=0)
Label(MiFrame,text="Precio total:").grid(row=5,column=0)
Label(MiFrame,text="Numero de pedido:").grid(row=6,column=0)
#Text Entry
Entry(MiFrame,textvariable=MuzzaEntry).grid(row=0,column=1)
Entry(MiFrame,textvariable=NapolitanaEntry).grid(row=1,column=1)
Entry(MiFrame,textvariable=CalabresaEntry).grid(row=2,column=1)
Entry(MiFrame,textvariable=NameEntry).grid(row=3,column=1)
Entry(MiFrame,state=DISABLED,textvariable=NumberPizzaEntry).grid(row=4,column=1)
Entry(MiFrame,state=DISABLED,textvariable=Subtotal).grid(row=5,column=1)
Entry(MiFrame,state=DISABLED,textvariable=NumberOfOrder).grid(row=6,column=1)
#List Orders
ListaPedidos=Listbox(MiFrame,heigh=10)
ListaPedidos.grid(row=0,column=4,rowspan=10)
#Scroll
scrollista=Scrollbar(MiFrame,command=ListaPedidos.yview)
scrollista.grid(row=0,column=5,rowspan=10,sticky="nsew")
ListaPedidos.config(yscrollcommand=scrollista.set)
#Buttons import export
Button(MiFrame,text="Importar datos",command=lambda: test(1)).grid(row=8,column=0)
Button(MiFrame,text="Exportar datos",command=lambda: test(2)).grid(row=8,column=1)
Button(MiFrame,text="Finalizar dia",command=lambda: test(3)).grid(row=8,column=2)
#Button down
Button(MiFrame,text="Calcular precio",command=lambda: hCalculate(1)).grid(row=7,column=0)
Button(MiFrame,text="Cancelar pedido",command=lambda: test(5)).grid(row=7,column=1)
Button(MiFrame,text="Confirmar pedido",command=lambda: hCalculate(0)).grid(row=7,column=2)
raiz.mainloop()