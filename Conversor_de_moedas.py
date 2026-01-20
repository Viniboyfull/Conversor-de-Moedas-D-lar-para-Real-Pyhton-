import tkinter as tk
import requests

def converter():
    try:
        valor = float(entry_valor.get())
        resposta = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        taxa = resposta.json()["rates"]["BRL"]
        resultado = valor * taxa
        label_resultado.config(text=f"{valor} USD = {resultado:.2f} BRL")
    except:
        label_resultado.config(text="Erro na conversão")

# Janela principal
janela = tk.Tk()
janela.title("Conversor de Moedas")

tk.Label(janela, text="Valor em USD:").pack()
entry_valor = tk.Entry(janela)
entry_valor.pack()

btn_converter = tk.Button(janela, text="Converter", command=converter)
btn_converter.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()