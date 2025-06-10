from currency import get_convertion
import matplotlib.pyplot as plt

quotes = get_convertion("BRL")
if quotes is None:
    print("Erro ao obter cotações.")
    exit()

l_currencies = ["USD - Dollar", "EUR - Euro", "GBP - Libra"]
l_values = [1/quotes["USD"], 1/quotes["EUR"], 1/quotes["GBP"]]

def graph_bar():
    plt.figure(figsize=(10, 6))
    plt.bar(l_currencies, l_values, color=['blue', 'green', 'red'])
    plt.title("Cotações de Moedas em Relação ao Real (BRL)")
    plt.xlabel("Moedas")
    plt.ylabel("Valor em BRL")
    plt.xticks(rotation=45)
    plt.tight_layout()  
    plt.show()

def graph_pie():
    plt.figure(figsize=(8, 8))
    plt.pie(l_values, labels=l_currencies, autopct='%1.1f%%', startangle=140)
    plt.title("Cotações de Moedas em Relação ao Real (BRL)")
    plt.axis('equal')
    plt.show()

def graph_scatter():
    plt.figure(figsize=(10, 6))
    plt.scatter(l_currencies, l_values, color='purple', s=100)
    plt.title("Cotações de Moedas em Relação ao Real (BRL)")
    plt.xlabel("Moedas")
    plt.ylabel("Valor em BRL")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()