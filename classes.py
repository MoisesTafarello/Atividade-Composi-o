class Processador:
    def __init__(self, modelo, velocidade_ghz):
        self.__modelo = modelo
        self.__velocidade_ghz = velocidade_ghz

    def getModelo (self):
        return self.__modelo
    
    def getVelocidade_ghz (self):
        return self.__velocidade_ghz
    
    def __str__(self):
        return f" - Processador: {self.__modelo},\n - Velocidade: {self.__velocidade_ghz} GHZ"
    

class Memoria_Ram:
    def __init__(self, capacidade_gb, tipo):
        self.__capacidade_gb = capacidade_gb
        self.__tipo = tipo

    def getCapacidade_gb (self):
        return self.__capacidade_gb
    
    def getTipo (self):
        return self.__tipo
    
    def __str__(self):
        return f" - Memória Ram: {self.__capacidade_gb} GB,\n - Tipo: {self.__tipo}"

class Armazenamento:
    def __init__(self, tipo, capacidade_gb ):
        self.__tipo = tipo
        self.__capacidade_gb = capacidade_gb

    def getTipo (self):
        return self.__tipo
    
    def getCapacidade_gb (self):
        return self.__capacidade_gb
    
    def __str__(self):
        return f" - Armazernamento {self.__tipo},\n - Capacidade: {self.__capacidade_gb} GB"

class Computador:
    def __init__(self, marca, modelo, processador_modelo, processador_ghz, ram_capacidade, ram_tipo, armazenamento_tipo, armazenamento_capacidade):
        self.__marca = marca
        self.__modelo = modelo 
        self.__processador = Processador (processador_modelo, processador_ghz)
        self.__memoria_ram = Memoria_Ram (ram_capacidade, ram_tipo)
        self.__armazenamento = Armazenamento (armazenamento_tipo, armazenamento_capacidade) 

    def getMarca (self):
        return self.__marca
    
    def getModelo (self):
        return self.__modelo
    
    def getProcessador (self):
        return self.__processador
    
    def getMemoria_ram (self):
        return self.__memoria_ram
    
    def getArmazenamento (self):
        return self.__armazenamento
    
    def ligar (self):
        print (f"\n Ligando o Computador {self.getMarca ()} {self.getModelo ()}... ")
        print (self.getProcessador ())
        print (self.getMemoria_ram ())
        print (self.getArmazenamento ())
        return self

    def __str__ (self):
        return (f" - Computador: {self.__marca} {self.__modelo}\n"
                f"{self.__processador}\n"
                f"{self.__memoria_ram}"
                f"{self.__armazenamento}")
