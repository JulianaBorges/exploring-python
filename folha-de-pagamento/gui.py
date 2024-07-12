from tkinter import *
from tkinter import ttk, messagebox

# cores ---------------------
cor_0 = "#595959"
cor_fundo_1 = "#ECE9E2"
cor_fundo_2 = "#595959"
cor_letra = "#403d3d"


# Criando janela -------------

janela = Tk()
janela.title("")
janela.geometry('490x610')
janela.configure(background=cor_fundo_1)
janela.resizable(width=FALSE, height=FALSE)

# frames
frameCima = Frame(janela, width=500, height=70, bg=cor_fundo_1, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2,)

frameMeio = Frame(janela, width=500, height=300,bg=cor_fundo_2, relief="solid")
frameMeio.grid(row=1, column=0, stick=NSEW)

frameBaixo = Frame(janela, width=500, height=150, bg=cor_fundo_1, relief="raised")
frameBaixo.grid(row=2, column=0, pady=10, sticky=NSEW)


# frame Cime ---------------------------------------------------

app_logo = Label(frameCima, text="Folha de Pagamento", compound=LEFT, padx=5, anchor= NW, font=('arial 22'), bg=cor_fundo_1, fg=cor_fundo_2)
app_logo.place(x=10, y=20)

janela.mainloop()
