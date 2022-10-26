from tkinter import *
import random
import pickle

ventana_configuracion = Tk()
ventana_configuracion.title("Mastermind")
ventana_configuracion.state("zoomed")

seleccion_dificultad = IntVar()
seleccion_dificultad.set(1)

seleccion_reloj = IntVar()
seleccion_reloj.set(1)

seleccion_posicion_panel = IntVar()
seleccion_posicion_panel.set(1)

seleccion_panel = IntVar()
seleccion_panel.set(1)

# -------------------------------------------- Frames -------------------------------------------- #
dificultad = Frame(ventana_configuracion, bg="black", height=300, width=500)
dificultad.place(x=175, y=40)

radiobuttons_dificultad = Frame(dificultad, bg="yellow", height=150, width=250)
radiobuttons_dificultad.place(x=150, y=90)

reloj = Frame(ventana_configuracion, bg="black", height=300, width=500)
reloj.place(x=175, y=380)

radiobuttons_reloj = Frame(reloj, bg="yellow", height=150, width=250)
radiobuttons_reloj.place(x=150, y=90)

posicion_panel = Frame(ventana_configuracion, bg="black", height=300, width=500)
posicion_panel.place(x=875, y=40)

radiobuttons_posicion_panel = Frame(posicion_panel, bg="yellow", height=150, width=250)
radiobuttons_posicion_panel.place(x=150, y=90)

panel = Frame(ventana_configuracion, bg="black", height=300, width=500)
panel.place(x=875, y=380)

radiobuttons_panel = Frame(panel, bg="yellow", height=150, width=250)
radiobuttons_panel.place(x=150, y=90)

# -------------------------------------------- Labels -------------------------------------------- #
Label(dificultad, text="Dificultad:", bg="red", font=("Open Sans", 12)).place(x=50, y=50)

Label(reloj, text="Reloj:", bg="red", font=("Open Sans", 12)).place(x=50, y=50)

Label(posicion_panel, text="Posición del panel:", bg="red", font=("Open Sans", 12)).place(x=50, y=50)

Label(panel, text="Panel de elementos para utilizar:", bg="red", font=("Open Sans", 12)).place(x=50, y=50)

# -------------------------------------------- Radiobuttons -------------------------------------------- #
nivel_facil = Radiobutton(radiobuttons_dificultad, text="Nivel Fácil", font=("Open Sans", 12),
                          variable=seleccion_dificultad, value=1)
nivel_facil.place(x=0, y=0)

nivel_medio = Radiobutton(radiobuttons_dificultad, text="Nivel Medio", font=("Open Sans", 12),
                          variable=seleccion_dificultad, value=2)
nivel_medio.place(x=0, y=40)

nivel_dificil = Radiobutton(radiobuttons_dificultad, text="Nivel Difícil", font=("Open Sans", 12),
                            variable=seleccion_dificultad, value=3)
nivel_dificil.place(x=0, y=80)

reloj_si = Radiobutton(radiobuttons_reloj, text="Si", bg="white", font=("Open Sans", 12), variable=seleccion_reloj,
                       value=1)
reloj_si.place(x=0, y=0)

reloj_no = Radiobutton(radiobuttons_reloj, text="No", bg="white", font=("Open Sans", 12), variable=seleccion_reloj,
                       value=2)
reloj_no.place(x=0, y=40)

reloj_por_jugada = Radiobutton(radiobuttons_reloj, text="Cronómetro por jugada", bg="white", font=("Open Sans", 12),
                               variable=seleccion_reloj, value=3)
reloj_por_jugada.place(x=0, y=80)

reloj_por_juego = Radiobutton(radiobuttons_reloj, text="Cronómetro por juego", bg="white", font=("Open Sans", 12),
                              variable=seleccion_reloj, value=4)
reloj_por_juego.place(x=0, y=120)

posicion_panel_derecha = Radiobutton(radiobuttons_posicion_panel, text="Derecha", font=("Open Sans", 12),
                                     variable=seleccion_posicion_panel, value=1)
posicion_panel_derecha.place(x=0, y=0)

