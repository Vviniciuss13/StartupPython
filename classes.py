class Candidato():
    
    def __init__(self, nome, telefone, minibio):
        self.nome = nome
        self.telefone = telefone
        self.minibio = minibio
        self.__notaEntrevista = 0
        self.__notaTeorico = 0
        self.__notaPratico = 0
        self.__notaSoftSkill = 0
    
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

        
        