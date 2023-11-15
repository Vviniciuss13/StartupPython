import bd
import tkinter as tk
from classes import Candidato
from reportlab.pdfgen.canvas import Canvas

def gerarPdfInfo(candidatos):
    x = 750
    y = 100
    canvas = Canvas("candidatospesquisados.pdf")
    canvas.drawString(200, 800, "Feito por Carlos Vinícius - Candidatos Filtrados - Todas as Informações")
    for candidato in candidatos:
        canvas.drawString(y, x, "ID: " + str(candidato[0]))
        canvas.drawString(y, (x-10), "Nome: " + candidato[1])
        canvas.drawString(y, (x-20), "Telefone: " + candidato[2])
        canvas.drawString(y, (x-30), "MiniBio: " + candidato[3])
        canvas.drawString(y, (x-40), "Nota de Entrevista: " + str(candidato[4]))
        canvas.drawString(y, (x-50), "Nota prova teorica: " + str(candidato[5]))
        canvas.drawString(y, (x-60), "Nota prova pratica: " + str(candidato[6]))
        canvas.drawString(y, (x-70), "Nota de SoftSkill: " + str(candidato[7]))
        x = x - 120
        
        if(x < 100 and y > 100):
            canvas.showPage()
            x = 750
            y = 100
        
        if(x < 100):
            y = 300
            x = 750
    canvas.save()
    
def gerarPdf(candidatos):
    x = 750
    y = 100
    canvas = Canvas("candidatospesquisadosbasico.pdf")
    canvas.drawString(200, 800, "Feito por Carlos Vinícius - Candidatos Filtrados - Informações Básicas")
    for candidato in candidatos:
        canvas.drawString(y, (x-10), "Nome: " + candidato[1])
        canvas.drawString(y, (x-20), "Nota de Entrevista: " + str(candidato[4]))
        canvas.drawString(y, (x-30), "Nota prova teorica: " + str(candidato[5]))
        canvas.drawString(y, (x-40), "Nota prova pratica: " + str(candidato[6]))
        canvas.drawString(y, (x-50), "Nota de SoftSkill: " + str(candidato[7]))
        x = x - 90
        
        if(x < 100 and y > 100):
            canvas.showPage()
            x = 750
            y = 100
        
        if(x < 100):
            y = 300
            x = 750
    canvas.save()

def gerarPdfTodosInfo(candidatos):
    x = 750
    y = 100
    canvas = Canvas("candidatosinformacoes.pdf")
    canvas.drawString(200, 800, "Feito por Carlos Vinícius - Todos os Candidatos - Todas informações")
    for candidato in candidatos:
        canvas.drawString(y, x, "ID: " + str(candidato[0]))
        canvas.drawString(y, (x-10), "Nome: " + candidato[1])
        canvas.drawString(y, (x-20), "Telefone: " + candidato[2])
        canvas.drawString(y, (x-30), "MiniBio: " + candidato[3])
        canvas.drawString(y, (x-40), "Nota de Entrevista: " + str(candidato[4]))
        canvas.drawString(y, (x-50), "Nota prova teorica: " + str(candidato[5]))
        canvas.drawString(y, (x-60), "Nota prova pratica: " + str(candidato[6]))
        canvas.drawString(y, (x-70), "Nota de SoftSkill: " + str(candidato[7]))
        x = x - 120
        
        if(x < 100 and y > 100):
            canvas.showPage()
            x = 750
            y = 100
        
        if(x < 100):
            y = 300
            x = 750
    canvas.save()
    
def gerarPdfTodos(candidatos):
    x = 750
    y = 100
    canvas = Canvas("candidatosbasico.pdf")
    canvas.drawString(200, 800, "Feito por Carlos Vinícius - Todos os Candidatos - Informações Basicas")
    for candidato in candidatos:
        canvas.drawString(y, (x-10), "Nome: " + candidato[1])
        canvas.drawString(y, (x-20), "Nota de Entrevista: " + str(candidato[4]))
        canvas.drawString(y, (x-30), "Nota prova teorica: " + str(candidato[5]))
        canvas.drawString(y, (x-40), "Nota prova pratica: " + str(candidato[6]))
        canvas.drawString(y, (x-50), "Nota de SoftSkill: " + str(candidato[7]))
        x = x - 90
        
        if(x < 100 and y > 100):
            canvas.showPage()
            x = 750
            y = 100
        
        if(x < 100):
            y = 300
            x = 750
    canvas.save()

