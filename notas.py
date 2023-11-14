from tkinter import*
def enviar():
    input = texto.get("1.0",END)
    print(input)
#ventana
window = Tk()
window.title("BLOCK DE NOTAS")
window.iconbitmap("icono/icono.ico")
texto = Text(window,
            bg="#ffffe0",
            font = ("Ink Free", 25),
            heigh = 8,
            width = 20,
            padx=20,
            pady=20,
            fg = "blue")
texto.pack()

boton = Button(window, text="enviar", command=enviar)
boton.pack()



window.mainloop()