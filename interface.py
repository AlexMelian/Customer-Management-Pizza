from tkinter import Button, Label, Grid, Entry, Pack, DISABLED, Listbox, Tk, Frame, StringVar, Scrollbar
import functions

def window():
    raiz = Tk()
    NombreEntry=StringVar(value=1)
    CanpizzaEntry=StringVar(value=1)
    TotalParcial=StringVar(value=1)
    MuzzaEntry=StringVar(value=1)
    NapolitanaEntry=StringVar(value=1)
    CalabresaEntry=StringVar(value=1)
    NumeroDePedido=StringVar(value=1)
    #raiz.iconbitmap("pizza.ico")
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
    #Texto Entry
    Entry(MiFrame,textvariable=MuzzaEntry).grid(row=0,column=1)
    Entry(MiFrame,textvariable=NapolitanaEntry).grid(row=1,column=1)
    Entry(MiFrame,textvariable=CalabresaEntry).grid(row=2,column=1)
    Entry(MiFrame,textvariable=NombreEntry).grid(row=3,column=1)
    Entry(MiFrame,state=DISABLED,textvariable=CanpizzaEntry).grid(row=4,column=1)
    Entry(MiFrame,state=DISABLED,textvariable=TotalParcial).grid(row=5,column=1)
    Entry(MiFrame,state=DISABLED,textvariable=NumeroDePedido).grid(row=6,column=1)
    #ListaPedidos
    ListaPedidos=Listbox(MiFrame,heigh=10)
    ListaPedidos.grid(row=0,column=4,rowspan=10)
    #Scroll
    scrollista=Scrollbar(MiFrame,command=ListaPedidos.yview)
    scrollista.grid(row=0,column=5,rowspan=10,sticky="nsew")
    ListaPedidos.config(yscrollcommand=scrollista.set)
    #Botones import export
    Button(MiFrame,text="Importar datos",command=functions.test(1)).grid(row=8,column=0)
    Button(MiFrame,text="Exportar datos",command=functions.test(2)).grid(row=8,column=1)
    Button(MiFrame,text="Finalizar dia",command=functions.test(3)).grid(row=8,column=2)
    #Boton abajo
    Button(MiFrame,text="Calcular precio",command=functions.test(4)).grid(row=7,column=0)
    Button(MiFrame,text="Cancelar pedido",command=functions.test(5)).grid(row=7,column=1)
    Button(MiFrame,text="Confirmar pedido",command=functions.test(6)).grid(row=7,column=2)
    raiz.mainloop()