### PESQUISA ######
def abrirPesquisa():
    janelaPesquisa = tk.Tk()
    janelaPesquisa.geometry("850x500")
    janelaPesquisa.configure(background="#7EACB2")

    def enterPesquisar(o):
        buttonPesquisar['background'] = "#1D2A57"

    def outPesquisar(o):
        buttonPesquisar['background'] = "#2A3D7E"

    title = tk.Label(janelaPesquisa, text="Startup: Escolha dos Candidatos", bg="#7EACB2", fg="#fff", font=("", 25))
    title.pack()

    instrucao = tk.Label(janelaPesquisa, text="Escolha os Requisitos:", bg="#7EACB2", fg="#fff", font=("", 20))
    instrucao.pack()

    frame = tk.Frame(janelaPesquisa, bg="#7EACB2")

    # Labels
    entrevistaLabel = tk.Label(frame, text="Nota Mínima da Entrevista: ", bg="#7EACB2", fg="#fff", font=("", 10))
    entrevistaLabel.grid(column=0, row=2, pady=15)

    teoricoLabel = tk.Label(frame, text="Nota Mínima da prova teorica: ", bg="#7EACB2", fg="#fff", font=("", 10))
    teoricoLabel.grid(column=2, row=2)

    praticoLabel = tk.Label(frame, text="Nota Mínima da prova pratica: ", bg="#7EACB2", fg="#fff", font=("", 10))
    praticoLabel.grid(column=0, row=4)

    softSkillLabel = tk.Label(frame, text="Nota Mínima sobre a SoftSkill: ", bg="#7EACB2", fg="#fff", font=("", 10))
    softSkillLabel.grid(column=2, row=4)

    # INPUTS
    entrevistaEntry = tk.Entry(frame)
    entrevistaEntry.insert(0, "0")
    entrevistaEntry.grid(column=0, row=3, padx=10, ipady=5)

    teoricoEntry = tk.Entry(frame)
    teoricoEntry.insert(0, "0")
    teoricoEntry.grid(column=2, row=3, padx=10, ipady=5)

    praticoEntry = tk.Entry(frame)
    praticoEntry.insert(0, "0")
    praticoEntry.grid(column=0, row=5, padx=10, ipady=5)

    softSkillEntry = tk.Entry(frame)
    softSkillEntry.insert(0, "0")
    softSkillEntry.grid(column=2, row=5, padx=10, ipady=5)

    # BUTTON 
    buttonPesquisar = tk.Button(janelaPesquisa, text="Pesquisar Candidato", command=lambda: pesquisar(entrevistaEntry.get(), teoricoEntry.get(), praticoEntry.get(), softSkillEntry.get()))
    buttonPesquisar.configure(bg='#2A3D7E', fg='#fff', border=0)
    
    frame.pack()
    
    buttonPesquisar.pack(pady=20, ipadx=10, ipady=10) 
    buttonPesquisar.bind("<Enter>", enterPesquisar)
    buttonPesquisar.bind("<Leave>", outPesquisar)


def pesquisar(entrevista, teorico, pratico, softSkill):
    notas = [entrevista, teorico, pratico, softSkill]

    mostrarResultados(notas)

def mostrarResultados(notas):
    janelaResultados = tk.Tk()
    janelaResultados.geometry("850x600")
    janelaResultados.config(bg="#7EACB2")

    scrollbar = tk.Scrollbar(janelaResultados)
    scrollbar.pack(side="right", fill="y")

    listCandidatos = tk.Listbox(janelaResultados, yscrollcommand=scrollbar.set, bg="#5EACB2", border=0, fg="#fff", font=("", 20, ""))

    allCandidatos = bd.exibirTodos()

    candidatos = bd.pesquisarCandidato(notas[0], notas[1], notas[2], notas[3])
    for candidato in candidatos:

        listCandidatos.insert("end", "ID: " + str(candidato[0]))
        listCandidatos.insert("end", "Nome: " + candidato[1])
        listCandidatos.insert("end", "Telefone: " + candidato[2])
        listCandidatos.insert("end", "MiniBio: " + candidato[3])
        listCandidatos.insert("end", "Nota da Entrevista: " + str(candidato[4]))
        listCandidatos.insert("end", "Nota da Prova Teorica: " + str(candidato[5]))
        listCandidatos.insert("end", "Nota da Prova Pratica: " + str(candidato[6]))
        listCandidatos.insert("end", "Nota de SoftSkill: " + str(candidato[7]))
        listCandidatos.insert("end", "-------------------------------")

    listCandidatos.pack(side="top", pady=15, ipady=15, ipadx=50)
    
    scrollbar.config(command=listCandidatos.yview)

    framePdf = tk.Frame(janelaResultados, bg="#7EACB2")

    buttonPdfAll = tk.Button(framePdf, text="gerar pdf com informações basicas de todos os Candidatos", command=lambda: gerarPdfTodos(allCandidatos))
    buttonPdfAll.configure(bg='#2A3D7E', fg='#fff', border=0)
    buttonPdfAll.grid(column="0", row="0", padx=20, pady=10, ipadx=20, ipady=20)
    
    buttonPdfAllInfo = tk.Button(framePdf, text="gerar pdf com todas informações de todos os Candidatos", command=lambda: gerarPdfTodosInfo(allCandidatos))
    buttonPdfAllInfo.configure(bg='#2A3D7E', fg='#fff', border=0)
    buttonPdfAllInfo.grid(column="1", row="0", padx=20, pady=10, ipadx=20, ipady=20)

    buttonPdf = tk.Button(framePdf, text="gerar pdf com informações basicas dos candidatos pesquisados", command=lambda: gerarPdf(candidatos))
    buttonPdf.configure(bg='#CF9A32', fg='#fff', border=0)
    buttonPdf.grid(column="0", row="1", padx=20, pady=10, ipadx=20, ipady=20)
    
    buttonPdfInfo = tk.Button(framePdf, text="gerar pdf com todas as informações dos candidatos pesquisados", command=lambda: gerarPdfInfo(candidatos))
    buttonPdfInfo.configure(bg='#CF9A32', fg='#fff', border=0)
    buttonPdfInfo.grid(column="1", row="1", padx=20, pady=10, ipadx=20, ipady=20)

    framePdf.pack()