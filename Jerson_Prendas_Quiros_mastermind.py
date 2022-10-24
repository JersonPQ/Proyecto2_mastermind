from tkinter import *
import random
import pickle

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
negros = 0
blancos = 0

started = False
nombre_jugador = StringVar
secuencia_a_adivinar = 0
partida_guardada = []
opciones = ["A", "B", "C", "D", "E", "F"]
opcion_seleccionada = opciones[0]

# ---------------- Funciones --------------------- #


def start():
    global started, opciones, boton_start, posicion_fila, secuencia_a_adivinar, negros, blancos

    if not started:
        started = True
        posicion_fila = 0
        negros = 0
        blancos = 0
        secuencia_a_adivinar = random.choices(opciones, k=4)
        boton_start.configure(image=check_button, command=lambda: cambiar_fila(posicion_fila))

        print("Secuencia a adivinar: {0}".format(secuencia_a_adivinar))

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


def cancel():
    global started, boton_start, start_button, cantidad_filas, matriz_tablero, negros, blancos

    if started:
        started = False
        negros = 0
        blancos = 0
        boton_start.configure(image=start_button, command=lambda: start())

        # deshabilita los cuadritos de el tablero
        for fila in matriz_tablero:
            for cuadro in fila:
                cuadro.unbind("<Button-1>")

        print("Juego cancelado")
    else:
        print("Juego no ha sido iniciado")

    # limpia text de los cuadritos en caso de clickear cancel
    for x in range(cantidad_filas):
        for y in range(cantidad_columnas):
            matriz_tablero[x][y].configure(text="")


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
    global posicion_fila, started, secuencia_a_adivinar, negros, blancos
    negros = 0
    blancos = 0

    # valida de que todos los cuadritos tengan un valor y no estén vacíos
    for elemento in matriz_tablero[row]:
        if "" == elemento["text"]:
            return

        print(row)

    # REVISAAAARRRR
    for i_elemento_revisar, elemento_revisar in enumerate(matriz_tablero[posicion_fila]):
        if elemento_revisar["text"] == secuencia_a_adivinar[i_elemento_revisar]:
            negros += 1
        elif elemento_revisar["text"] in secuencia_a_adivinar:
            blancos += 1

    print(f"Cuadritos negros: {negros}")
    print(f"Cuadritos blancos: {blancos}")

    if negros == 4:
        print("¡HAS GANADO!")
        boton_start.configure(image=start_button, command=start)
        started = False
        return

    posicion_fila += 1

    # si posicion de fila es == a cantidad de filas se cambia el boton y se "reinicia el conteo de filas"
    if posicion_fila == cantidad_filas:
        boton_start.configure(image=start_button, command=lambda: start())
        started = False
        print("No lo has conseguido, A LA PRÓXIMA")
        return

    # si la fila en la que se está es mayor que 0 y menor o igual que el numero de filas, entonces habilita el poder
    # dar click como boton, y deshabilita el anterior que estaba habilitado
    if 0 < posicion_fila <= cantidad_filas:
        for cuadro in matriz_tablero[posicion_fila - 1]:
            cuadro.unbind("<Button-1>")

        for cuadro in matriz_tablero[posicion_fila]:
            cuadro.bind("<Button-1>", lambda e, btn=cuadro: poner_opcion(btn))


def save(matriz_partida):
    global started, posicion_fila, secuencia_a_adivinar

    if started:
        datos_cuadrito_tablero = []

        for i_matriz in matriz_partida:
            fila = []

            for j_matriz in i_matriz:
                fila.append(j_matriz["text"])

            datos_cuadrito_tablero.append(fila)

        archivo_partida = open("partida_guardada.dat", "wb")
        pickle.dump(datos_cuadrito_tablero, archivo_partida)
        pickle.dump(posicion_fila, archivo_partida)
        pickle.dump(secuencia_a_adivinar, archivo_partida)
        archivo_partida.close()


def load(tablero_matriz):
    global started, posicion_fila, partida_guardada, secuencia_a_adivinar
    archivo_partida = open("partida_guardada.dat", "rb")

    while True:
        try:
            partida_guardada += [pickle.load(archivo_partida)]
        except EOFError:
            break

    datos_cuadritos_tablero = partida_guardada[0]
    posicion_fila = partida_guardada[1]
    secuencia_a_adivinar = partida_guardada[2]

    print(f"Secuencia a adivinar: {secuencia_a_adivinar}")

    archivo_partida.close()

    if not started:
        for i_matriz in range(len(tablero_matriz)):
            for j_matriz in range(len(tablero_matriz[0])):
                tablero_matriz[i_matriz][j_matriz]["text"] = datos_cuadritos_tablero[i_matriz][j_matriz]

        boton_start.configure(image=check_button, command=lambda: cambiar_fila(posicion_fila))

        for cuadro in matriz_tablero[posicion_fila]:
            cuadro.bind("<Button-1>", lambda e, btn=cuadro: poner_opcion(btn))

        started = True


# ---------------- Frames --------------------- #

botones_izquierda = Frame(ventana_juego, bg="black", height=180)
botones_izquierda.grid(row=1, rowspan=3, column=0, padx=150)

entry_jugador = Frame(botones_izquierda, bg="white")
entry_jugador.grid(row=1, column=0, pady=15)

start_cancel_buttons = Frame(botones_izquierda, bg="white")
start_cancel_buttons.grid(row=2, column=0, pady=40)

tablero = Frame(ventana_juego, bg="light gray", width=400, height=800)
tablero.grid(row=1, rowspan=8, column=3, pady=15)

tabla_calificadora = Frame(ventana_juego, bg="light gray", width=150, height=800, padx=5)
tabla_calificadora.grid(row=1, rowspan=7, column=4, pady=15)

panel_opciones = Frame(ventana_juego, bg="red", width=100, height=500)
panel_opciones.grid(row=1, rowspan=3, column=5, padx=150, pady=15)

save_load_buttons = Frame(ventana_juego, bg="orange", width=210, height=175)
save_load_buttons.grid(row=4, column=5)

# ---------------- Labels --------------------- #

Label(botones_izquierda, image=logo, borderwidth=0, padx=40).grid(row=0, column=0, padx=10, pady=10)
Label(entry_jugador, text="Jugador:", bg="white", font=("Open Sans", 12), padx=5).grid(row=0, column=0)

# ---------------- Buttons --------------------- #

Entry(entry_jugador, textvariable=nombre_jugador, bg="light gray", borderwidth=0, font=("Open Sans", 12)).grid(row=0,
                                                                                                               column=1)
boton_start = Button(start_cancel_buttons, image=start_button, bg="white", borderwidth=0, pady=15, padx=30,
                     command=lambda: start())
boton_start.grid(row=0, column=0, pady=20)

Button(start_cancel_buttons, image=cancel_button, bg="white", borderwidth=0, pady=15, padx=30,
       command=cancel).grid(row=1, column=0, pady=20)

save_button = Button(save_load_buttons, text="SAVE", bg="red", padx=42, pady=15, command=lambda: save(matriz_tablero))
save_button.grid(row=0, column=0, padx=10, pady=10)

load_button = Button(save_load_buttons, text="LOAD", bg="red", padx=40, pady=15, command=lambda: load(matriz_tablero))
load_button.grid(row=1, column=0, padx=10, pady=10)

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
