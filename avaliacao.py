import tkinter as tk
import bd
from classes import Candidato

### PESQUISA ######

def abrirPesquisa():
    janelaPesquisa = tk.Tk()
    janelaPesquisa.geometry("850x500")


    title = tk.Label(janelaPesquisa, text="Startup: Escolha dos Candidatos")
    title.pack()

    instrucao = tk.Label(janelaPesquisa, text="Escolha os Requisitos:")
    instrucao.pack()

    frame = tk.Frame(janelaPesquisa)

    # Labels
    entrevistaLabel = tk.Label(frame, text="Nota Mínima da Entrevista: ")
    entrevistaLabel.grid(column=0, row=2, pady=15)

    teoricoLabel = tk.Label(frame, text="Nota Mínima da prova teorica: ")
    teoricoLabel.grid(column=1, row=2)

    praticoLabel = tk.Label(frame, text="Nota Mínima da prova pratica: ")
    praticoLabel.grid(column=0, row=4)

    softSkillLabel = tk.Label(frame, text="Nota Mínima sobre a SoftSkill: ")
    softSkillLabel.grid(column=1, row=4)

    # INPUTS
    entrevistaEntry = tk.Entry(frame)
    entrevistaEntry.insert(0, "0")
    entrevistaEntry.grid(column=0, row=3, padx=10)

    teoricoEntry = tk.Entry(frame)
    teoricoEntry.insert(0, "0")
    teoricoEntry.grid(column=1, row=3, padx=10)

    praticoEntry = tk.Entry(frame)
    praticoEntry.insert(0, "0")
    praticoEntry.grid(column=0, row=5, padx=10)

    softSkillEntry = tk.Entry(frame)
    softSkillEntry.insert(0, "0")
    softSkillEntry.grid(column=1, row=5, padx=10)

    # BUTTON 
    buttonPesquisar = tk.Button(janelaPesquisa, text="Pesquisar Candidato", command=lambda: mostrarResultados(entrevistaEntry.get(), teoricoEntry.get(), praticoEntry.get(), softSkillEntry.get()))

    frame.pack()

    buttonPesquisar.pack(pady=20, ipadx=10, ipady=10)

def mostrarResultados(entrevista, teorico, pratico, softSkill):
    janelaResultados = tk.Toplevel()
    janelaResultados.geometry("550x350")

    candidatos = len(bd.pesquisarCandidato(entrevista, teorico, pratico, softSkill))
    print(candidatos)
    for i in range(candidatos):
            for j in range(8):
                
                e = tk.Entry(janelaResultados, width=5, fg='blue',
                               font=('Arial',16,'bold'))
                 
                e.grid(row=i, column=j)
                e.insert(0, candidatos[i][j])
    if(candidatos == 0):
        avisoLabel = tk.Label(janelaResultados, text="Não há candidatos para essa vaga")
        avisoLabel.pack(pady=10)

### INSERIR

def abrirCadastro():
    janelaInserir = tk.Toplevel()
    janelaInserir.geometry("850x500")

    title = tk.Label(janelaInserir, text="Startup: Cadastrar Usuário")
    title.pack(pady=10)

    instrucoes = tk.Label(janelaInserir, text="Informações: ")
    instrucoes.pack(pady=10)

    frame = tk.Frame(janelaInserir)

    # Labels
    nomeLabel = tk.Label(frame, text="Nome: ")
    nomeLabel.grid(column=0, row=2, pady=15)

    telefoneLabel = tk.Label(frame, text="Telefone: ")
    telefoneLabel.grid(column=1, row=2)

    minibioLabel = tk.Label(frame, text="MiniBio: ")
    minibioLabel.grid(column=2, row=2)

    entrevistaLabel = tk.Label(frame, text="Nota Mínima da Entrevista: ")
    entrevistaLabel.grid(column=3, row=2, pady=15)

    teoricoLabel = tk.Label(frame, text="Nota Mínima da prova teorica: ")
    teoricoLabel.grid(column=0, row=4)

    praticoLabel = tk.Label(frame, text="Nota Mínima da prova pratica: ")
    praticoLabel.grid(column=1, row=4)

    softSkillLabel = tk.Label(frame, text="Nota Mínima sobre a SoftSkill: ")
    softSkillLabel.grid(column=2, row=4)

    # INPUTS
    nomeEntry = tk.Entry(frame)
    nomeEntry.insert(0, "0")
    nomeEntry.grid(column=0, row=3, padx=10)

    telefoneEntry = tk.Entry(frame)
    telefoneEntry.insert(0, "0")
    telefoneEntry.grid(column=1, row=3, padx=10)

    minibioEntry = tk.Entry(frame)
    minibioEntry.insert(0, "0")
    minibioEntry.grid(column=2, row=3, padx=10)

    entrevistaEntry = tk.Entry(frame)
    entrevistaEntry.insert(0, "0")
    entrevistaEntry.grid(column=3, row=3, padx=10)

    teoricoEntry = tk.Entry(frame)
    teoricoEntry.insert(0, "0")
    teoricoEntry.grid(column=0, row=5, padx=10)

    praticoEntry = tk.Entry(frame)
    praticoEntry.insert(0, "0")
    praticoEntry.grid(column=1, row=5, padx=10)

    softSkillEntry = tk.Entry(frame)
    softSkillEntry.insert(0, "0")
    softSkillEntry.grid(column=2, row=5, padx=10)

    buttonInserir = tk.Button(frame, text="Inserir Candidato", command=lambda: print("oi"))
    buttonInserir.grid(column=3, row=5, padx=10)

    frame.pack()




janela = tk.Tk()
janela.geometry("850x500")
title = tk.Label(janela, text="Startup")
title.pack(pady=10)

buttonHomePesquisar = tk.Button(janela, text="Pesquisar Candidato", command=abrirPesquisa)
buttonHomePesquisar.pack(pady=10)

buttonCadastrar = tk.Button(janela, text="Cadastrar Candidato", command=abrirCadastro)
buttonCadastrar.pack(pady=10)

janela.mainloop()