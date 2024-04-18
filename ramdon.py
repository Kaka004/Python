import random
import tkinter as tk
from tkinter import messagebox

class NumeroRandomico:
    def __init__(self):
        self.gerar_novo_numero()

    def gerar_novo_numero(self):
        self.novo_numero = random.randint(1, 100)

    def adivinhar_numero(self, tentativa):
        if tentativa == self.novo_numero:
            self.gerar_novo_numero()
            return "Parabéns! Você acertou o número secreto! Um novo número foi gerado."
        elif tentativa < self.novo_numero:
            return "O número secreto é maior."
        else:
            return "O número secreto é menor."

def fazer_tentativa(event=None):
    try:
        tentativa = int(entrada.get())
        resultado = jogo.adivinhar_numero(tentativa)
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")
    

# Criar janela
janela = tk.Tk()
janela.title("Número Randômico")

# Criar instância do jogo
jogo = JogoAleatorio()

# Criar widgets
label = tk.Label(janela, text="Adivinhe o número (entre 1 e 100):")
label.pack()

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Tentar", command=fazer_tentativa)
botao.pack()

entrada.bind("<Return>", fazer_tentativa)

# Executar interface gráfica
janela.mainloop()
