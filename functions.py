import db.bd as bd
from classes import Candidato
import tkinter as tk
from reportlab.pdfgen.canvas import Canvas

#WINDOW MENSSAGENS
def messageSucesso():
    message = tk.Tk()
    message.geometry("200x100")
    message.configure(background="#7EACB2")
    
    labelSucesso = tk.Label(message, text="Usuario Cadastrado", bg="#7EACB2")
    labelSucesso.pack(pady=20)

    buttonOk = tk.Button(message, text='Ok', command=message.destroy)
    buttonOk.config(bg="#3D712A", fg='#fff', border=0)
    buttonOk.pack(pady=10, ipadx=10, ipady=10)

def messageFalha():
    aviso = tk.Toplevel()
    aviso.geometry = "200x300"
    aviso.configure(background="#7EACB2")
    avisoLabel = tk.Label(aviso, text="Campos vazios!", bg="#7EACB2", fg="#fff", font=("", 20))
    avisoLabel.pack(pady=10)

    buttonOk = tk.Button(aviso, text="Ok", command=aviso.destroy)
    buttonOk.configure(bg='#E63128', fg='#fff', border=0)
    buttonOk.pack(pady=10, ipadx=10, ipady=10)
        
    buttonOk.pack() 

#PEGAR INFORMAÇÔES
def getInfo(nome, telefone, minibio, entrevista, teorico, pratico, softSkill, control):
    info = []
    if control == 'notes':
        info.append(entrevista.get())
        info.append(teorico.get())
        info.append(pratico.get())
        info.append(softSkill.get())
    else:
        info.append(nome.get())
        info.append(telefone.get())
        info.append(minibio.get())
        info.append(entrevista.get())
        info.append(teorico.get())
        info.append(pratico.get())
        info.append(softSkill.get())
    
    return info
    
# CADASTRAR FUNCTION
def criarCandidato(info):
    candidato = Candidato(info[0], info[1], info[2])
    candidato.setEntrevista(info[3])
    candidato.setTeorico(info[4])
    candidato.setPratico(info[5])
    candidato.setSkill(info[6])

    if(bd.inserirCandidato(candidato)):
        messageSucesso()
    else:
        messageFalha() 
        
#PDFS FUNCTIONS        

def gerarPdfInfo(candidatos):
    x = 750
    y = 100
    canvas = Canvas("pdfs/candidatospesquisados.pdf")
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
    canvas = Canvas("pdfs/candidatospesquisadosbasico.pdf")
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
    canvas = Canvas("pdfs/candidatosinformacoes.pdf")
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
    canvas = Canvas("pdfs/candidatosbasico.pdf")
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