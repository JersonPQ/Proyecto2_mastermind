from tkinter import *
from tkinter import messagebox
import random
import pickle
from datetime import datetime


def configuracion():
    ventana_configuracion = Toplevel()
    ventana_configuracion.title("Mastermind")
    ventana_configuracion.geometry("1466x768")
    ventana_configuracion.state("zoomed")

    fondo_configuracion = PhotoImage(file="fondo_configuracion.png")

    # -------------------------------------------- Funciones -------------------------------------------- #

    def guardar_configuracion():
        configuracion_partida = open("mastermind2022configuracion.dat", "wb")
        pickle.dump(seleccion_dificultad.get(), configuracion_partida)
        pickle.dump(seleccion_reloj.get(), configuracion_partida)
        pickle.dump(seleccion_posicion_panel.get(), configuracion_partida)
        pickle.dump(seleccion_panel.get(), configuracion_partida)
        configuracion_partida.close()

        ventana_configuracion.destroy()

    # -------------------------------------------- Labels -------------------------------------------- #
    Label(ventana_configuracion, image=fondo_configuracion, bd=0).pack()

    Label(ventana_configuracion, text="Dificultad:", bg="white", font=("Open Sans", 12)).place(x=225, y=90)

    Label(ventana_configuracion, text="Reloj:", bg="white", font=("Open Sans", 12)).place(x=225, y=430)

    Label(ventana_configuracion, text="Posición del panel:", bg="white", font=("Open Sans", 12)).place(x=925, y=90)

    Label(ventana_configuracion, text="Panel de elementos para utilizar:", bg="white", font=("Open Sans", 12)).place(
        x=925, y=430)

    # -------------------------------------------- Radiobuttons -------------------------------------------- #
    nivel_facil = Radiobutton(ventana_configuracion, text="Nivel Fácil", bg="white", font=("Open Sans", 12),
                              variable=seleccion_dificultad, value=1)
    nivel_facil.place(x=325, y=130)

    nivel_medio = Radiobutton(ventana_configuracion, text="Nivel Medio", bg="white", font=("Open Sans", 12),
                              variable=seleccion_dificultad, value=2)
    nivel_medio.place(x=325, y=170)

    nivel_dificil = Radiobutton(ventana_configuracion, text="Nivel Difícil", bg="white", font=("Open Sans", 12),
                                variable=seleccion_dificultad, value=3)
    nivel_dificil.place(x=325, y=210)

    reloj_si = Radiobutton(ventana_configuracion, text="Si", bg="white", font=("Open Sans", 12),
                           variable=seleccion_reloj,
                           value=1)
    reloj_si.place(x=325, y=470)

    reloj_no = Radiobutton(ventana_configuracion, text="No", bg="white", font=("Open Sans", 12),
                           variable=seleccion_reloj,
                           value=2)
    reloj_no.place(x=325, y=510)

    reloj_por_jugada = Radiobutton(ventana_configuracion, text="Cronómetro por jugada", bg="white",
                                   font=("Open Sans", 12),
                                   variable=seleccion_reloj, value=3)
    reloj_por_jugada.place(x=325, y=550)

    reloj_por_juego = Radiobutton(ventana_configuracion, text="Cronómetro por juego", bg="white",
                                  font=("Open Sans", 12),
                                  variable=seleccion_reloj, value=4)
    reloj_por_juego.place(x=325, y=590)

    posicion_panel_derecha = Radiobutton(ventana_configuracion, text="Derecha", bg="white", font=("Open Sans", 12),
                                         variable=seleccion_posicion_panel, value=1)
    posicion_panel_derecha.place(x=1025, y=130)

    posicion_panel_izquierda = Radiobutton(ventana_configuracion, text="Izquierda", bg="white", font=("Open Sans", 12),
                                           variable=seleccion_posicion_panel, value=2)
    posicion_panel_izquierda.place(x=1025, y=170)

    panel_colores = Radiobutton(ventana_configuracion, text="Colores", bg="white", font=("Open Sans", 12),
                                variable=seleccion_panel,
                                value=1)
    panel_colores.place(x=1025, y=470)

    panel_letras = Radiobutton(ventana_configuracion, text="Letras", bg="white", font=("Open Sans", 12),
                               variable=seleccion_panel, value=2)
    panel_letras.place(x=1025, y=510)

    panel_numeros = Radiobutton(ventana_configuracion, text="Números", bg="white", font=("Open Sans", 12),
                                variable=seleccion_panel,
                                value=3)
    panel_numeros.place(x=1025, y=550)

    # -------------------------------------------- Buttons -------------------------------------------- #
    Button(ventana_configuracion, image=back_button, borderwidth=0, command=guardar_configuracion).place(x=20, y=20)

    ventana_configuracion.mainloop()


# -------------------------------------------- Función para juego colores -------------------------------------------- #


