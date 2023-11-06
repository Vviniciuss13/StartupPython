import tkinter as tk
import bd
from classes import Candidato

### PESQUISA ######

def abrirPesquisa():
    janelaPesquisa = tk.Toplevel()
    janelaPesquisa.geometry("500x350")

    title = tk.Label(janelaPesquisa, text="Startup: Escolha dos Candidatos")
    title.pack(pady=10)

    instrucao = tk.Label(janelaPesquisa, text="Escolha os Requisitos:")
    instrucao.pack(pady=20)

    frameEntrevista = tk.Frame(janelaPesquisa, height=200, width=80)
    frameTeorico = tk.Frame(janelaPesquisa, height=200, width=80)
    framePratico = tk.Frame(janelaPesquisa, height=200, width=80)
    frameSoftSkill = tk.Frame(janelaPesquisa, height=200, width=80)

    # Labels
    entrevistaLabel = tk.Label(frameEntrevista, text="Nota Mínima da Entrevista: ")
    entrevistaLabel.pack()

    teoricoLabel = tk.Label(frameTeorico, text="Nota Mínima da prova teorica: ")
    teoricoLabel.pack()

    praticoLabel = tk.Label(framePratico, text="Nota Mínima da prova pratica: ")
    praticoLabel.pack()

    softSkillLabel = tk.Label(frameSoftSkill, text="Nota Mínima sobre a SoftSkill: ")
    softSkillLabel.pack()

    # INPUTS
    entrevistaEntry = tk.Entry(frameEntrevista)
    entrevistaEntry.insert(0, "0")
    entrevistaEntry.pack()

    teoricoEntry = tk.Entry(frameTeorico)
    teoricoEntry.insert(0, "0")
    teoricoEntry.pack()

    praticoEntry = tk.Entry(framePratico)
    praticoEntry.insert(0, "0")
    praticoEntry.pack()

    softSkillEntry = tk.Entry(frameSoftSkill)
    softSkillEntry.insert(0, "0")
    softSkillEntry.pack()

    frameEntrevista.pack()
    frameTeorico.pack()
    framePratico.pack()
    frameSoftSkill.pack()

    # BUTTON 
    buttonPesquisar = tk.Button(janelaPesquisa, text="Pesquisar Candidato", command=lambda: mostrarResultados(entrevistaEntry.get(), teoricoEntry.get(), praticoEntry.get(), softSkillEntry.get()))
    buttonPesquisar.pack(pady=25)

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



janela = tk.Tk()
janela.geometry("500x350")
title = tk.Label(janela, text="Startup")
title.pack(pady=10)

buttonCadastrar = tk.Button(janela, text="Pesquisar Candidato", command=abrirPesquisa)
buttonCadastrar.pack(pady=10)

### INSERIR


janela.mainloop()