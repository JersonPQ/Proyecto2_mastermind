from tkinter import *


def menu_principal():
    global menu_principal
    menu_principal = Tk()
    menu_principal.title("Mastermind Game")
    logo = PhotoImage(file="mastermind_copy.png")
    Label(menu_principal, image=logo).pack()

    # texto = Label(ventana, text="Frame", font="Sans_Serif 15", bg="gray", fg="white")  # Buscar arreglo al font
    # texto.grid(row=0, column=0, columnspan=3, pady=20)

    jugar = Button(menu_principal, text="Jugar", width=15, height=2)  # agregar el command= para darle funcionalidad
    jugar.pack()
    conf = Button(menu_principal, text="Configuración", width=15, height=2, command=menu_conf)
    conf.pack()
    top10_resumen = Button(menu_principal, text="Top 10 resumen", width=15, height=2)
    top10_resumen.pack()
    top10_detalle = Button(menu_principal, text="Top 10 detalle", width=15, height=2)
    top10_detalle.pack()

    menu_principal.mainloop()


def menu_conf():
    global menu_conf
    menu_conf = Toplevel()
    menu_conf.title("Configuración")
    menu_principal.withdraw()

    Button(menu_conf, text="Dificultad", width=15, height=2).pack()
    Button(menu_conf, text="Reloj", width=15, height=2).pack()
    Button(menu_conf, text="Posición panel", width=15, height=2).pack()
    Button(menu_conf, text="Elegir panel", width=15, height=2).pack()
    Button(menu_conf, text="Volver menú principal", width=15, height=2, command=volver_menu_top10_res_a_menu_prin).pack()

    menu_conf.mainloop()


def volver_menu_top10_res_a_menu_prin():
    menu_principal.deiconify()
    menu_conf.destroy()


menu_principal()
