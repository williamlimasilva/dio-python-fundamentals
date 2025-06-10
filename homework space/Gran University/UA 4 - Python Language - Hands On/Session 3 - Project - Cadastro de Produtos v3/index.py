from classes.Product import Product

def menu():
    print("=== Menu ===")
    print("1. Listar Produtos")
    print("2. Adicionar Produto")
    print("3. Atualizar Produto")
    print("4. Excluir Produto")
    print("0. Sair")

option = 1

while option != 0: 
    menu()
    option = int(input("Escolha uma opção: "))
    match option:
        case 1:
            Product.list()
        case 2:
            code = input("Digite o código do produto: ")
            name = input("Digite o nome do produto: ")
            price = float(input("Digite o preço do produto: "))
            quantity = int(input("Digite a quantidade do produto: "))
            product = Product(code, name, price, quantity)
            product.create()
        case 3:
            Product.list()
            item_code = int(input("Digite o índice do produto a atualizar: "))
            code = input("Digite o novo código do produto: ")
            name = input("Digite o novo nome do produto: ")
            price = float(input("Digite o novo preço do produto: "))
            quantity = int(input("Digite a nova quantidade do produto: "))
            product = Product(code, name, price, quantity)
            product.update(item_code)
        case 4:
            Product.list()
            item_code = int(input("Digite o índice do produto a excluir: "))
            Product.delete(item_code)
        case 0:
            print("Saindo...")
        case _:
            print("Opção inválida!")


