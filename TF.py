# Função para adicionar produto ao inventário
def adicionar_produto(inventario, nome, preco, quantidade):
    inventario[nome] = {'preco': preco, 'quantidade': quantidade}

# Função para remover produto do inventário
def remover_produto(inventario, nome):
    if nome in inventario:
        del inventario[nome]
    else:
        print("Produto não encontrado no inventário.")

# Função para listar todos os produtos no inventário
def listar_produtos(inventario):
    if inventario:
        for nome, info in inventario.items():
            print(f"Produto: {nome}, Preço: {info['preco']}, Quantidade: {info['quantidade']}")
    else:
        print("Inventário vazio.")

# Função principal para interagir com o usuário
def main():
    inventario = {}
    while True:
        print("\nMenu de Inventário:")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            adicionar_produto(inventario, nome, preco, quantidade)
        elif escolha == '2':
            nome = input("Nome do produto: ")
            remover_produto(inventario, nome)
        elif escolha == '3':
            listar_produtos(inventario)
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()