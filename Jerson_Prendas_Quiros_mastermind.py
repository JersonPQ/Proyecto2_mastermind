from tkinter import *
import random

ventana_juego = Tk()
ventana_juego.title("Mastermind")
ventana_juego.configure(bg="purple")
ventana_juego.state("zoomed")

logo = PhotoImage(file="mastermind_copy_(Logo mas pequeno).png")
start_button = PhotoImage(file="START_button_recortado_(boton).png")
cancel_button = PhotoImage(file="CANCEL_button_recortado_(boton).png")
check_button = PhotoImage(file="CALIFICAR_recortado_(boton).png")

cantidad_filas = 8
cantidad_columnas = 4
columnas_tabla_calificar = 2
matriz_tablero = []
matriz_tabla_calificar = []
posicion_fila = 0

started = False
nombre_jugador = StringVar
opciones = ["A", "B", "C", "D", "E", "F"]
opcion_seleccionada = opciones[0]

# ---------------- Funciones --------------------- #


def start():
    global started, opciones, boton_start, posicion_fila

    posicion_fila = 0

    if not started:
        started = True
        secuencia_a_adivinar = random.choices(opciones, k=4)
        boton_start.configure(image=check_button, command=lambda: cambiar_fila(posicion_fila))

        # limpia text de los cuadritos en caso de haber terminado un juego y lo vuelve a iniciar
        for x in range(cantidad_filas):
            for y in range(cantidad_columnas):
                matriz_tablero[x][y].configure(text="")

        # habilita los cuadritos que están en la fila 0
        for cuadro in matriz_tablero[posicion_fila]:
            cuadro.bind("<Button-1>", lambda e, btn=cuadro: poner_opcion(btn))

        print("Juego iniciado")
    else:
        print("Espere que se termine el juego")


def cancel(row):
    global started, boton_start, start_button, cantidad_filas, matriz_tablero

    # deshabilita los cuadritos de la posicion en la que se estaba en caso de dar cancel
    for cuadro in matriz_tablero[row]:
        cuadro.unbind("<Button-1>")

    if started:
        started = False
        boton_start.configure(image=start_button, command=lambda: start())

    # limpia text de los cuadritos en caso de clickear cancel
    for x in range(cantidad_filas):
        for y in range(cantidad_columnas):
            matriz_tablero[x][y].configure(text="")

        print("Juego cancelado")
    else:
        print("Juego no ha sido iniciado")


def poner_opcion(label):
    if started:
        # da valor al label clickeado
        label.configure(text=opcion_seleccionada)
        print(label)


def seleccionar_opcion(label):
    global opcion_seleccionada

    if started:
        # toma el valor del label clickeado (los del panel)
        opcion_seleccionada = label['text']
        print(label)


def cambiar_fila(row):
    global posicion_fila, started

    # valida de que todos los cuadritos tengan un valor y no estén vacíos
    for elemento in matriz_tablero[row]:
        if "" == elemento["text"]:
            return

        print(row)

    posicion_fila += 1

    # si posicion de fila es == a cantidad de filas se cambia el boton y se "reinicia el conteo de filas"
    if posicion_fila == cantidad_filas:
        boton_start.configure(image=start_button, command=lambda: start())
        started = False
        return

    # si la fila en la que se está es mayor que 0 y menor o igual que el numero de filas, entonces habilita el poder
    # dar click como boton, y deshabilita el anterior que estaba habilitado
    if 0 < posicion_fila <= cantidad_filas:
        for cuadro in matriz_tablero[posicion_fila - 1]:
            cuadro.unbind("<Button-1>")

        for cuadro in matriz_tablero[posicion_fila]:
            cuadro.bind("<Button-1>", lambda e, btn=cuadro: poner_opcion(btn))


# ---------------- Frames --------------------- #

botones_izquierda = Frame(ventana_juego, bg="black", height=500)
botones_izquierda.grid(row=1, rowspan=4, column=0, padx=150, pady=15)

tablero = Frame(ventana_juego, bg="light gray", width=400, height=800)
tablero.grid(row=1, rowspan=8, column=3, pady=15)

tabla_calificadora = Frame(ventana_juego, bg="light gray", width=150, height=800, padx=5)
tabla_calificadora.grid(row=1, rowspan=7, column=4, pady=15)

panel_opciones = Frame(ventana_juego, bg="red", width=100, height=500)
panel_opciones.grid(row=1, rowspan=3, column=5, padx=150, pady=15)

entry_jugador = Frame(botones_izquierda, bg="white")
entry_jugador.grid(row=1, column=0, pady=40)

start_cancel_buttons = Frame(botones_izquierda, bg="white")
start_cancel_buttons.grid(row=2, column=0, pady=80)


# ---------------- Labels --------------------- #

Label(botones_izquierda, image=logo, borderwidth=0, padx=40).grid(row=0, column=0, padx=10, pady=60)
Label(entry_jugador, text="Jugador:", bg="white", font=("Open Sans", 12), padx=5).grid(row=0, column=0)

# ---------------- Buttons --------------------- #

Entry(entry_jugador, textvariable=nombre_jugador, bg="light gray", borderwidth=0, font=("Open Sans", 12)).grid(row=0,
                                                                                                               column=1)
boton_start = Button(start_cancel_buttons, image=start_button, bg="white", borderwidth=0, pady=15, padx=30,
                     command=lambda: start())
boton_start.grid(row=0, column=0, pady=20)
Button(start_cancel_buttons, image=cancel_button, bg="white", borderwidth=0, pady=15, padx=30,
       command=lambda: cancel(posicion_fila)).grid(row=1, column=0, pady=20)

# ---------------- Código --------------------- #

# for para crear cuadro de los botones de los colores
for i in range(cantidad_filas):
    fila_tablero = []

    for j in range(cantidad_columnas):
        label_tablero = Label(tablero, text="", width=5, height=2)
        label_tablero.grid(row=i, column=j, padx=10, pady=30)
        fila_tablero.append(label_tablero)

    matriz_tablero.append(fila_tablero)

# for para crear la tabla de calificación
for i in range(cantidad_filas):
    fila_calificadora = []
    fila_cuadrito = Frame(tabla_calificadora, bg="light gray")

    for j in range(columnas_tabla_calificar):
        lista_fila_cuadrito = []

        for fila_cal in range(columnas_tabla_calificar):
            label_calificar = Label(fila_cuadrito, text="O", width=2, height=1)
            label_calificar.grid(row=j, column=fila_cal, pady=10, padx=5)
            lista_fila_cuadrito.append(label_calificar)

        fila_cuadrito.grid(row=i, column=j, pady=7)
        fila_calificadora.append(lista_fila_cuadrito)

    matriz_tabla_calificar.append(fila_calificadora)

# for para crear botones del panel
for i in range(len(opciones)):
    label_panel = Label(panel_opciones, text=opciones[i], width=5, height=2)
    label_panel.grid(row=i, column=0, padx=10, pady=20)
    label_panel.bind("<Button-1>", lambda e, btn=label_panel: seleccionar_opcion(btn))

ventana_juego.mainloop()
