class Candidato():
    
    def __init__(self, nome, telefone, minibio, entrevista, teorico, pratico, softskill):
        self.nome = nome
        self.telefone = telefone
        self.minibio = minibio
        self.__notaEntrevista = entrevista
        self.__notaTeorico = teorico
        self.__notaPratico = pratico
        self.__notaSoftSkill = softskill
    
    def getEntrevista(self):
        return self.__notaEntrevista
    
    def setEntrevista(self, valor):
        self.__notaEntrevista = valor
        
    def getTeorico(self):
        return self.__notaTeorico
    
    def setTeorico(self, valor):
        self.__notaTeorico = valor

    def getPratico(self):
        return self.__notaPratico
    
    def setPratico(self, valor):
        self.__notaPratico = valor
    
    def getSkill(self):
        return self.__notaSoftSkill
    
    def setSkill(self, valor):
        self.__notaSoftSkill = valor

        
        