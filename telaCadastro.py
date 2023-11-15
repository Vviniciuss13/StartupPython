
import bd
import tkinter as tk
from classes import Candidato

### INSERIR

def abrirCadastro():
    janelaInserir = tk.Toplevel()
    janelaInserir.geometry("850x500")
    janelaInserir.configure(background="#7EACB2")

    title = tk.Label(janelaInserir, text="Startup: Cadastrar Usuário", bg="#7EACB2", fg="#fff", font=("", 25))
    title.pack(pady=10)

    instrucoes = tk.Label(janelaInserir, text="Informações: ", bg="#7EACB2", fg="#fff", font=("", 20))
    instrucoes.pack(pady=10)

    frame = tk.Frame(janelaInserir, bg="#7EACB2")

    # Labels
    nomeLabel = tk.Label(frame, text="Nome: ", bg="#7EACB2", fg='#fff', font=("", 12))
    nomeLabel.grid(column=0, row=2)

    telefoneLabel = tk.Label(frame, text="Telefone: ", bg="#7EACB2", fg='#fff', font=("", 12))
    telefoneLabel.grid(column=1, row=2)

    minibioLabel = tk.Label(frame, text="MiniBio: ", bg="#7EACB2", fg='#fff', font=("", 12))
    minibioLabel.grid(column=2, row=2)

    entrevistaLabel = tk.Label(frame, text="Nota da Entrevista: ", bg="#7EACB2", fg='#fff', font=("", 12))
    entrevistaLabel.grid(column=3, row=2, pady=15)

    teoricoLabel = tk.Label(frame, text="Nota da prova teorica: ", bg="#7EACB2", fg='#fff', font=("", 12))
    teoricoLabel.grid(column=0, row=4, pady=10)

    praticoLabel = tk.Label(frame, text="Nota da prova pratica: ", bg="#7EACB2", fg='#fff', font=("", 12))
    praticoLabel.grid(column=1, row=4, pady=10)

    softSkillLabel = tk.Label(frame, text="Nota sobre a SoftSkill: ", bg="#7EACB2", fg='#fff', font=("", 12))
    softSkillLabel.grid(column=2, row=4, pady=10)

    # INPUTS
    nomeEntry = tk.Entry(frame)
    nomeEntry.grid(column=0, row=3, padx=10, ipady=5, pady=10)

    telefoneEntry = tk.Entry(frame)
    telefoneEntry.grid(column=1, row=3, padx=10, ipady=5, pady=10)

    minibioEntry = tk.Entry(frame)
    minibioEntry.grid(column=2, row=3, padx=10, ipady=5, pady=10)

    entrevistaEntry = tk.Entry(frame)
    entrevistaEntry.grid(column=3, row=3, padx=10, ipady=5, pady=10)

    teoricoEntry = tk.Entry(frame)
    teoricoEntry.grid(column=0, row=5, padx=10, ipady=5, pady=10)

    praticoEntry = tk.Entry(frame)
    praticoEntry.grid(column=1, row=5, padx=10, ipady=5, pady=10)

    softSkillEntry = tk.Entry(frame)
    softSkillEntry.grid(column=2, row=5, padx=10, ipady=5, pady=10)

    buttonInserir = tk.Button(frame, text="Inserir Candidato", command=lambda: criarCandidato())
    buttonInserir.configure(bg='#2A3D7E', fg='#fff', border=0)
    buttonInserir.grid(column=3, row=5, padx=10, ipadx=20, ipady=15)

    frame.pack()

    def criarCandidato():
        candidato = Candidato(nomeEntry.get(), telefoneEntry.get(), minibioEntry.get())
        candidato.setEntrevista(entrevistaEntry.get())
        candidato.setTeorico(teoricoEntry.get())
        candidato.setPratico(praticoEntry.get())
        candidato.setSkill(softSkillEntry.get())

        if(bd.inserirCandidato(candidato)):
            messageSucesso()
        else: 
            aviso = tk.Toplevel()
            aviso.geometry = "200x300"
            aviso.configure(background="#7EACB2")
            avisoLabel = tk.Label(aviso, text="Campos vazios!", bg="#7EACB2", fg="#fff", font=("", 20))
            avisoLabel.pack(pady=10)
        
            buttonOk = tk.Button(aviso, text="Ok", command=aviso.destroy)
            buttonOk.configure(bg='#E63128', fg='#fff', border=0)
            buttonOk.pack(pady=10, ipadx=10, ipady=10)
            
            buttonOk.pack()

def messageSucesso():
    message = tk.Tk()
    message.geometry("200x100")
    message.configure(background="#7EACB2")
    
    labelSucesso = tk.Label(message, text="Usuario Cadastrado", bg="#7EACB2")
    labelSucesso.pack(pady=20)

    buttonOk = tk.Button(message, text='Ok', command=message.destroy)
    buttonOk.config(bg="#3D712A", fg='#fff', border=0)
    buttonOk.pack(pady=10, ipadx=10, ipady=10)
