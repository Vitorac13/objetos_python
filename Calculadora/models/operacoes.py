class Entrada:
    def __init__(self, num1=1, num2=1):
        self.num1 = num1
        self.num2 = num2

class OperacoesBasicas:

    def __init__(self, entrada):
        self.entrada = entrada
    
    def soma(self):
        return self.entrada.num1 + self.entrada.num2
    
    def subtracao(self):
        return self.entrada.num1 - self.entrada.num2
    
    def multiplicacao(self):
        return self.entrada.num1 * self.entrada.num2
    
    def divisao(self):      
        if self.entrada.num2 != 0:
            return self.entrada.num1 / self.entrada.num2
        else:
            return "Erro: Divisão por zero não é permitida."
        
class OperacoesAvancadas:

    def __init__(self, entrada):
        self.entrada = entrada
    
    def potencia(self, expoente):
        return self.entrada.num1 ** expoente

class Calculadora:

    def __init__(self, entrada):
        self.basicas = OperacoesBasicas(entrada)
        self.avancadas = OperacoesAvancadas(entrada)