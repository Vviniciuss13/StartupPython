import tkinter as tk
import bd
from classes import Candidato
import telaCadastro as cadastro
import telaPesquisa as pesquisa

janela = tk.Tk()
janela.geometry("850x500")
title = tk.Label(janela, text="Startup")
title.pack(pady=10)

buttonHomePesquisar = tk.Button(janela, text="Pesquisar Candidato", command=pesquisa.abrirPesquisa)
buttonHomePesquisar.pack(pady=10)

buttonCadastrar = tk.Button(janela, text="Cadastrar Candidato", command=cadastro.abrirCadastro)
buttonCadastrar.pack(pady=10)

janela.mainloop()