import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para carregar o CSV
def carregar_csv():
    # Abrir uma caixa de diálogo para selecionar o arquivo CSV
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if caminho_arquivo:
        # Carregar o arquivo CSV usando pandas
        global df
        df = pd.read_csv(caminho_arquivo)
        
        # Atualizar o texto com o resumo dos dados
        resumo = df.describe().to_string()
        texto_resumo.config(state=tk.NORMAL)
        texto_resumo.delete(1.0, tk.END)
        texto_resumo.insert(tk.END, resumo)
        texto_resumo.config(state=tk.DISABLED)
        
        # Exibir gráfico de exemplo (caso tenha colunas numéricas)
        plotar_grafico()

# Função para plotar gráfico
def plotar_grafico():
    if df is not None:
        # Criar um gráfico simples usando Matplotlib
        fig, ax = plt.subplots(figsize=(5, 4))
        df.plot(kind='line', ax=ax)
        
        # Criar um canvas para o gráfico dentro da janela Tkinter
        canvas = FigureCanvasTkAgg(fig, master=janela)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=0, columnspan=2)

# Criar a janela principal
janela = tk.Tk()
janela.title("Dashboard Simples")

# Botão para carregar o CSV
botao_carregar = tk.Button(janela, text="Carregar CSV", command=carregar_csv)
botao_carregar.grid(row=0, column=0, pady=10, padx=10)

# Caixa de texto para exibir resumo dos dados
texto_resumo = tk.Text(janela, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED)
texto_resumo.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

# Inicializar a variável df como None
df = None

# Rodar a interface Tkinter
janela.mainloop()








