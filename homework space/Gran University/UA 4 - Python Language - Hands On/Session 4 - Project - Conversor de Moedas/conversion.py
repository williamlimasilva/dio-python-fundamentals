import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Session 5 - Project - Gráficos de cotação de moedas'))
from currency import get_convertion

def main():
    print("=== Conversor de Moedas ===")
    moedas = {
        "1": "BRL",
        "2": "USD",
        "3": "EUR",
        "4": "GBP",
        "5": "JPY",
        "6": "AUD",
        "7": "CAD",
        "8": "CHF",
        "9": "CNY"
    }
    while True:
        print("Selecione a moeda de origem:")
        for k, v in moedas.items():
            print(f"{k} - {v}")
        escolha = input("Digite o número correspondente à moeda de origem: ")
        source = moedas.get(escolha)
        if not source:
            print("Opção inválida. Tente novamente.")
            continue
        try:
            amount = float(input(f"Digite o valor em {source}: "))
            rates = get_convertion(source)
            if rates is None:
                continue
            print("Mostrando cotações para USD, EUR e GBP:")
            for target in ["USD", "EUR", "GBP","BRL"]:
                if target in rates:
                    result = amount * rates[target]
                    print(f"{amount} {source} = {result:.2f} {target}")
                else:
                    print(f"Taxa de conversão para {target} não disponível")
        except ValueError:
            print("Valor inválido. Tente novamente.")
        again = input("Deseja fazer outra cotação? S/N: ").lower()
        if again != 's':
            print("Encerrando o conversor.")
            break

if __name__ == "__main__":
    main()
