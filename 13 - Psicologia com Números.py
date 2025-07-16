import tkinter as tk
from tkinter import messagebox
import random

class AnaliseNumericaApp:
    """
    Classe principal do aplicativo de Análise Numérica.
    Permite inserir vários números e, ao final, apresenta
    estatísticas e interpretações que envolve a escolha dos
    números com a personalidade da pessoa. Totalmente aleatório,
    sem nenhum fundamento científico.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Análise de Números")
        self.root.geometry("600x500")
        self.numeros = []  # Lista para armazenar os números inseridos

        # Instruções iniciais ao usuário
        instrucoes = (
            "Digite quantos números quiser. Os que vierem à sua cabeça.\n"
            "Pode usar vírgula ou ponto. Números negativos também são aceitos.\n"
            "Não existe número bom ou ruim.\n"
            "Ao final, vamos descobrir o que os números dizem sobre você hoje!"
        )
        self.label_instrucao = tk.Label(
            root,
            text=instrucoes,
            font=("Arial", 12),
            justify="left",
            wraplength=580
        )
        self.label_instrucao.pack(pady=15)

        # Campo de entrada de número
        self.entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.entry.pack(pady=5)

        # Botão para inserir o número na lista
        self.inserir_btn = tk.Button(
            root, text="Inserir Número",
            command=self.inserir_numero,
            width=20
        )
        self.inserir_btn.pack(pady=5)

        # Título da lista de números inseridos
        self.label_lista = tk.Label(
            root,
            text="Números inseridos:",
            font=("Arial", 12)
        )
        self.label_lista.pack(pady=(20, 5))

        # Exibição dos números já inseridos
        self.lista_texto = tk.Label(
            root,
            text="",
            font=("Arial", 12),
            fg="blue"
        )
        self.lista_texto.pack()

        # Botão para finalizar e analisar os números
        self.finalizar_btn = tk.Button(
            root,
            text="FINALIZAR ANÁLISE",
            command=self.analisar,
            bg="green",
            fg="white",
            font=("Arial", 14),
            width=30,
            height=2
        )
        self.finalizar_btn.pack(pady=30)

    def inserir_numero(self):
        """
        Tenta converter o valor digitado para número.
        Aceita ponto ou vírgula. Adiciona à lista se for válido.
        """
        entrada = self.entry.get().replace(",", ".").strip()
        if entrada == "":
            return  # Ignora entrada vazia
        try:
            num = float(entrada)
            self.numeros.append(num)
            self.entry.delete(0, tk.END)
            self.atualizar_lista()
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido (ex: 7.5, -3, 4,2)")

    def atualizar_lista(self):
        """
        Atualiza a exibição da lista de números já inseridos.
        """
        texto = ", ".join(str(n) for n in self.numeros)
        self.lista_texto.config(text=texto)

    def analisar(self):
        """
        Analisa os números inseridos: estatísticas matemáticas e
        interpretações simbólicas, como se fossem traços de personalidade.
        """
        if len(self.numeros) == 0:
            messagebox.showinfo("Aviso", "Nenhum número foi inserido.")
            return

        nums = self.numeros
        maior = max(nums)
        menor = min(nums)
        media = sum(nums) / len(nums)
        pares = [n for n in nums if n % 2 == 0]
        impares = [n for n in nums if n % 2 != 0]

        # Mostra as estatísticas básicas
        resultado = (
            f"Números inseridos: {nums}\n"
            f"Quantidade: {len(nums)}\n"
            f"Maior número: {maior}\n"
            f"Menor número: {menor}\n"
            f"Média: {media:.2f}\n"
            f"Soma total: {sum(nums):.2f}\n"
            f"Números pares: {pares}\n"
            f"Números ímpares: {impares}"
        )
        messagebox.showinfo("Resultado da Análise", resultado)

        # A seguir, uma interpretação simbólica e "psicológica"
        teorias = []

        # Cada linha abaixo adiciona uma "interpretação" com base nos números
        teorias.append(media > 50 and "Média alta indica personalidade ambiciosa.") or teorias.append("Média baixa sugere foco em metas realistas.")
        teorias.append(len(nums) <= 5 and "Poucos números sugerem perfil reservado.") or teorias.append("Muitos números sugerem mente expansiva.")
        teorias.append(len(pares) > len(impares) and "Preferência por pares indica busca por equilíbrio.") or teorias.append("Mais ímpares sugerem pensamento fora do convencional.")
        teorias.append(maior > 100 and "Inserir valores altos revela otimismo elevado.") or teorias.append("Ausência de valores altos pode indicar contenção emocional.")
        teorias.append(menor < 0 and "Números negativos indicam traços de pessimismo.") or teorias.append("Nenhum número negativo sugere positividade constante.")
        teorias.append(media % 2 == 0 and "Média par indica tendência a padrões organizados.") or teorias.append("Média ímpar revela criatividade espontânea.")
        teorias.append(len(nums) > 20 and "Grande volume de dados indica compulsão por controle.") or teorias.append("Poucos dados sugerem desapego ao controle.")
        teorias.append(len(set(nums)) == 1 and "Repetição total sugere personalidade obsessiva.") or teorias.append("Diversidade nos dados mostra mente aberta.")
        teorias.append(all(n >= 0 for n in nums) and "A ausência de negativos sugere otimismo comportamental.") or teorias.append("Presença de negativos indica introspecção.")
        teorias.append(any(n > 1000 for n in nums) and "Valores extremos podem indicar impulsividade.") or teorias.append("Ausência de extremos revela racionalidade.")
        teorias.append(len(impares) == 0 and "Nenhum ímpar pode indicar desejo por simetria.") or teorias.append("A presença de ímpares mostra flexibilidade.")
        teorias.append(len(pares) == 0 and "Sem números pares pode indicar rebeldia.") or teorias.append("A presença de pares mostra conformismo social.")
        teorias.append(maior - menor > 500 and "Grande variação numérica sugere oscilações emocionais.") or teorias.append("Pequena variação indica estabilidade.")
        teorias.append(nums.count(0) > 0 and "Inserir zero pode indicar estagnação momentânea.") or teorias.append("Ausência de zero reflete movimento constante.")
        teorias.append(sum(nums) < 0 and "Soma negativa sugere tendência à introspecção.") or teorias.append("Soma positiva reflete orientação para fora.")
        teorias.append(media > 100 and "Média altíssima sugere idealismo.") or teorias.append("Média moderada reflete pé no chão.")
        teorias.append(all(n % 1 == 0 for n in nums) and "Todos inteiros indicam racionalidade.") or teorias.append("Presença de decimais revela nuances emocionais.")
        teorias.append(nums == sorted(nums) and "Inserção crescente mostra pensamento progressivo.") or teorias.append("Ordem aleatória indica mente caótica.")
        teorias.append(nums == sorted(nums, reverse=True) and "Inserção decrescente mostra apego ao passado.") or teorias.append("Sequência variada mostra foco no presente.")
        teorias.append(len([n for n in nums if 0 < n < 10]) > 5 and "Muitos números pequenos indicam atenção aos detalhes.") or teorias.append("Poucos valores pequenos indicam visão macro.")

        # Seleciona 5 teorias aleatórias entre as geradas
        teorias_finais = random.sample([t for t in teorias if isinstance(t, str)], 5)

        # Exibe as interpretações selecionadas
        interpretacao = "\n".join(f"- {t}" for t in teorias_finais)
        messagebox.showinfo("Interpretação Psicológica", interpretacao)

        # Reseta os dados para nova rodada
        self.numeros = []
        self.lista_texto.config(text="")

# ===============================
# INÍCIO DO PROGRAMA (mainloop)
# ===============================
if __name__ == "__main__":
    root = tk.Tk()
    app = AnaliseNumericaApp(root)
    root.mainloop()
