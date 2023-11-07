
import bd
import tkinter as tk
from classes import Candidato

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

    entrevistaLabel = tk.Label(frame, text="Nota da Entrevista: ")
    entrevistaLabel.grid(column=3, row=2, pady=15)

    teoricoLabel = tk.Label(frame, text="Nota da prova teorica: ")
    teoricoLabel.grid(column=0, row=4)

    praticoLabel = tk.Label(frame, text="Nota da prova pratica: ")
    praticoLabel.grid(column=1, row=4)

    softSkillLabel = tk.Label(frame, text="Nota sobre a SoftSkill: ")
    softSkillLabel.grid(column=2, row=4)

    # INPUTS
    nomeEntry = tk.Entry(frame)
    nomeEntry.insert(0, "")
    nomeEntry.grid(column=0, row=3, padx=10)

    telefoneEntry = tk.Entry(frame)
    telefoneEntry.insert(0, "")
    telefoneEntry.grid(column=1, row=3, padx=10)

    minibioEntry = tk.Entry(frame)
    minibioEntry.insert(0, "")
    minibioEntry.grid(column=2, row=3, padx=10)

    entrevistaEntry = tk.Entry(frame)
    entrevistaEntry.insert(0, "")
    entrevistaEntry.grid(column=3, row=3, padx=10)

    teoricoEntry = tk.Entry(frame)
    teoricoEntry.insert(0, "")
    teoricoEntry.grid(column=0, row=5, padx=10)

    praticoEntry = tk.Entry(frame)
    praticoEntry.insert(0, "")
    praticoEntry.grid(column=1, row=5, padx=10)

    softSkillEntry = tk.Entry(frame)
    softSkillEntry.insert(0, "")
    softSkillEntry.grid(column=2, row=5, padx=10)

    buttonInserir = tk.Button(frame, text="Inserir Candidato", command=lambda: criarCandidato())
    buttonInserir.grid(column=3, row=5, padx=10)

    def criarCandidato():
        candidato = Candidato(nomeEntry.get(), telefoneEntry.get(), minibioEntry.get())
        candidato.setEntrevista(entrevistaEntry.get())
        candidato.setTeorico(teoricoEntry.get())
        candidato.setPratico(praticoEntry.get())
        candidato.setSkill(softSkillEntry.get())

        bd.inserirCandidato(candidato)

        messageSucesso()

    def messageSucesso():
        message = tk.Tk()
        message.geometry("200x100")
        
        labelSucesso = tk.Label(message, text="Usuario Cadastrado")
        labelSucesso.pack(pady=20)

        buttonOk = tk.Button(message, text='Ok', command=message.destroy)
        buttonOk.pack(pady=10, ipadx=10, ipady=10)
        

    frame.pack()