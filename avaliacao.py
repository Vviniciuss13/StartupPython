import tkinter as tk
import bd
from classes import Candidato
import telaCadastro as cadastro
import telaPesquisa as pesquisa
import aspose.pdf as ap
import aspose.pdf as ap

def enterCadastrar(e):
    buttonCadastrar['background'] = "#315F21"

def outCadastrar(o):
    buttonCadastrar['background'] = "#3D712A"

def enterPesquisar(o):
    buttonHomePesquisar['background'] = "#1D2A57"

def outPesquisar(o):
    buttonHomePesquisar['background'] = "#2A3D7E"

def enterPdf(o):
    buttonPdf['background'] = "#1D2A57"

def outPdf(o):
    buttonPdf['background'] = "#A67C28"

def gerarPdf():
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Hello,world!")
    page.paragraphs.add(text_fragment)
    document.save("output.pdf")

janela = tk.Tk()
janela.geometry("850x500")
janela.configure(background="#7EACB2")

title = tk.Label(janela, text="Startup", font=("@DFKai-SB", 30), bg="#7EACB2")
title.pack(pady=10)

frame = tk.Frame(janela, bg="#7EACB2")

buttonHomePesquisar = tk.Button(frame, text="Pesquisar Candidato", command=pesquisa.abrirPesquisa)
buttonHomePesquisar.configure(bg='#2A3D7E', fg='#fff', border=0)
buttonHomePesquisar.grid(column=0, row=0, pady=10, ipadx=40, ipady=30)
buttonHomePesquisar.bind("<Enter>", enterPesquisar)
buttonHomePesquisar.bind("<Leave>", outPesquisar)

buttonCadastrar = tk.Button(frame, text="Cadastrar Candidato", command=cadastro.abrirCadastro)
buttonCadastrar.configure(bg='#3D712A', fg='#fff', border=0)
buttonCadastrar.grid(column=2, row=0, padx=30, pady=10, ipadx=40, ipady=30)
buttonCadastrar.bind("<Enter>", enterCadastrar)
buttonCadastrar.bind("<Leave>", outCadastrar)

frame.pack()

buttonPdf = tk.Button(janela, text="gerar pdf", command=gerarPdf)
buttonPdf.configure(bg='#CF9A32', fg='#fff', border=0)

buttonPdf.pack(padx=30, pady=10, ipadx=40, ipady=30)
buttonPdf.bind("<Enter>", enterPdf)
buttonPdf.bind("<Leave>", outPdf)

janela.mainloop()