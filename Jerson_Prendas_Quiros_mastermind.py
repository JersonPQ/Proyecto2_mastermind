from tkinter import *

ventana_juego = Tk()
ventana_juego.title("Mastermind")
ventana_juego.configure(bg="purple")
ventana_juego.state("zoomed")
logo = PhotoImage(file="mastermind_copy_(Logo mas pequeno).png")
start_button = PhotoImage(file="START_button_recortado_(boton).png")
cancel_button = PhotoImage(file="CANCEL_button_recortado_(boton).png")

cantidad_filas = 8
cantidad_columnas = 4
columnas_tabla_calificar = 2
matriz_tablero = []
matriz_tabla_calificar = []

started = False
nombre_jugador = StringVar
secuencia_a_adivinar = []
opcion_seleccionada = "A"
opcion1 = "A"
opcion2 = "B"
opcion3 = "C"
opcion4 = "D"
opcion5 = "E"
opcion6 = "F"


# ---------------- Funciones --------------------- #


def start():
    global started

    if not started:
        started = True
        print("Juego inicado")
    else:
        print("Espere que se termine el juego")


def cancel():
    global started

    if started:
        started = False
        print("Juego cancelado")
    else:
        print("Juego no ha sido iniciado")


def poner_color(label):
    print(label)


# ---------------- Frames --------------------- #

botones_izquierda = Frame(ventana_juego, bg="black", height=500)
botones_izquierda.grid(row=1, rowspan=4, column=0, padx=150, pady=15)

tablero = Frame(ventana_juego, bg="blue", width=400, height=800)
tablero.grid(row=1, rowspan=8, column=3, pady=15)

tabla_calificadora = Frame(ventana_juego, bg="dark gray", width=150, height=800)
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
Button(start_cancel_buttons, image=start_button, bg="white", borderwidth=0, pady=15, padx=30,
       command=lambda: start()).grid(row=0, column=0, pady=20)
Button(start_cancel_buttons, image=cancel_button, bg="white", borderwidth=0, pady=15, padx=30,
       command=lambda: cancel()).grid(row=1, column=0, pady=20)

# ---------------- Código --------------------- #

# for para crear cuadro de los botones de los colores
for i in range(cantidad_filas):
    fila_tablero = []

    for j in range(cantidad_columnas):
        label_tablero = Label(tablero, text="O", width=5, height=2)
        label_tablero.grid(row=i, column=j, padx=10, pady=30)
        label_tablero.bind("<Button-1>", lambda e, btn=label_tablero: poner_color(btn))
        fila_tablero.append(label_tablero)

    matriz_tablero.append(fila_tablero)

for i in range(cantidad_filas):
    fila_calificadora = []
    fila_cuadrito = Frame(tabla_calificadora)

    for j in range(columnas_tabla_calificar):
        lista_fila_cuadrito = []

        for fila_cal in range(columnas_tabla_calificar):
            label_calificar = Label(fila_cuadrito, text="O", width=4, height=1)
            label_calificar.grid(row=j, column=fila_cal, pady=10)
            lista_fila_cuadrito.append(label_calificar)

        fila_cuadrito.grid(row=i, column=j, pady=7)
        fila_calificadora.append(lista_fila_cuadrito)

    matriz_tabla_calificar.append(fila_calificadora)

for

ventana_juego.mainloop()
