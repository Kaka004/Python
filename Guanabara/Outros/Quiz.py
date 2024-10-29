import tkinter as tk
from tkinter import messagebox
import random

# Defina uma lista de perguntas e respostas
perguntas = {
    "Qual é a capital do Brasil?": "Brasília",
    "Quem escreveu 'Dom Quixote'?": "Miguel de Cervantes",
    "Quantos planetas existem em nosso sistema solar?": "Oito"
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Quiz")
        
        self.pergunta_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.pergunta_label.pack(pady=10)
        
        self.resposta_entry = tk.Entry(root, font=("Helvetica", 12))
        self.resposta_entry.pack(pady=5)
        
        self.botao_responder = tk.Button(root, text="Responder", command=self.responder)
        self.botao_responder.pack(pady=5)
        
        self.pontuacao_label = tk.Label(root, text="Pontuação: 0")
        self.pontuacao_label.pack(pady=10)
        
        self.pontuacao = 0
        self.total_perguntas = len(perguntas)
        self.pergunta_atual = None
        
        self.proxima_pergunta()

    def proxima_pergunta(self):
        self.pergunta_atual, self.resposta_correta = random.choice(list(perguntas.items()))
        self.pergunta_label.config(text=self.pergunta_atual)
        self.resposta_entry.delete(0, tk.END)
    
    def responder(self):
        resposta_jogador = self.resposta_entry.get().strip().capitalize()
        if resposta_jogador == self.resposta_correta:
            self.pontuacao += 1
            messagebox.showinfo("Resposta", "Correto!")
        else:
            messagebox.showerror("Resposta", f"Incorreto. A resposta correta é: {self.resposta_correta}")
        self.atualizar_pontuacao()
        if self.pontuacao < self.total_perguntas:
            self.proxima_pergunta()
        else:
            messagebox.showinfo("Fim do jogo", f"Jogo concluído! Sua pontuação final é: {self.pontuacao}/{self.total_perguntas}")
            self.root.destroy()
    
    def atualizar_pontuacao(self):
        self.pontuacao_label.config(text=f"Pontuação: {self.pontuacao}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
