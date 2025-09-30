from classes import *

meu_pc = Computador(
    marca = "Asus",
    modelo = "Rog Strix G16",
    processador_modelo = "Ryzen 7 9800X3D",
    processador_ghz = 5.2,
    ram_capacidade = 64,
    ram_tipo = "DDR5",
    armazenamento_tipo = "SSD NVME",
    armazenamento_capacidade = 2000
)

meu_pc.ligar()
print("\nRepresentação completa:")
print(meu_pc)

del meu_pc
