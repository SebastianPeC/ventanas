from tkinter import *
from PIL import Image, ImageTk
           
ventana = Tk()

#colocar logo
path = Image.open("C:\\Users\\SEBASTIAN\\Desktop\\VISUAL STUDIO CODE-CARPETA\\ventanas\\descarga.jpeg")
icono = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icono)

#titulo de la app
ventana.title("app de sebastian")

#dimenciones y configuracion de la ventana
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto
ventana.geometry(f"700x500")
ventana.resizable(True, True)
ventana.config(bg="light blue")

#primer frame
marco1 = Frame(ventana, width=200, height=100, bd=2, relief="solid",bg="pink")

marco1.grid(row=0, column=0, padx=10, pady=10)

#etiqueta para guardar el texto a cambiar
etiqueta= Label(marco1,text="inicio", bg="pink", fg="black", font=("Times New Roman", 16))
etiqueta.pack(expand=True, fill=BOTH)

#ingresar el texto por el que cambiar
cuadro_texto = Entry(marco1, width=40)
cuadro_texto.pack()

#funcion para cambiar texto
def cambiar_texto():
    texto_ingresado = cuadro_texto.get()
    etiqueta.config(text="Texto ingresado: " + texto_ingresado)
boton1 = Button(marco1,bg="pink", text="agregar texto", command=cambiar_texto)
boton1.pack()


#segundo frame
marco2 = Frame(ventana,width=200,height=100,bd=2,relief="solid",bg="orange")
marco2.grid(row=0, column=1, padx=10, pady=10)#lo use para poder separar los frames

#etiqueta donde mostrar la opcion seleccionada
etiqueta2= Label(marco2,text="elige un refrigerio", bg="orange", fg="black", font=("Times New Roman", 16))
etiqueta2.pack(expand=True, fill=BOTH)


#funcion para elegir y mostrar la opcion seleccionada (debes tener seleccionada solo una)
def obtener_seleccion():
    seleccionados = cuadro_lista.curselection()
    for index in seleccionados:
        elemento = cuadro_lista.get(index)
        etiqueta2.config(text="refrigerio seleccionado: " + elemento)
cuadro_lista = Listbox(marco2, width=30, selectmode="multiple")
cuadro_lista.pack()
elementos = ["patatas", "cocacola", "palomitas", "yogurt"]
for elemento in elementos:
    cuadro_lista.insert(END, elemento)

#boton para mostrar la opcion seleccionada
boton = Button(marco2, text="Obtener refrigerio", command=obtener_seleccion,bg="orange")
boton.pack()

#tercer frame
marco3 = Frame(ventana,width=200,height=100,bd=2,relief="solid",bg="red")
marco3.grid(row=1, column=0, padx=10, pady=10)



#funcion para hacer un checklist
def obtener_estado():
    if variable.get() == 1:
        print("La casilla de verificación está seleccionada")
    else:
        print("La casilla de verificación no está seleccionada")
variable = IntVar()
casilla_verificacion = Checkbutton(marco3, text="Opción", variable=variable, command=obtener_estado,bg="purple",fg="white")
casilla_verificacion.pack()

#tercer frame
marco4= Frame(ventana,width=200,height=100,bd=2,relief="solid",bg="red")
marco4.grid(row=1,column=1,padx=10,pady=10)

#funcion para hacer un radiobutton
def obtener_seleccion():
    seleccion = variable.get()
    if seleccion == 2:
        print("primera opcion seleccionada")
    elif seleccion == 3:
        print("segunda opcion seleccionada")
    elif seleccion == 4:
        print("tercera opcion seleccionada")

opcion1 = Radiobutton(marco4, text="primera opcion", variable=variable, value=2, command=obtener_seleccion,bg="yellow")
opcion1.pack()

opcion2 = Radiobutton(marco4, text="segunda opcion", variable=variable, value=3, command=obtener_seleccion,bg="blue")
opcion2.pack()

opcion3 = Radiobutton(marco4, text="tercera opcion", variable=variable, value=4, command=obtener_seleccion,bg="red")
opcion3.pack()


ventana.mainloop()