def juego_colores():
    global cantidad_filas, cantidad_columnas, matriz_tablero, matriz_tabla_calificar, matriz_tabla_calificar, \
        matriz_tabla_calificar, posicion_fila, negros, blancos, started, nombre_jugador, secuencia_a_adivinar, \
        partida_guardada, opciones, opcion_seleccionada, opcion_del_momento, nivel, posicion_botones_izquierda, posicion_panel_eje_x
    global horas, minutos, segundos, tiempo_limite

    ventana_juego = Toplevel()
    ventana_juego.title("Mastermind")
    ventana_juego.geometry("1466x768")
    ventana_juego.configure(bg="white")
    ventana_juego.state("zoomed")

    logo = PhotoImage(file="mastermind_copy_(Logo mas pequeno).png")
    start_button = PhotoImage(file="START_button_recortado_(boton).png")
    cancel_button = PhotoImage(file="CANCEL_button_recortado_(boton).png")
    check_button = PhotoImage(file="CALIFICAR_recortado_(boton).png")
    save_button_img = PhotoImage(file="SAVE_recortado_(boton).png")
    load_button_img = PhotoImage(file="LOAD_recortado_(boton).png")

    if seleccion_dificultad.get() == 1:
        cantidad_filas = 8
        nivel = "Nivel: Fácil"
    elif seleccion_dificultad.get() == 2:
        cantidad_filas = 7
        nivel = "Nivel: Medio"
    elif seleccion_dificultad.get() == 3:
        cantidad_filas = 6
        nivel = "Nivel: Difícil"

    if seleccion_reloj.get() != 2:
        horas = 0
        minutos = 0
        segundos = 0

    if seleccion_posicion_panel.get() == 1:
        posicion_botones_izquierda = 150
        posicion_panel_eje_x = 1060
    elif seleccion_posicion_panel.get() == 2:
        posicion_botones_izquierda = 1060
        posicion_panel_eje_x = 150

    cantidad_columnas = 4
    matriz_tablero = []
    matriz_tabla_calificar = []
    posicion_fila = 0
    negros = 0
    blancos = 0

    started = False
    nombre_jugador = StringVar(ventana_juego)
    tiempo_limite = StringVar(ventana_juego)
    secuencia_a_adivinar = 0
    partida_guardada = []
    opciones = ["sky blue", "orange", "red", "green", "brown", "yellow"]
    opcion_seleccionada = opciones[0]
    opcion_del_momento = opcion_seleccionada

    # -------------------------------------------- Funciones -------------------------------------------- #

    def start():
        global started, opciones, boton_start, posicion_fila, secuencia_a_adivinar, negros, blancos, entrada_nombre_jugador, tiempo_inicio, tiempo_limite
        global corriendo_crono, corriendo_crono_por_jugada, horas_por_jugada, minutos_por_jugada, segundos_por_jugada, tiempos_por_fila

        if not started and 30 >= len(entrada_nombre_jugador.get()) >= 2:
            if seleccion_reloj.get() != 2:
                if (seleccion_reloj.get() == 3 or seleccion_reloj.get() == 4) and not ("02:59:59" >= entry_tiempo_limite.get() >= "00:00:02"):
                    print("Favor primero poner tiempo límite")
                    return

                started = True
                corriendo_crono = False
                # entry_tiempo_limite.config(state="disabled")  #################################### terminar
                iniciar_crono()

            if seleccion_reloj.get() == 1:
                horas_por_jugada = 0
                minutos_por_jugada = 0
                segundos_por_jugada = 0
                tiempos_por_fila = []
                corriendo_crono_por_jugada = False
                iniciar_crono_por_jugada()

            started = True
            posicion_fila = 0
            negros = 0
            blancos = 0
            secuencia_a_adivinar = random.choices(opciones, k=4)

            boton_start.configure(image=check_button, command=lambda: cambiar_fila(posicion_fila))
            mensaje_limite_tiempo.place_forget()
            mensaje_perdio_partida.place_forget()
            mensaje_gano_partida.place_forget()

            # limpia text de los cuadritos en caso de haber terminado un juego y lo vuelve a iniciar
            for x in range(cantidad_filas):
                for y in range(cantidad_columnas):
                    matriz_tablero[x][y].configure(bg="#f0f0f0")

            # habilita los cuadritos que están en la fila 0
            for cuadro in matriz_tablero[posicion_fila]:
                cuadro.bind("<Button-1>", lambda e, btn=cuadro: poner_opcion(btn))

            # resetea los cuadritos de calificar
            for fila_calificar in matriz_tabla_calificar:
                for cuadrito_calificar in fila_calificar:
                    cuadrito_calificar.config(bg="orange")

            print(f"Secuencia a adivinar: {secuencia_a_adivinar}")
            print("Juego iniciado")
        else:
            print("Favor ingrese un nombre entre 2 y 30 caracteres.")

    def cancel():
        global started, boton_start, cantidad_filas, matriz_tablero, negros, blancos

        if started:
            confirmacion = messagebox.askquestion("¡Oh oh!", "¿Estás seguro de cancelar la partida?")

            if confirmacion == "no":
                return

            started = False
            negros = 0
            blancos = 0
            boton_start.configure(image=start_button, command=lambda: start())
            pausar_reset_crono()

            # deshabilita los cuadritos de el tablero
            for fila in matriz_tablero:
                for cuadro in fila:
                    cuadro.unbind("<Button-1>")

            # resetea los cuadritos de calificar
            for fila_calificar in matriz_tabla_calificar:
                for cuadrito_calificar in fila_calificar:
                    cuadrito_calificar.config(bg="orange")

            # limpia color de los cuadritos en caso de clickear cancel
            for x in range(cantidad_filas):
                for y in range(cantidad_columnas):
                    matriz_tablero[x][y].configure(bg="#f0f0f0")

            print("Juego cancelado")
        else:
            print("Juego no ha sido iniciado")

    def poner_opcion(label):
        if started:
            # da valor al label clickeado
            label.configure(bg=opcion_seleccionada)
            print(label)

    def seleccionar_opcion(label):
        global opcion_seleccionada, opcion_del_momento, opcion_del_momento_label

        if started:
            # toma el valor del label clickeado (los del panel)
            opcion_seleccionada = label['bg']
            opcion_del_momento = opcion_seleccionada
            opcion_del_momento_label.config(bg=opcion_del_momento, text=opcion_del_momento)
            print(label)

    def cambiar_fila(row):
        global posicion_fila, started, secuencia_a_adivinar, negros, blancos, tiempo_partida
        global horas, minutos, segundos, horas_por_jugada, minutos_por_jugada, segundos_por_jugada
        global jugadas_nivel_facil, jugadas_nivel_medio, jugadas_nivel_dificil

        negros = 0
        blancos = 0
        i_cuadrito_blanco = 0


        # valida de que todos los cuadritos tengan un valor y no estén vacíos
        for elemento in matriz_tablero[row]:
            if "#f0f0f0" == elemento["bg"]:
                return

            print(row)

        if seleccion_reloj.get() == 3:
            horas, minutos, segundos = 0, 0, 0
            iniciar_crono()
        elif seleccion_reloj.get() == 1:
            tiempos_por_fila.append(f"{horas_string_por_jugada}:{minutos_string_por_jugada}:{segundos_string_por_jugada}")
            horas_por_jugada = 0
            minutos_por_jugada = 0
            segundos_por_jugada = 0
            iniciar_crono_por_jugada()
            
        # revisa si las letras son iguales a las de la secuencia creada
        for i_elemento_revisar, elemento_revisar in enumerate(matriz_tablero[posicion_fila]):
            if elemento_revisar["bg"] == secuencia_a_adivinar[i_elemento_revisar]:  # type: ignore
                negros += 1
            elif elemento_revisar["bg"] in secuencia_a_adivinar:
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
            boton_start.configure(image=start_button, command=start)
            started = False
            mensaje_gano_partida.place(x=posicion_botones_izquierda + 40, y=650)

            if seleccion_reloj.get() != 2:
                # toma el tiempo que tardó en terminar la partida
                tiempo_partida = crono_label["text"]
                print(f"Tiempo en terminar la partida: {tiempo_partida}")

            if seleccion_reloj.get() == 1:
                fecha_hora = datetime.now()

                if nivel == "Nivel: Fácil":
                    jugadas_nivel_facil.append([entrada_nombre_jugador.get(), tiempo_partida, secuencia_a_adivinar, fecha_hora.date(), fecha_hora.time(), tiempos_por_fila])
                elif nivel == "Nivel: Medio":
                    jugadas_nivel_medio.append([entrada_nombre_jugador.get(), tiempo_partida, secuencia_a_adivinar, fecha_hora.date(), fecha_hora.time(), tiempos_por_fila])
                else:
                    jugadas_nivel_dificil.append([entrada_nombre_jugador.get(), tiempo_partida, secuencia_a_adivinar, fecha_hora.date(), fecha_hora.time(), tiempos_por_fila])

                # ordena las listas de manera descendente
                jugadas_nivel_facil = sorted(jugadas_nivel_facil, key=lambda datos: datos[1])
                jugadas_nivel_medio = sorted(jugadas_nivel_medio, key=lambda datos: datos[1])
                jugadas_nivel_dificil = sorted(jugadas_nivel_dificil, key=lambda datos: datos[1])
                
                # de la lista toma solo los 10 primeros
                jugadas_nivel_facil = jugadas_nivel_facil[:10]
                jugadas_nivel_medio = jugadas_nivel_medio[:10]
                jugadas_nivel_dificil = jugadas_nivel_dificil[:10]

                top_10["Facil"] = jugadas_nivel_facil
                top_10["Medio"] = jugadas_nivel_medio
                top_10["Dificil"] = jugadas_nivel_dificil

                archivo_top10 = open("mastermind2022top10.dat", "wb")
                pickle.dump(top_10, archivo_top10)
                archivo_top10.close()

            pausar_reset_crono()
            print("¡HAS GANADO!")

            return

        posicion_fila += 1

        # si posicion de fila es == a cantidad de filas se cambia el boton y se "reinicia el conteo de filas"
        if posicion_fila == cantidad_filas:
            boton_start.configure(image=start_button, command=lambda: start())
            started = False
            mensaje_perdio_partida.place(x=posicion_botones_izquierda + 30, y=650)
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

            # toma valor de cada "bg" de cada cuadrito de la matriz tablero
            for i_matriz in matriz_partida:
                fila = []

                for j_matriz in i_matriz:
                    fila.append(j_matriz["bg"])

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
            pickle.dump(opciones, archivo_partida)
            pickle.dump(cantidad_filas, archivo_partida)
            pickle.dump(posicion_botones_izquierda, archivo_partida)
            pickle.dump(posicion_panel_eje_x, archivo_partida)
            pickle.dump(seleccion_reloj.get(), archivo_partida)

            if seleccion_reloj.get() != 2:
                pickle.dump(horas, archivo_partida)
                pickle.dump(minutos, archivo_partida)
                pickle.dump(segundos, archivo_partida)

                if seleccion_reloj.get() in [3, 4]:
                    pickle.dump(entry_tiempo_limite.get(), archivo_partida)
                if seleccion_reloj.get() == 1:
                    pickle.dump(horas_por_jugada, archivo_partida)
                    pickle.dump(minutos_por_jugada, archivo_partida)
                    pickle.dump(segundos_por_jugada, archivo_partida)
                    pickle.dump(tiempos_por_fila, archivo_partida)

            archivo_partida.close()

    def load():
        global started, posicion_fila, partida_guardada, secuencia_a_adivinar, nombre_jugador, nivel, opciones, label_panel, opcion_seleccionada, opcion_del_momento, opcion_del_momento_label, \
            fila_calificadora, cantidad_filas, label_calificar, label_tablero, fila_tablero, matriz_tablero, matriz_tabla_calificar, posicion_botones_izquierda, posicion_panel_eje_x, \
            seleccion_reloj
        global horas, minutos, segundos, corriendo_crono, tiempos_por_fila, corriendo_crono_por_jugada, horas_por_jugada, minutos_por_jugada, segundos_por_jugada

        if not started:
            # quita los labels de el tablero anterior de el tablero de juego y el tablero de calificacion
            for fila_label in matriz_tablero:
                for label in fila_label:
                    label.grid_forget()
                    
            for fila_label_califica in matriz_tabla_calificar:
                for label_califica in fila_label_califica:
                    label_califica.grid_forget()
            
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
            opciones = partida_guardada[6]
            cantidad_filas = partida_guardada[7]
            posicion_botones_izquierda = partida_guardada[8]
            posicion_panel_eje_x = partida_guardada[9]
            seleccion_reloj.set(partida_guardada[10])
            
            if seleccion_reloj.get() in [3, 4]:
                tiempo_limite.set(partida_guardada[14])

            archivo_partida.close()

            print(f"Secuencia a adivinar: {secuencia_a_adivinar}")
            # resetea el label de la opcion seleccionada
            opcion_seleccionada = opciones[0]
            opcion_del_momento = opcion_seleccionada
            opcion_del_momento_label.config(bg=opcion_del_momento)

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
                    label_tablero = Label(tablero, bg="#f0f0f0", width=5, height=2)
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
            for i_matriz in range(cantidad_filas):
                for j_matriz in range(cantidad_columnas):
                    matriz_tablero[i_matriz][j_matriz]["bg"] = datos_cuadritos_tablero[i_matriz][j_matriz]

            boton_start.configure(image=check_button, command=lambda: cambiar_fila(posicion_fila))

            # cambia los colores del tablero de calificación al de los colores de los colores
            for fila_califica in range(cantidad_columnas):
                for cuadrito in range(cantidad_columnas):
                    matriz_tabla_calificar[fila_califica][cuadrito]["bg"] = datos_colores_tablero[fila_califica][
                        cuadrito]

            for cuadro in matriz_tablero[posicion_fila]:
                cuadro.bind("<Button-1>", lambda e, btn=cuadro: poner_opcion(btn))

            # crea el nuevo panel con los datos cargados
            for i in range(len(opciones)):
                label_panel = Label(panel_opciones, bg=opciones[i], width=5, height=2)
                label_panel.grid(row=i, column=0, padx=10, pady=20)
                label_panel.bind("<Button-1>", lambda e, btn=label_panel: seleccionar_opcion(btn))

            started = True

            if seleccion_reloj.get() != 2:
                horas, minutos, segundos = partida_guardada[11], partida_guardada[12], partida_guardada[13]
                corriendo_crono = False
                crono_label.place(x=posicion_botones_izquierda + 90, y=600)
                iniciar_crono()

            # desaparece los mensajes de limite tiempo en caso de seleccion reloj sea 1 o 2
            if seleccion_reloj.get() in [1, 2]:
                tiempo_limite_label.place_forget()
                entry_tiempo_limite.place_forget()
                
                if seleccion_reloj.get() == 1:
                    horas_por_jugada = partida_guardada[14]
                    minutos_por_jugada = partida_guardada[15]
                    segundos_por_jugada = partida_guardada[16]
                    tiempos_por_fila = partida_guardada[17]
                    corriendo_crono_por_jugada = False
                    iniciar_crono_por_jugada()
                    
                if seleccion_reloj.get() == 2:
                    crono_label.place_forget()
                    
            # reposiciona label de tiempo limite y el entryde tiempo limite
            elif seleccion_reloj.get() in [3,4]:
                if seleccion_reloj.get() == 3:
                    var_jugada_o_juego = "jugada"
                else:
                    var_jugada_o_juego = "juego"
                
                tiempo_limite_label.config(text=f"Ingrese tiempo límite por {var_jugada_o_juego} \nen formato 00:00:00:")
                tiempo_limite_label.place(x=posicion_botones_izquierda + 30, y=460)
                entry_tiempo_limite.place(x=posicion_botones_izquierda + 60, y=505)

    # funciones para cronómetro en caso de elegir configuración si, por jugada o por juego
    def iniciar_crono():
        global corriendo_crono

        if not corriendo_crono:
            actualizar_crono()
            corriendo_crono = True

    def actualizar_crono():
        global horas, minutos, segundos, actualiza_tiempo, started

        segundos += 1

        if segundos == 60:
            minutos += 1
            segundos = 0

        if minutos == 60:
            horas += 1
            minutos = 0

        horas_string = f"0{horas}"
        minutos_string = f"{minutos}" if minutos > 9 else f"0{minutos}"
        segundos_string = f"{segundos}" if segundos > 9 else f"0{segundos}"
        crono_label.config(text=horas_string + ":" + minutos_string + ":" + segundos_string)

        if seleccion_reloj.get() in [3, 4] and entry_tiempo_limite.get() == crono_label["text"]:
            mensaje_limite_tiempo.place(x=posicion_botones_izquierda + 40, y=650)
            started = False
            boton_start.configure(image=start_button, command=lambda: start())
            pausar_reset_crono()

            # deshabilita los cuadritos de el tablero
            for fila in matriz_tablero:
                for cuadro in fila:
                    cuadro.unbind("<Button-1>")

            # resetea los cuadritos de calificar
            for fila_calificar in matriz_tabla_calificar:
                for cuadrito_calificar in fila_calificar:
                    cuadrito_calificar.config(bg="orange")

            # limpia color de los cuadritos en caso de clickear cancel
            for x in range(cantidad_filas):
                for y in range(cantidad_columnas):
                    matriz_tablero[x][y].configure(bg="#f0f0f0")

            return

        actualiza_tiempo = ventana_juego.after(1000, actualizar_crono)

    def pausar_reset_crono():
        global corriendo_crono, horas, minutos, segundos

        if corriendo_crono:
            # cancelar la funcion de actualizar crono usando after_cancel()
            crono_label.after_cancel(actualiza_tiempo)
            corriendo_crono = False

        horas, minutos, segundos = 0, 0, 0
        crono_label.config(text="00:00:00")

    # funciones de cronómetro para medir el tiempo por jugada en caso de poner reloj en "SI"
    def iniciar_crono_por_jugada():
        global corriendo_crono_por_jugada

        if not corriendo_crono_por_jugada:
            actualizar_crono_por_jugada()
            corriendo_crono_por_jugada = True

    def actualizar_crono_por_jugada():
        global horas_por_jugada, minutos_por_jugada, segundos_por_jugada, actualiza_tiempo_por_jugada, started, horas_string_por_jugada, minutos_string_por_jugada, segundos_string_por_jugada

        segundos_por_jugada += 1

        if segundos_por_jugada == 60:
            minutos_por_jugada += 1
            segundos_por_jugada = 0

        if minutos_por_jugada == 60:
            horas_por_jugada += 1
            minutos_por_jugada = 0

        horas_string_por_jugada = f"0{horas_por_jugada}"
        minutos_string_por_jugada = f"{minutos_por_jugada}" if minutos_por_jugada > 9 else f"0{minutos_por_jugada}"
        segundos_string_por_jugada = f"{segundos_por_jugada}" if segundos_por_jugada > 9 else f"0{segundos_por_jugada}"

        if not started:
            pausar_reset_crono_por_jugada()
            return

        ventana_juego.after(1000, actualizar_crono_por_jugada)

    def pausar_reset_crono_por_jugada():
        global corriendo_crono_por_jugada, horas_por_jugada, minutos_por_jugada, segundos_por_jugada

        if corriendo_crono_por_jugada:
            # cancelar la funcion de actualizar crono usando after_cancel()
            ventana_juego.after_cancel(actualiza_tiempo)
            corriendo_crono_por_jugada = False

        horas_por_jugada, minutos_por_jugada, segundos_por_jugada = 0, 0, 0

    # -------------------------------------------- Frames -------------------------------------------- #

    global botones_izquierda, entry_jugador, start_cancel_buttons, tablero_tabla_calificadora, tablero, panel_opciones, tabla_calificadora

    botones_izquierda = Frame(ventana_juego, bg="white", height=180)
    botones_izquierda.place(x=posicion_botones_izquierda, y=75)

    entry_jugador = Frame(botones_izquierda, bg="white")
    entry_jugador.grid(row=1, column=0, pady=15)

    start_cancel_buttons = Frame(botones_izquierda, bg="white")
    start_cancel_buttons.grid(row=2, column=0, pady=40)

    tablero_tabla_calificadora = Frame(ventana_juego, bg="#b93f70")
    tablero_tabla_calificadora.place(x=600, y=15)

    tablero = Frame(tablero_tabla_calificadora, bg="#b93f70", width=400, height=800)
    tablero.grid(row=0, column=0)

    tabla_calificadora = Frame(tablero_tabla_calificadora, bg="#b93f70", width=150, height=800, padx=5)
    tabla_calificadora.grid(row=0, column=1)

    panel_opciones = Frame(ventana_juego, bg="#121d46", width=100, height=500)
    panel_opciones.place(x=posicion_panel_eje_x, y=15)

    save_load_buttons = Frame(ventana_juego, bg="white", width=210, height=175)
    save_load_buttons.place(x=posicion_panel_eje_x - 40, y=500)

    # -------------------------------------------- Labels -------------------------------------------- #

    global opcion_del_momento_label, nivel_label

    Label(botones_izquierda, image=logo, borderwidth=0, padx=40).grid(row=0, column=0, padx=10, pady=10)
    Label(entry_jugador, text="Jugador:", bg="white", font=("Open Sans", 12), padx=5).grid(row=0, column=0)
    nivel_label = Label(ventana_juego, text=nivel, bg="#ec518f", font=("Open Sans", 12), padx=5, pady=5)
    nivel_label.place(x=1300, y=15)

    opcion_del_momento_label = Label(ventana_juego, text=opcion_del_momento, bg=opcion_del_momento,
                                     font=("Open Sans", 12), padx=5, pady=5)
    opcion_del_momento_label.place(x=1300, y=700)

    mensaje_gano_partida = Label(ventana_juego, text="¡FELICIDADES, GANASTE!", font=("Open Sans", 14), bg="light green")

    mensaje_perdio_partida = Label(ventana_juego, text="¡UPS! No lo has conseguido en esta \n¡A la próxima!",
                                   font=("Open Sans", 12), bg="#f25363")

    mensaje_limite_tiempo = Label(ventana_juego, text="¡Oh oh!\n ¡Te has quedado sin tiempo!", font=("Open Sans", 12),
                                  bg="#f25363")

    entry_tiempo_limite = Entry(ventana_juego, font=("Open Sans", 13), borderwidth=0, justify="center", bg="pink", textvariable=tiempo_limite)

    crono_label = Label(ventana_juego, bg="yellow", text="00:00:00", font=("Open Sans", 20))

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

    save_button = Button(save_load_buttons, image=save_button_img, borderwidth=0, bg="white", padx=42, pady=15,
                         command=lambda: save(matriz_tablero, matriz_tabla_calificar))
    save_button.grid(row=0, column=0, padx=10, pady=10)

    load_button = Button(save_load_buttons, image=load_button_img, borderwidth=0, bg="white", padx=40, pady=15,
                         command=load)
    load_button.grid(row=1, column=0, padx=10, pady=10)

    Button(ventana_juego, image=back_button, borderwidth=0, command=ventana_juego.destroy).place(x=20, y=20)

    # -------------------------------------------- Código -------------------------------------------- #

    if seleccion_reloj.get() == 3:
        var_jugada_o_juego = "jugada"

    else:
        var_jugada_o_juego = "juego"

    tiempo_limite_label = Label(ventana_juego, bg="white",
            text=f"Ingrese tiempo límite por {var_jugada_o_juego} \nen formato 00:00:00:",
            font=("Open Sans", 13))

    if seleccion_reloj.get() != 2:
        if seleccion_reloj.get() != 1:
            tiempo_limite_label.place(x=posicion_botones_izquierda + 30, y=460)
            entry_tiempo_limite.place(x=posicion_botones_izquierda + 60, y=505)

        crono_label.place(x=posicion_botones_izquierda + 90, y=600)

    # for para crear cuadro de los botones de los colores
    for i in range(cantidad_filas):
        fila_tablero = []

        for j in range(cantidad_columnas):
            label_tablero = Label(tablero, bg="#f0f0f0", width=5, height=2)
            label_tablero.grid(row=i, column=j, padx=10, pady=30)
            fila_tablero.append(label_tablero)

        matriz_tablero.append(fila_tablero)

    # for para crear la tabla de calificación
    for i in range(cantidad_filas):
        fila_calificadora = []

        for j in range(4):
            label_calificar = Label(tabla_calificadora, text="", bg="orange", width=1)
            label_calificar.grid(row=i, column=j, padx=5, pady=37)
            fila_calificadora.append(label_calificar)

        matriz_tabla_calificar.append(fila_calificadora)

    # for para crear botones del panel
    for i in range(len(opciones)):
        label_panel = Label(panel_opciones, bg=opciones[i], width=5, height=2)
        label_panel.grid(row=i, column=0, padx=10, pady=20)
        label_panel.bind("<Button-1>", lambda e, btn=label_panel: seleccionar_opcion(btn))

    ventana_juego.mainloop()