posicion_panel_izquierda = Radiobutton(radiobuttons_posicion_panel, text="Izquierda", font=("Open Sans", 12),
                                       variable=seleccion_posicion_panel, value=2)
posicion_panel_izquierda.place(x=0, y=40)

panel_colores = Radiobutton(radiobuttons_panel, text="Colores", font=("Open Sans", 12), variable=seleccion_panel,
                            value=1)
panel_colores.place(x=0, y=0)

panel_letras = Radiobutton(radiobuttons_panel, text="Letras", font=("Open Sans", 12), variable=seleccion_panel, value=2)
panel_letras.place(x=0, y=40)

panel_numeros = Radiobutton(radiobuttons_panel, text="Números", font=("Open Sans", 12), variable=seleccion_panel,
                            value=3)
panel_numeros.place(x=0, y=80)


def juego_letras_numeros():
    global cantidad_filas, cantidad_columnas, matriz_tablero, matriz_tabla_calificar, matriz_tabla_calificar, \
        matriz_tabla_calificar, posicion_fila, negros, blancos, started, nombre_jugador, secuencia_a_adivinar, \
        partida_guardada, opciones, opcion_seleccionada, opcion_del_momento, nivel, posicion_botones_izquierda, posicion_panel_eje_x

    ventana_juego = Toplevel()
    ventana_juego.title("Mastermind")
    ventana_juego.configure(bg="white")
    ventana_juego.state("zoomed")

    logo = PhotoImage(file="mastermind_copy_(Logo mas pequeno).png")
    start_button = PhotoImage(file="START_button_recortado_(boton).png")
    cancel_button = PhotoImage(file="CANCEL_button_recortado_(boton).png")
    check_button = PhotoImage(file="CALIFICAR_recortado_(boton).png")

    if seleccion_dificultad.get() == 1:
        cantidad_filas = 8
        nivel = "Nivel: Fácil"
    elif seleccion_dificultad.get() == 2:
        cantidad_filas = 7
        nivel = "Nivel: Medio"
    elif seleccion_dificultad.get() == 3:
        cantidad_filas = 6
        nivel = "Nivel: Difícil"

    # if seleccion_reloj == 1:

    if seleccion_posicion_panel.get() == 1:
        posicion_botones_izquierda = 150
        posicion_panel_eje_x = 1060
    elif seleccion_posicion_panel.get() == 2:
        posicion_botones_izquierda = 1060
        posicion_panel_eje_x = 150

    if seleccion_panel.get() == 2:
        opciones = ["A", "B", "C", "D", "E", "F"]
    elif seleccion_panel.get() == 3:
        opciones = ["1", "2", "3", "4", "5", "6"]

    cantidad_columnas = 4
    matriz_tablero = []
    matriz_tabla_calificar = []
    posicion_fila = 0
    negros = 0
    blancos = 0

    started = False
    nombre_jugador = StringVar(ventana_juego)
    secuencia_a_adivinar = 0
    partida_guardada = []
    opcion_seleccionada = opciones[0]
    opcion_del_momento = f"Opción seleccionada: {opcion_seleccionada}"

    # -------------------------------------------- Funciones -------------------------------------------- #

    def start():
        global started, opciones, boton_start, posicion_fila, secuencia_a_adivinar, negros, blancos, entrada_nombre_jugador

        if not started and not (entrada_nombre_jugador.get() == ""):
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

            # resetea los cuadritos de calificar
            for fila_calificar in matriz_tabla_calificar:
                for cuadrito_calificar in fila_calificar:
                    cuadrito_calificar.config(bg="orange")

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

            # resetea los cuadritos de calificar
            for fila_calificar in matriz_tabla_calificar:
                for cuadrito_calificar in fila_calificar:
                    cuadrito_calificar.config(bg="orange")

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
        global opcion_seleccionada, opcion_del_momento, opcion_del_momento_label

        if started:
            # toma el valor del label clickeado (los del panel)
            opcion_seleccionada = label['text']
            opcion_del_momento = f"Opción seleccionada: {opcion_seleccionada}"
            opcion_del_momento_label.config(text=opcion_del_momento)
            print(label)

    def cambiar_fila(row):
        global posicion_fila, started, secuencia_a_adivinar, negros, blancos
        negros = 0
        blancos = 0
        i_cuadrito_blanco = 0

        # valida de que todos los cuadritos tengan un valor y no estén vacíos
        for elemento in matriz_tablero[row]:
            if "" == elemento["text"]:
                return

            print(row)

        # revisa si las letras son iguales a las de la secuencia creada
        for i_elemento_revisar, elemento_revisar in enumerate(matriz_tablero[posicion_fila]):
            if elemento_revisar["text"] == secuencia_a_adivinar[i_elemento_revisar]:
                negros += 1
            elif elemento_revisar["text"] in secuencia_a_adivinar:
                blancos += 1

        # pone de color negro y blanco en cada cuadrito dependiendo de la cantidad de "pines" negros y blancos que tenga
        # en la fila
        for cuadrito_negro in range(negros):
            matriz_tabla_calificar[row][cuadrito_negro].config(bg="black")
            i_cuadrito_blanco += 1

        for cuadrito_blanco in range(blancos):
            comienza_cuadrito_blanco = matriz_tabla_calificar[row][i_cuadrito_blanco:]
            comienza_cuadrito_blanco[cuadrito_blanco].config(bg="white")

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

    def save(matriz_partida, matriz_tabla_calificacion):
        global started, posicion_fila, secuencia_a_adivinar, entrada_nombre_jugador

        if started:
            datos_cuadrito_tablero = []
            datos_color_calificacion = []

            # toma valor de cada "text" de cada cuadrito de la matriz tablero
            for i_matriz in matriz_partida:
                fila = []

                for j_matriz in i_matriz:
                    fila.append(j_matriz["text"])

                datos_cuadrito_tablero.append(fila)

            for fila_califica in matriz_tabla_calificacion:
                fila_calificacion = []

                for cuadrito in fila_califica:
                    fila_calificacion.append(cuadrito["bg"])

                datos_color_calificacion.append(fila_calificacion)

            archivo_partida = open("mastermind2022juegoactual.dat", "wb")
            pickle.dump(datos_cuadrito_tablero, archivo_partida)
            pickle.dump(posicion_fila, archivo_partida)
            pickle.dump(secuencia_a_adivinar, archivo_partida)
            pickle.dump(entrada_nombre_jugador.get(), archivo_partida)
            pickle.dump(datos_color_calificacion, archivo_partida)
            pickle.dump(nivel, archivo_partida)
            # pickle.dump()  # Guardar el reloj aquí
            # pickle.dump()  # Guardar la posicion del panel aquí
            # pickle.dump()  # posicion de los botones de izquierda aquí
            pickle.dump(opciones, archivo_partida)
            pickle.dump(cantidad_filas, archivo_partida)
            pickle.dump(posicion_botones_izquierda, archivo_partida)
            pickle.dump(posicion_panel_eje_x, archivo_partida)
            archivo_partida.close()

    def load(tablero_matriz, tablero_calificacion):
        global started, posicion_fila, partida_guardada, secuencia_a_adivinar, nombre_jugador, nivel, opciones, label_panel, opcion_seleccionada, opcion_del_momento, opcion_del_momento_label, \
            fila_calificadora, cantidad_filas, label_calificar, label_tablero, fila_tablero, matriz_tablero, matriz_tabla_calificar, posicion_botones_izquierda, posicion_panel_eje_x

        if not started:
            archivo_partida = open("mastermind2022juegoactual.dat", "rb")

            while True:
                try:
                    partida_guardada += [pickle.load(archivo_partida)]
                except EOFError:
                    break

            datos_cuadritos_tablero = partida_guardada[0]
            posicion_fila = partida_guardada[1]
            secuencia_a_adivinar = partida_guardada[2]
            nombre_jugador.set(partida_guardada[3])
            datos_colores_tablero = partida_guardada[4]
            nivel = partida_guardada[5]
            # reloj = partida_guardada[6]
            # posicion_panel = partida_guardada[6]
            # posicion_botones_izquierda = partida_guardada[7]
            opciones = partida_guardada[6]
            cantidad_filas = partida_guardada[7]
            posicion_botones_izquierda = partida_guardada[8]
            posicion_panel_eje_x = partida_guardada[9]

            print(f"Secuencia a adivinar: {secuencia_a_adivinar}")

            archivo_partida.close()

            # resetea el label de la opcion seleccionada
            opcion_seleccionada = opciones[0]
            opcion_del_momento = f"Opción seleccionada: {opcion_seleccionada}"
            opcion_del_momento_label.config(text=opcion_del_momento)

            # resetea el label del nivel
            nivel_label.config(text=nivel)

            # reposiciona los botones de la izquierda, el panel de opciones y los botones de save y load según como el
            # usuario guardó la partida
            botones_izquierda.place(x=posicion_botones_izquierda, y=75)
            panel_opciones.place(x=posicion_panel_eje_x, y=15)
            save_load_buttons.place(x=posicion_panel_eje_x - 40, y=500)

            matriz_tablero = []
            matriz_tabla_calificar = []

            # crea la nueva tabla con la cantidad de filas correspondientes
            for i in range(cantidad_filas):
                fila_tablero = []

                for j in range(cantidad_columnas):
                    label_tablero = Label(tablero, text="", width=5, height=2)
                    label_tablero.grid(row=i, column=j, padx=10, pady=30)
                    fila_tablero.append(label_tablero)

                matriz_tablero.append(fila_tablero)

            # for para crear la tabla de calificación nueva con la partida guardada
            for i in range(cantidad_filas):
                fila_calificadora = []
                # fila_cuadrito = Frame(tabla_calificadora, bg="light gray")

                for j in range(4):
                    label_calificar = Label(tabla_calificadora, text="", bg="orange", width=1)
                    label_calificar.grid(row=i, column=j, padx=5, pady=37)
                    fila_calificadora.append(label_calificar)

                matriz_tabla_calificar.append(fila_calificadora)

            # cambia los valores del tablero vacío al del tablero guardado
            for i_matriz in range(len(tablero_matriz)):
                for j_matriz in range(len(tablero_matriz[0])):
                    matriz_tablero[i_matriz][j_matriz]["text"] = datos_cuadritos_tablero[i_matriz][j_matriz]

            boton_start.configure(image=check_button, command=lambda: cambiar_fila(posicion_fila))

            # cambia los colores del tablero de calificación al de los colores de los colores
            for fila_califica in range(len(tablero_calificacion)):
                for cuadrito in range(len(tablero_calificacion[0])):
                    matriz_tabla_calificar[fila_califica][cuadrito]["bg"] = datos_colores_tablero[fila_califica][cuadrito]

            for cuadro in matriz_tablero[posicion_fila]:
                cuadro.bind("<Button-1>", lambda e, btn=cuadro: poner_opcion(btn))

            # crea el nuevo panel con los datos cargados
            for i in range(len(opciones)):
                label_panel = Label(panel_opciones, text=opciones[i], width=5, height=2)
                label_panel.grid(row=i, column=0, padx=10, pady=20)
                label_panel.bind("<Button-1>", lambda e, btn=label_panel: seleccionar_opcion(btn))

            started = True

    # -------------------------------------------- Frames -------------------------------------------- #

    global botones_izquierda, entry_jugador, start_cancel_buttons, tablero_tabla_calificadora, tablero, panel_opciones, tabla_calificadora

    botones_izquierda = Frame(ventana_juego, bg="white", height=180)
    botones_izquierda.place(x=posicion_botones_izquierda, y=75)

    entry_jugador = Frame(botones_izquierda, bg="white")
    entry_jugador.grid(row=1, column=0, pady=15)

    start_cancel_buttons = Frame(botones_izquierda, bg="white")
    start_cancel_buttons.grid(row=2, column=0, pady=40)

    tablero_tabla_calificadora = Frame(ventana_juego, bg="light gray")
    tablero_tabla_calificadora.place(x=600, y=15)

    tablero = Frame(tablero_tabla_calificadora, bg="light gray", width=400, height=800)
    tablero.grid(row=0, column=0)

    tabla_calificadora = Frame(tablero_tabla_calificadora, bg="light gray", width=150, height=800, padx=5)
    tabla_calificadora.grid(row=0, column=1)

    panel_opciones = Frame(ventana_juego, bg="light gray", width=100, height=500)
    panel_opciones.place(x=posicion_panel_eje_x, y=15)

    save_load_buttons = Frame(ventana_juego, bg="white", width=210, height=175)
    save_load_buttons.place(x=posicion_panel_eje_x - 40, y=500)

    # -------------------------------------------- Labels -------------------------------------------- #

    global opcion_del_momento_label, nivel_label

    Label(botones_izquierda, image=logo, borderwidth=0, padx=40).grid(row=0, column=0, padx=10, pady=10)
    Label(entry_jugador, text="Jugador:", bg="white", font=("Open Sans", 12), padx=5).grid(row=0, column=0)
    nivel_label = Label(ventana_juego, text=nivel, bg="pink", font=("Open Sans", 12), padx=5, pady=5)
    nivel_label.place(x=1300, y=15)

    opcion_del_momento_label = Label(ventana_juego, text=opcion_del_momento, bg="pink", font=("Open Sans", 12), padx=5,
                                     pady=5)
    opcion_del_momento_label.place(x=1300, y=700)

    # -------------------------------------------- Buttons -------------------------------------------- #

    global entrada_nombre_jugador, boton_start, save_button, load_button

    entrada_nombre_jugador = Entry(entry_jugador, textvariable=nombre_jugador, bg="light gray", borderwidth=0,
                                   font=("Open Sans", 12))
    entrada_nombre_jugador.grid(row=0, column=1)

    boton_start = Button(start_cancel_buttons, image=start_button, bg="white", borderwidth=0, pady=15, padx=30,
                         command=lambda: start())
    boton_start.grid(row=0, column=0, pady=20)

    Button(start_cancel_buttons, image=cancel_button, bg="white", borderwidth=0, pady=15, padx=30,
           command=cancel).grid(row=1, column=0, pady=20)

    save_button = Button(save_load_buttons, text="SAVE", bg="red", padx=42, pady=15,
                         command=lambda: save(matriz_tablero, matriz_tabla_calificar))
    save_button.grid(row=0, column=0, padx=10, pady=10)

    load_button = Button(save_load_buttons, text="LOAD", bg="red", padx=40, pady=15,
                         command=lambda: load(matriz_tablero, matriz_tabla_calificar))
    load_button.grid(row=1, column=0, padx=10, pady=10)

    # -------------------------------------------- Código -------------------------------------------- #

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
        # fila_cuadrito = Frame(tabla_calificadora, bg="light gray")

        for j in range(4):
            label_calificar = Label(tabla_calificadora, text="", bg="orange", width=1)
            label_calificar.grid(row=i, column=j, padx=5, pady=37)
            fila_calificadora.append(label_calificar)
            # lista_fila_cuadrito = []
            #
            # for fila_cal in range(columnas_tabla_calificar):
            #     label_calificar = Label(fila_cuadrito, text="", width=1, height=1)
            #     label_calificar.grid(row=j, column=fila_cal, pady=10, padx=5)
            #     lista_fila_cuadrito.append(label_calificar)

            # fila_cuadrito.grid(row=i, column=j, pady=7)
            # fila_calificadora.append(lista_fila_cuadrito)

        matriz_tabla_calificar.append(fila_calificadora)

    # for para crear botones del panel
    for i in range(len(opciones)):
        label_panel = Label(panel_opciones, text=opciones[i], width=5, height=2)
        label_panel.grid(row=i, column=0, padx=10, pady=20)
        label_panel.bind("<Button-1>", lambda e, btn=label_panel: seleccionar_opcion(btn))

    ventana_juego.mainloop()


Button(ventana_configuracion, text="Prueba", command=juego_letras_numeros).place(x=0)

ventana_configuracion.mainloop()
