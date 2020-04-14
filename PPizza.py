from tkinter import *
from io import open
from datetime import date
from datetime import datetime

contador=1#contadores
muzacont=0
calacont=0
napocont=0
raiz=Tk()
#diccionarios
#NombreCliente={}#Primero numero de pedido
#PizzasPedidas={}#Primero numero de pedido
#PrecioPizzas={}#Primero numero de pedido
DiccioFin={}
#Stringvars
NombreEntry=StringVar()
CanpizzaEntry=StringVar()
TotalParcial=StringVar()
MuzzaEntry=StringVar()
NapolitanaEntry=StringVar()
CalabresaEntry=StringVar()
NumeroDePedido=StringVar()
#contador del numero de pedido mostrado
NumeroDePedido.set("{}".format(contador))
raiz.iconbitmap("pizza.ico")
#funciones
def confirmarpedido():
    Nombre=str(NombreEntry.get())
    Pedido=int(CanpizzaEntry.get())
    contador=int(NumeroDePedido.get())
    PrecioF=int(TotalParcial.get())
    TotalParcial.set("{}".format(contador))
    Horario = ffecha(1)#pedir la fecha
    DiccioFin[contador]=[Nombre.capitalize(),Pedido,PrecioF,Horario]
    ListaPedidos.insert(END,"{}".format(contador)+' '+'{}'.format(Horario)+' '
    + '{}'.format(Pedido)+' '+'{}'.format(PrecioF)+' '+Nombre.capitalize())
    contador+=1
    NumeroDePedido.set("{}".format(contador))
    cancelarpedido()
    print(DiccioFin)

def errores(coderror):
    if coderror==1:
        ventana_error = Toplevel(raiz)
        ventana_error.title("Error")
        labelexample = Label(ventana_error, text = "No se pueden calcular 0 pizzas")
        buttonexample = Button(ventana_error, text = "Aceptar", command = ventana_error.destroy)
        labelexample.pack()
        buttonexample.pack()
        ventana_error.grab_set()
        raiz.wait_window(ventana_error)
    if coderror==2:
        ventana_error = Toplevel(raiz)
        ventana_error.title("Error")
        labelexample = Label(ventana_error, text = "No se deben ingresar letras en las cantidades de pizzas")
        buttonexample = Button(ventana_error, text = "Aceptar", command = ventana_error.destroy)
        labelexample.pack()
        buttonexample.pack()
        ventana_error.grab_set()
        raiz.wait_window(ventana_error)
def calcularprecio():
    SMuza=str(MuzzaEntry.get())
    SNapo=str(NapolitanaEntry.get())
    SCal=str(CalabresaEntry.get())
    if(len(SMuza)==0 and len(SNapo)==0 and len(SCal)==0):
        errores(1)
        return
    if(len(SMuza)==0):
        SMuza='0'
        MuzzaEntry.set('0')
    if(len(SNapo)==0):
        SNapo='0'
        NapolitanaEntry.set('0')
    if(len(SCal)==0):
        SCal='0'
        CalabresaEntry.set('0')
    try:
        PMuza=int(SMuza)
        PNapo=int(SNapo)
        PCal=int(SCal)
    except ValueError:
        errores(2)
    CantPizzas=PMuza+PNapo+PCal
    TotalM=PMuza*100
    TotalN=PNapo*120
    TotalC=PCal*140
    PTotal=TotalC+TotalM+TotalN
    CanpizzaEntry.set(CantPizzas)
    TotalParcial.set(PTotal)

def cancelarpedido():
    MuzzaEntry.set('')
    CalabresaEntry.set('')
    NapolitanaEntry.set('')
    TotalParcial.set('')
    NombreEntry.set('')
    CanpizzaEntry.set('')

def findia():
    dia = ffecha(2)
    print(dia)
    with open("./findia/{}.txt".format(dia), "w") as agendaarchivo:
        for nombre, valor  in DiccioFin.items():
            agendaarchivo.write("%s %s\n" %(nombre, valor))

def importdatos():
    ventana_importar = Toplevel(raiz)
    ventana_importar.title("Importar")
    Button(ventana_importar, text = "Aceptar").grid(row = 0, column = 0)
    Button(ventana_importar, text = "Cancelar").grid(row = 0, column = 1)

    ventana_importar.grab_set()
    raiz.wait_window(ventana_importar)

def exportardatos():
    dia = ffecha(0)
    #archivo_texto = open("{}.txt".format(dia),"w")
    #archivo_texto.write(DiccioFin)
    #for x int DiccioFin:
    with open("{}.txt".format(dia), "w") as agendaarchivo:
        for nombre, valor  in DiccioFin.items():
            agendaarchivo.write("%s %s\n" %(nombre, valor))
            

def ffecha(bandera):
    hoy = date.today()#la fecha de hoy
    tiempo = datetime.now()#año mes dia hora minutos segundos
    hora = str(tiempo.hour)
    minuto = str(tiempo.minute)
    if bandera==0:#esto pide exportardatos
        fecha = "{}-{}-{}".format(hoy,hora,minuto)
        return fecha
    elif bandera==1:#esto pide finalizar pedidos
        fecha = "{}-{}".format(hora,minuto)
        return fecha
    else:#esto pide findia
        return hoy
#---------
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
Button(MiFrame,text="Importar datos",command=importdatos).grid(row=8,column=0)
Button(MiFrame,text="Exportar datos",command=exportardatos).grid(row=8,column=1)
Button(MiFrame,text="Finalizar dia",command=findia).grid(row=8,column=2)
#Boton abajo
Button(MiFrame,text="Calcular precio",command=calcularprecio).grid(row=7,column=0)
Button(MiFrame,text="Cancelar pedido",command=cancelarpedido).grid(row=7,column=1)
Button(MiFrame,text="Confirmar pedido",command=confirmarpedido).grid(row=7,column=2)
#
raiz.mainloop()