# -------------------------------------- Función para juego de letras o números -------------------------------------- #


def juego_letras_numeros():
    global cantidad_filas, cantidad_columnas, matriz_tablero, matriz_tabla_calificar, matriz_tabla_calificar, \
        matriz_tabla_calificar, posicion_fila, negros, blancos, started, nombre_jugador, secuencia_a_adivinar, \
        partida_guardada, opciones, opcion_seleccionada, opcion_del_momento, nivel, posicion_botones_izquierda, posicion_panel_eje_x
    global horas, minutos, segundos, tiempo_limite

    ventana_juego = Toplevel()
    ventana_juego.title("Mastermind")
    ventana_juego.geometry("1466x768")
    ventana_juego.configure(bg="white")
    ventana_juego.state("zoomed")

    logo = PhotoImage(file="mastermind_copy_(Logo mas pequeno).png")
    start_button = PhotoImage(file="START_button_recortado_(boton).png")
    cancel_button = PhotoImage(file="CANCEL_button_recortado_(boton).png")
    check_button = PhotoImage(file="CALIFICAR_recortado_(boton).png")
    save_button_img = PhotoImage(file="SAVE_recortado_(boton).png")
    load_button_img = PhotoImage(file="LOAD_recortado_(boton).png")

    if seleccion_dificultad.get() == 1:
        cantidad_filas = 8
        nivel = "Nivel: Fácil"
    elif seleccion_dificultad.get() == 2:
        cantidad_filas = 7
        nivel = "Nivel: Medio"
    elif seleccion_dificultad.get() == 3:
        cantidad_filas = 6
        nivel = "Nivel: Difícil"

    if seleccion_reloj.get() != 2:
        horas = 0
        minutos = 0
        segundos = 0

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
    tiempo_limite = StringVar(ventana_juego)
    secuencia_a_adivinar = 0
    partida_guardada = []
    opcion_seleccionada = opciones[0]
    opcion_del_momento = f"Opción seleccionada: {opcion_seleccionada}"

    # -------------------------------------------- Funciones -------------------------------------------- #

    def start():
        global started, opciones, boton_start, posicion_fila, secuencia_a_adivinar, negros, blancos, entrada_nombre_jugador
        global corriendo_crono, corriendo_crono_por_jugada, horas_por_jugada, minutos_por_jugada, segundos_por_jugada, tiempos_por_fila

        if not started and 30 >= len(entrada_nombre_jugador.get()) >= 2:
            if seleccion_reloj.get() != 2:
                if (seleccion_reloj.get() == 3 or seleccion_reloj.get() == 4) and not ("02:59:59" >= entry_tiempo_limite.get() >= "00:00:02"):
                    print("Favor primero poner tiempo límite")
                    return

                started = True
                corriendo_crono = False
                # entry_tiempo_limite.config(state="disabled")  #################################### terminar
                iniciar_crono()

            if seleccion_reloj.get() == 1:
                horas_por_jugada = 0
                minutos_por_jugada = 0
                segundos_por_jugada = 0
                tiempos_por_fila = []
                corriendo_crono_por_jugada = False
                iniciar_crono_por_jugada()

            started = True
            posicion_fila = 0
            negros = 0
            blancos = 0
            secuencia_a_adivinar = random.choices(opciones, k=4)

            boton_start.configure(image=check_button, command=lambda: cambiar_fila(posicion_fila))
            mensaje_limite_tiempo.place_forget()
            mensaje_perdio_partida.place_forget()
            mensaje_gano_partida.place_forget()

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

            print(f"Secuencia a adivinar: {secuencia_a_adivinar}")
            print("Juego iniciado")
        else:
            print("Favor ingrese un nombre entre 2 y 30 caracteres.")


    def cancel():
        global started, boton_start, cantidad_filas, matriz_tablero, negros, blancos

        if started:
            confirmacion = messagebox.askquestion("¡Oh oh!", "¿Estás seguro de cancelar la partida?")

            if confirmacion == "no":
                return

            started = False
            negros = 0
            blancos = 0
            boton_start.configure(image=start_button, command=lambda: start())
            pausar_reset_crono()

            # deshabilita los cuadritos de el tablero
            for fila in matriz_tablero:
                for cuadro in fila:
                    cuadro.unbind("<Button-1>")

            # resetea los cuadritos de calificar
            for fila_calificar in matriz_tabla_calificar:
                for cuadrito_calificar in fila_calificar:
                    cuadrito_calificar.config(bg="orange")

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
        global opcion_seleccionada, opcion_del_momento, opcion_del_momento_label

        if started:
            # toma el valor del label clickeado (los del panel)
            opcion_seleccionada = label['text']
            opcion_del_momento = f"Opción seleccionada: {opcion_seleccionada}"
            opcion_del_momento_label.config(text=opcion_del_momento)
            print(label)

    def cambiar_fila(row):
        global posicion_fila, started, secuencia_a_adivinar, negros, blancos, tiempo_partida
        global horas, minutos, segundos, horas_por_jugada, minutos_por_jugada, segundos_por_jugada
        global jugadas_nivel_facil, jugadas_nivel_medio, jugadas_nivel_dificil

        negros = 0
        blancos = 0
        i_cuadrito_blanco = 0



        # valida de que todos los cuadritos tengan un valor y no estén vacíos
        for elemento in matriz_tablero[row]:
            if "" == elemento["text"]:
                return

            print(row)

        if seleccion_reloj.get() == 3:
            horas, minutos, segundos = 0, 0, 0
            iniciar_crono()
        elif seleccion_reloj.get() == 1:
            tiempos_por_fila.append(f"{horas_string_por_jugada}:{minutos_string_por_jugada}:{segundos_string_por_jugada}")
            horas_por_jugada = 0
            minutos_por_jugada = 0
            segundos_por_jugada = 0
            iniciar_crono_por_jugada()
            
        # revisa si las letras son iguales a las de la secuencia creada
        for i_elemento_revisar, elemento_revisar in enumerate(matriz_tablero[posicion_fila]):
            if elemento_revisar["text"] == secuencia_a_adivinar[i_elemento_revisar]:  # type: ignore
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
            boton_start.configure(image=start_button, command=start)
            started = False
            mensaje_gano_partida.place(x=posicion_botones_izquierda + 40, y=650)

            if seleccion_reloj.get() != 2:
                # toma el tiempo que tardó en terminar la partida
                tiempo_partida = crono_label["text"]
                print(f"Tiempo en terminar la partida: {tiempo_partida}")

            if seleccion_reloj.get() == 1:
                fecha_hora = datetime.now()

                if nivel == "Nivel: Fácil":
                    jugadas_nivel_facil.append([entrada_nombre_jugador.get(), tiempo_partida, secuencia_a_adivinar, fecha_hora.date(), fecha_hora.time(), tiempos_por_fila])
                elif nivel == "Nivel: Medio":
                    jugadas_nivel_medio.append([entrada_nombre_jugador.get(), tiempo_partida, secuencia_a_adivinar, fecha_hora.date(), fecha_hora.time(), tiempos_por_fila])
                else:
                    jugadas_nivel_dificil.append([entrada_nombre_jugador.get(), tiempo_partida, secuencia_a_adivinar, fecha_hora.date(), fecha_hora.time(), tiempos_por_fila])

                # ordena las listas de manera descendente
                jugadas_nivel_facil = sorted(jugadas_nivel_facil, key=lambda datos: datos[1])
                jugadas_nivel_medio = sorted(jugadas_nivel_medio, key=lambda datos: datos[1])
                jugadas_nivel_dificil = sorted(jugadas_nivel_dificil, key=lambda datos: datos[1])
                
                # de la lista toma solo los 10 primeros
                jugadas_nivel_facil = jugadas_nivel_facil[:10]
                jugadas_nivel_medio = jugadas_nivel_medio[:10]
                jugadas_nivel_dificil = jugadas_nivel_dificil[:10]

                top_10["Facil"] = jugadas_nivel_facil
                top_10["Medio"] = jugadas_nivel_medio
                top_10["Dificil"] = jugadas_nivel_dificil

                archivo_top10 = open("mastermind2022top10.dat", "wb")
                pickle.dump(top_10, archivo_top10)
                archivo_top10.close()

            pausar_reset_crono()
            print("¡HAS GANADO!")

            return

        posicion_fila += 1

        # si posicion de fila es == a cantidad de filas se cambia el boton y se "reinicia el conteo de filas"
        if posicion_fila == cantidad_filas:
            boton_start.configure(image=start_button, command=lambda: start())
            started = False
            mensaje_perdio_partida.place(x=posicion_botones_izquierda + 30, y=650)
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
            pickle.dump(opciones, archivo_partida)
            pickle.dump(cantidad_filas, archivo_partida)
            pickle.dump(posicion_botones_izquierda, archivo_partida)
            pickle.dump(posicion_panel_eje_x, archivo_partida)
            pickle.dump(seleccion_reloj.get(), archivo_partida)

            if seleccion_reloj.get() != 2:
                pickle.dump(horas, archivo_partida)
                pickle.dump(minutos, archivo_partida)
                pickle.dump(segundos, archivo_partida)

                if seleccion_reloj.get() == 1:
                    pickle.dump(horas_por_jugada, archivo_partida)
                    pickle.dump(minutos_por_jugada, archivo_partida)
                    pickle.dump(segundos_por_jugada, archivo_partida)
                    pickle.dump(tiempos_por_fila, archivo_partida)

                if seleccion_reloj.get() in [3, 4]:
                    pickle.dump(entry_tiempo_limite.get(), archivo_partida)

            archivo_partida.close()

    def load():
        global started, posicion_fila, partida_guardada, secuencia_a_adivinar, nombre_jugador, nivel, opciones, label_panel, opcion_seleccionada, opcion_del_momento, opcion_del_momento_label, \
            fila_calificadora, cantidad_filas, label_calificar, label_tablero, fila_tablero, matriz_tablero, matriz_tabla_calificar, posicion_botones_izquierda, posicion_panel_eje_x, \
            seleccion_reloj
        global horas, minutos, segundos, corriendo_crono, tiempos_por_fila, corriendo_crono_por_jugada, horas_por_jugada, minutos_por_jugada, segundos_por_jugada

        if not started:
            # elimina los labels de la tabla anterior, de la tabla y de la tabla de calificacion
            for fila_label in matriz_tablero:
                for label in fila_label:
                    label.grid_forget()
                    
            for fila_label_califica in matriz_tabla_calificar:
                for label_califica in fila_label_califica:
                    label_califica.grid_forget()
            
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
            opciones = partida_guardada[6]
            cantidad_filas = partida_guardada[7]
            posicion_botones_izquierda = partida_guardada[8]
            posicion_panel_eje_x = partida_guardada[9]
            seleccion_reloj.set(partida_guardada[10])
            
            if seleccion_reloj.get() in [3,4]:
                tiempo_limite.set(partida_guardada[14])
                
            archivo_partida.close()

            print(f"Secuencia a adivinar: {secuencia_a_adivinar}")
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
            for i_matriz in range(cantidad_filas):
                for j_matriz in range(cantidad_columnas):
                    matriz_tablero[i_matriz][j_matriz]["text"] = datos_cuadritos_tablero[i_matriz][j_matriz]

            boton_start.configure(image=check_button, command=lambda: cambiar_fila(posicion_fila))

            # cambia los colores del tablero de calificación al de los colores de los colores
            for fila_califica in range(len(matriz_tablero)):
                for cuadrito in range(len(matriz_tablero[0])):
                    matriz_tabla_calificar[fila_califica][cuadrito]["bg"] = datos_colores_tablero[fila_califica][
                        cuadrito]

            for cuadro in matriz_tablero[posicion_fila]:
                cuadro.bind("<Button-1>", lambda e, btn=cuadro: poner_opcion(btn))

            # crea el nuevo panel con los datos cargados
            for i in range(len(opciones)):
                label_panel = Label(panel_opciones, text=opciones[i], width=5, height=2)
                label_panel.grid(row=i, column=0, padx=10, pady=20)
                label_panel.bind("<Button-1>", lambda e, btn=label_panel: seleccionar_opcion(btn))

            started = True

            if seleccion_reloj.get() != 2:
                horas, minutos, segundos = partida_guardada[11], partida_guardada[12], partida_guardada[13]
                corriendo_crono = False
                crono_label.place(x=posicion_botones_izquierda + 90, y=600)
                iniciar_crono()

            # desaparece los mensajes de limite tiempo en caso de seleccion reloj sea 1 o 2
            if seleccion_reloj.get() in [1, 2]:
                tiempo_limite_label.place_forget()
                entry_tiempo_limite.place_forget()
                
                if seleccion_reloj.get() == 1:
                    horas_por_jugada = partida_guardada[14]
                    minutos_por_jugada = partida_guardada[15]
                    segundos_por_jugada = partida_guardada[16]
                    tiempos_por_fila = partida_guardada[17]
                    corriendo_crono_por_jugada = False
                    iniciar_crono_por_jugada()
                    
                if seleccion_reloj.get() == 2:
                    crono_label.place_forget()
            
            # reposiciona label de tiempo limite y el entryde tiempo limite
            elif seleccion_reloj.get() in [3,4]:
                if seleccion_reloj.get() == 3:
                    var_jugada_o_juego = "jugada"
                else:
                    var_jugada_o_juego = "juego"
                
                tiempo_limite_label.config(text=f"Ingrese tiempo límite por {var_jugada_o_juego} \nen formato 00:00:00:")
                tiempo_limite_label.place(x=posicion_botones_izquierda + 30, y=460)
                entry_tiempo_limite.place(x=posicion_botones_izquierda + 60, y=505)

    # funciones para cronómetro en caso de elegir configuración si, por jugada o por juego
    def iniciar_crono():
        global corriendo_crono

        if not corriendo_crono:
            actualizar_crono()
            corriendo_crono = True

    def actualizar_crono():
        global horas, minutos, segundos, actualiza_tiempo, started

        segundos += 1

        if segundos == 60:
            minutos += 1
            segundos = 0

        if minutos == 60:
            horas += 1
            minutos = 0

        horas_string = f"0{horas}"
        minutos_string = f"{minutos}" if minutos > 9 else f"0{minutos}"
        segundos_string = f"{segundos}" if segundos > 9 else f"0{segundos}"
        crono_label.config(text=horas_string + ":" + minutos_string + ":" + segundos_string)

        if seleccion_reloj.get() in [3, 4] and entry_tiempo_limite.get() == crono_label["text"]:
            mensaje_limite_tiempo.place(x=posicion_botones_izquierda + 40, y=650)
            started = False
            boton_start.configure(image=start_button, command=lambda: start())
            pausar_reset_crono()

            # deshabilita los cuadritos de el tablero
            for fila in matriz_tablero:
                for cuadro in fila:
                    cuadro.unbind("<Button-1>")

            # resetea los cuadritos de calificar
            for fila_calificar in matriz_tabla_calificar:
                for cuadrito_calificar in fila_calificar:
                    cuadrito_calificar.config(bg="orange")

            # limpia texto de los cuadritos en caso de clickear cancel
            for x in range(cantidad_filas):
                for y in range(cantidad_columnas):
                    matriz_tablero[x][y].configure(text="")

            return

        actualiza_tiempo = ventana_juego.after(1000, actualizar_crono)

    def pausar_reset_crono():
        global corriendo_crono, horas, minutos, segundos

        if corriendo_crono:
            # cancelar la funcion de actualizar crono usando after_cancel()
            crono_label.after_cancel(actualiza_tiempo)
            corriendo_crono = False

        horas, minutos, segundos = 0, 0, 0
        crono_label.config(text="00:00:00")

    # funciones de cronómetro para medir el tiempo por jugada en caso de poner reloj en "SI"
    def iniciar_crono_por_jugada():
        global corriendo_crono_por_jugada

        if not corriendo_crono_por_jugada:
            actualizar_crono_por_jugada()
            corriendo_crono_por_jugada = True

    def actualizar_crono_por_jugada():
        global horas_por_jugada, minutos_por_jugada, segundos_por_jugada, actualiza_tiempo_por_jugada, started, horas_string_por_jugada, minutos_string_por_jugada, segundos_string_por_jugada

        segundos_por_jugada += 1

        if segundos_por_jugada == 60:
            minutos_por_jugada += 1
            segundos_por_jugada = 0

        if minutos_por_jugada == 60:
            horas_por_jugada += 1
            minutos_por_jugada = 0

        horas_string_por_jugada = f"0{horas_por_jugada}"
        minutos_string_por_jugada = f"{minutos_por_jugada}" if minutos_por_jugada > 9 else f"0{minutos_por_jugada}"
        segundos_string_por_jugada = f"{segundos_por_jugada}" if segundos_por_jugada > 9 else f"0{segundos_por_jugada}"

        if not started:
            pausar_reset_crono_por_jugada()
            return

        ventana_juego.after(1000, actualizar_crono_por_jugada)

    def pausar_reset_crono_por_jugada():
        global corriendo_crono_por_jugada, horas_por_jugada, minutos_por_jugada, segundos_por_jugada

        if corriendo_crono_por_jugada:
            # cancelar la funcion de actualizar crono usando after_cancel()
            ventana_juego.after_cancel(actualiza_tiempo)
            corriendo_crono_por_jugada = False

        horas_por_jugada, minutos_por_jugada, segundos_por_jugada = 0, 0, 0

    # -------------------------------------------- Frames -------------------------------------------- #

    global botones_izquierda, entry_jugador, start_cancel_buttons, tablero_tabla_calificadora, tablero, panel_opciones, tabla_calificadora

    botones_izquierda = Frame(ventana_juego, bg="white", height=180)
    botones_izquierda.place(x=posicion_botones_izquierda, y=75)

    entry_jugador = Frame(botones_izquierda, bg="white")
    entry_jugador.grid(row=1, column=0, pady=15)

    start_cancel_buttons = Frame(botones_izquierda, bg="white")
    start_cancel_buttons.grid(row=2, column=0, pady=40)

    tablero_tabla_calificadora = Frame(ventana_juego, bg="#1b2c6c")
    tablero_tabla_calificadora.place(x=600, y=15)

    tablero = Frame(tablero_tabla_calificadora, bg="#1b2c6c", width=400, height=800)
    tablero.grid(row=0, column=0)

    tabla_calificadora = Frame(tablero_tabla_calificadora, bg="#1b2c6c", width=150, height=800, padx=5)
    tabla_calificadora.grid(row=0, column=1)

    panel_opciones = Frame(ventana_juego, bg="#b93f70", width=100, height=500)
    panel_opciones.place(x=posicion_panel_eje_x, y=15)

    save_load_buttons = Frame(ventana_juego, bg="white", width=210, height=175)
    save_load_buttons.place(x=posicion_panel_eje_x - 40, y=500)

    # -------------------------------------------- Labels -------------------------------------------- #

    global opcion_del_momento_label, nivel_label

    Label(botones_izquierda, image=logo, borderwidth=0, padx=40).grid(row=0, column=0, padx=10, pady=10)
    Label(entry_jugador, text="Jugador:", bg="white", font=("Open Sans", 12), padx=5).grid(row=0, column=0)

    nivel_label = Label(ventana_juego, text=nivel, bg="#ec518f", font=("Open Sans", 12), padx=5, pady=5)
    nivel_label.place(x=1300, y=15)

    opcion_del_momento_label = Label(ventana_juego, text=opcion_del_momento, bg="#ec518f", font=("Open Sans", 12),
                                     padx=5, pady=5)
    opcion_del_momento_label.place(x=1300, y=700)

    mensaje_gano_partida = Label(ventana_juego, text="¡FELICIDADES, GANASTE!", font=("Open Sans", 14), bg="light green")

    mensaje_perdio_partida = Label(ventana_juego, text="¡UPS! No lo has conseguido en esta \n¡A la próxima!",
                                   font=("Open Sans", 12), bg="#f25363")

    mensaje_limite_tiempo = Label(ventana_juego, text="¡Oh oh!\n ¡Te has quedado sin tiempo!", font=("Open Sans", 12),
                                  bg="#f25363")

    entry_tiempo_limite = Entry(ventana_juego, font=("Open Sans", 13), borderwidth=0, justify="center", bg="pink", textvariable=tiempo_limite)

    crono_label = Label(ventana_juego, bg="yellow", text="00:00:00", font=("Open Sans", 20))  ##################################################

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

    save_button = Button(save_load_buttons, image=save_button_img, borderwidth=0, bg="white", padx=42, pady=15,
                         command=lambda: save(matriz_tablero, matriz_tabla_calificar))
    save_button.grid(row=0, column=0, padx=10, pady=10)

    load_button = Button(save_load_buttons, image=load_button_img, borderwidth=0, bg="white", padx=40, pady=15,
                         command=load)
    load_button.grid(row=1, column=0, padx=10, pady=10)

    Button(ventana_juego, image=back_button, borderwidth=0, command=ventana_juego.destroy).place(x=20, y=20)

    # -------------------------------------------- Código -------------------------------------------- #

    if seleccion_reloj.get() == 3:
        var_jugada_o_juego = "jugada"

    else:
        var_jugada_o_juego = "juego"
        
    tiempo_limite_label = Label(ventana_juego, bg="white",
                                text=f"Ingrese tiempo límite por {var_jugada_o_juego} \nen formato 00:00:00:",
                                font=("Open Sans", 13))

    if seleccion_reloj.get() != 2:
        if seleccion_reloj.get() != 1:
            tiempo_limite_label.place(x=posicion_botones_izquierda + 30, y=460)
            entry_tiempo_limite.place(x=posicion_botones_izquierda + 60, y=505)

        crono_label.place(x=posicion_botones_izquierda + 90, y=600)

    # for para crear cuadro de los botones de las letras
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

        for j in range(4):
            label_calificar = Label(tabla_calificadora, text="", bg="orange", width=1)
            label_calificar.grid(row=i, column=j, padx=5, pady=37)
            fila_calificadora.append(label_calificar)

        matriz_tabla_calificar.append(fila_calificadora)

    # for para crear botones del panel
    for i in range(len(opciones)):
        label_panel = Label(panel_opciones, text=opciones[i], width=5, height=2)
        label_panel.grid(row=i, column=0, padx=10, pady=20)
        label_panel.bind("<Button-1>", lambda e, btn=label_panel: seleccionar_opcion(btn))

    ventana_juego.mainloop()


