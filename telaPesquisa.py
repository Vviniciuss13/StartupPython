import bd
import tkinter as tk
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
    buttonPesquisar = tk.Button(janelaPesquisa, text="Pesquisar Candidato", command=lambda: pesquisar(entrevistaEntry.get(), teoricoEntry.get(), praticoEntry.get(), softSkillEntry.get()))

    frame.pack()

    buttonPesquisar.pack(pady=20, ipadx=10, ipady=10)

def pesquisar(entrevista, teorico, pratico, softSkill):
    notas = [entrevista, teorico, pratico, softSkill]

    mostrarResultados(notas)

def mostrarResultados(notas):
    janelaResultados = tk.Toplevel()
    janelaResultados.geometry("550x350")

    candidatosFrame = []
    candidatos = bd.pesquisarCandidato(notas[0], notas[1], notas[2], notas[3])
    for candidato in candidatos:

        infoFrame = tk.Frame(janelaResultados)

        labelNome = tk.Label(infoFrame, text="Candidato: " + candidato[1])
        labelNome.grid(column=0, row=0)

        labelTelefone = tk.Label(infoFrame, text="Telefone: " + candidato[2])
        labelTelefone.grid(column=0, row=1)

        labelMiniBio = tk.Label(infoFrame, text="MiniBio: " + candidato[3])
        labelMiniBio.grid(column=0, row=2)

        labelEntrevista = tk.Label(infoFrame, text="Nota da Entrevista: " + str(candidato[4]))
        labelEntrevista.grid(column=0, row=3)

        labelTeorico = tk.Label(infoFrame, text="Nota da Teorico: " + str(candidato[5]))
        labelTeorico.grid(column=0, row=4)

        labelPratico = tk.Label(infoFrame, text="Nota da Pratico: " + str(candidato[6]))
        labelPratico.grid(column=0, row=5)

        labelSoftSkill = tk.Label(infoFrame, text="Nota da SoftSkill: " + str(candidato[7]))
        labelSoftSkill.grid(column=0, row=6)

        candidatosFrame.append(infoFrame)

    
    for candidatoFrame in candidatosFrame:
        candidatoFrame.pack(pady=20)
        