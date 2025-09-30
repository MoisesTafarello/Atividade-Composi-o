# 💻 Exercício: Criação e Composição de Objetos

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

## 🔹 Descrição

Este projeto é um exercício em Python sobre **composição de objetos**, representando um **Computador** e seus componentes: Processador, Memória RAM e Armazenamento.  
O objetivo é aplicar conceitos de **POO**, **encapsulamento** e **composição**, mostrando como os componentes fazem parte do computador.

---

## 🏗️ Estrutura do Projeto

### **Classes**

#### `Processador`
- **Atributos:** `modelo`, `velocidade_ghz`
- **Métodos:** `getModelo()`, `getVelocidade_ghz()`
- **Descrição:** Representa o processador do computador.

#### `MemoriaRAM`
- **Atributos:** `capacidade_gb`, `tipo`
- **Métodos:** `getCapacidade_gb()`, `getTipo()`
- **Descrição:** Representa a memória RAM.

#### `Armazenamento`
- **Atributos:** `tipo`, `capacidade_gb`
- **Métodos:** `getTipo()`, `getCapacidade_gb()`
- **Descrição:** Representa o armazenamento (SSD/HDD).

#### `Computador`
- **Atributos:** `marca`, `modelo` e composição de `Processador`, `MemoriaRAM`, `Armazenamento`
- **Métodos:** `getMarca()`, `getModelo()`, `getProcessador()`, `getMemoria_ram()`, `getArmazenamento()`, `ligar()`
- **Descrição:** Representa o computador completo, com acesso aos componentes via métodos `get_`.

---

## ⚙️ Funcionalidades

- Encadeamento de métodos: `meu_computador.ligar()`
- Representação amigável com `__str__`
- Demonstração de composição: componentes fazem parte do computador

---

## 🧪 Exemplo de Uso

```python
from classes import *

meu_pc = Computador(
    marca="Asus",
    modelo="Rog Strix G16",
    processador_modelo="Ryzen 7 9800X3D",
    processador_ghz=5.2,
    ram_capacidade=64,
    ram_tipo="DDR5",
    armazenamento_tipo="SSD NVME",
    armazenamento_capacidade=2000
)

meu_pc.ligar()
print("\nRepresentação completa:")
print(meu_pc)