def juego():
    if seleccion_panel.get() == 1:
        juego_colores()
    else:
        juego_letras_numeros()


ventana_principal = Tk()
ventana_principal.title("Mastermind")
ventana_principal.geometry("1466x768")
ventana_principal.state("zoomed")

logo_mastermind = PhotoImage(file="mastermind_copy.png")
fondo_principal = PhotoImage(file="Fondo_principal.png")
back_button = PhotoImage(file="VOLVER_(boton).png")
play_button = PhotoImage(file="PLAY_button_recortado_(boton).png")
options_button = PhotoImage(file="OPTIONS_button_recortado_(boton).png")

Label(ventana_principal, image=fondo_principal).place(x=0, y=0)

Label(ventana_principal, image=logo_mastermind, borderwidth=0).pack(pady=150)

boton_juego = Button(ventana_principal, image=play_button, borderwidth=0, command=juego)
boton_juego.pack(pady=0)

boton_configuracion = Button(ventana_principal, image=options_button, borderwidth=0, command=configuracion)
boton_configuracion.pack(pady=40)

niveles = ["Nivel: Fácil", "Nivel: Medio", "Nivel: Difícil"]

configuracion_guardada = []

seleccion_dificultad = IntVar()
seleccion_dificultad.set(1)

seleccion_reloj = IntVar()
seleccion_reloj.set(1)

seleccion_posicion_panel = IntVar()
seleccion_posicion_panel.set(1)

seleccion_panel = IntVar()
seleccion_panel.set(1)

top_10 = {}
jugadas_nivel_facil = []
jugadas_nivel_medio = []
jugadas_nivel_dificil = []

try:
    archivo_config = open("mastermind2022configuracion.dat", "rb")

    while True:
        try:
            configuracion_guardada += [pickle.load(archivo_config)]
        except EOFError:
            break

    seleccion_dificultad.set(configuracion_guardada[0])
    seleccion_reloj.set(configuracion_guardada[1])
    seleccion_posicion_panel.set(configuracion_guardada[2])
    seleccion_panel.set(configuracion_guardada[3])
    archivo_config.close()
except FileNotFoundError:
    pass

try:
    archivo_top = open("mastermind2022top10.dat", "rb")
    top_10 = pickle.load(archivo_top)
    archivo_top.close()
    
    jugadas_nivel_facil = top_10["Facil"]
    jugadas_nivel_medio = top_10["Medio"]
    jugadas_nivel_dificil = top_10["Dificil"]
except FileNotFoundError:
    pass

ventana_principal.mainloop()
