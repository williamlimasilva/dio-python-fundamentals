import graphs

def menu():
    while True:
        print("\nMenu:")
        print("1. Gráfico de Barras")
        print("2. Gráfico de Pizza")
        print("3. Gráfico de Dispersão")
        print("0. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            graphs.graph_bar()
        elif choice == "2":
            graphs.graph_pie()
        elif choice == "3":
            graphs.graph_scatter()
        elif choice == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    print("Bem-vindo ao Visualizador de Cotações de Moedas!")
    menu()