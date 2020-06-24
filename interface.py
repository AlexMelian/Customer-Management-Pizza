from tkinter import Button, Label, Grid, Entry, Pack, DISABLED, Listbox, Tk, Frame, StringVar, Scrollbar, IntVar
import functions

def window():
    raiz = Tk()
    
    
    NameEntry = StringVar()
    NumberPizzaEntry = IntVar()
    Subtotal = IntVar()
    MuzzaEntry = IntVar()
    NapolitanaEntry = IntVar()
    CalabresaEntry = IntVar()
    NumberOfOrder = IntVar()

    #raiz.iconbitmap('/pizza.ico')
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
    Button(MiFrame,text="Importar datos",command=lambda: functions.test(1)).grid(row=8,column=0)
    Button(MiFrame,text="Exportar datos",command=lambda: functions.test(2)).grid(row=8,column=1)
    Button(MiFrame,text="Finalizar dia",command=lambda: functions.test(3)).grid(row=8,column=2)
    #Button down
    Button(MiFrame,text="Calcular precio",command=lambda: functions.Calculate_Price(int(NapolitanaEntry.get()),int(MuzzaEntry.get()),int(CalabresaEntry.get()))).grid(row=7,column=0)
    Button(MiFrame,text="Cancelar pedido",command=lambda: functions.test(5)).grid(row=7,column=1)
    Button(MiFrame,text="Confirmar pedido",command=lambda: functions.Confirm_Order(1,2,3)).grid(row=7,column=2)
    raiz.mainloop()