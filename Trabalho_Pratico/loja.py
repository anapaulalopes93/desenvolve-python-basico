import os
import csv

def ler_usuarios():
    usuarios = []
    if os.path.exists('usuarios.csv') and os.path.getsize('usuarios.csv') > 0:
        with open('usuarios.csv', 'r') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # Pular a linha de cabeçalho
            for linha in leitor:
                if len(linha) == 5:
                    try:
                        usuario = {
                            'id': int(linha[0]),
                            'nome': linha[1],
                            'senha': linha[2],
                            'tipo': linha[3],
                            'permissao': linha[4]
                        }
                        usuarios.append(usuario)
                    except ValueError:
                        print(f"Erro ao ler linha: {linha}")
                else:
                    print(f"Linha inválida: {linha}")
    return usuarios

def criar_usuario():
    id_usuario = int(input("Digite o ID do usuário: "))
    nome_usuario = input("Digite o nome do usuário: ")
    senha_usuario = input("Digite a senha do usuário: ")
    tipo_usuario = input("Digite o tipo do usuário (Gerente ou Funcionário): ")
    permissao_usuario = input("Digite a permissão do usuário: ")
    with open('usuarios.csv', 'a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([id_usuario, nome_usuario, senha_usuario, tipo_usuario, permissao_usuario])
        arquivo.write("\n")  # Adiciona uma quebra de linha ao final da linha

def remover_usuario():
    id_usuario = int(input("Digite o ID do usuário a ser removido: "))
    usuarios = ler_usuarios()
    with open('usuarios.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["ID", "Nome", "Senha", "Tipo", "Permissão"])  # Cabeçalho
        for usuario in usuarios:
            if usuario['id']!= id_usuario:
                escritor.writerow([usuario['id'], usuario['nome'], usuario['senha'], usuario['tipo'], usuario['permissao']])

def listar_usuarios():
    usuarios = ler_usuarios()
    for usuario in usuarios:
        print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Tipo: {usuario['tipo']}, Permissão: {usuario['permissao']}")

def ler_produtos():
    produtos = []
    with open('produtos.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Pular a linha de cabeçalho
        for linha in leitor:
            if linha:  # Ignorar linhas vazias
                produtos.append(linha)
    print("Produtos cadastrados:")
    for linha in produtos:
        if len(linha) >= 3:
            print(f"ID: {linha[0]}, Nome: {linha[1]}, Preço: {linha[2]}")
        else:
            print(f"Linha inválida: {linha}")
    return produtos  # Retorna a lista de produtos

def criar_produto():
    id_produto = int(input("Digite o ID do produto: "))
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    with open('produtos.csv', 'a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([id_produto, nome_produto, preco_produto])
        arquivo.write("\n")
    print("Produto criado com sucesso!")

def atualizar_produto():
    id_produto = input("Digite o ID do produto que deseja atualizar: ")
    with open('produtos.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        produtos = [linha for linha in leitor]
    for linha in produtos:
        if linha[0] == id_produto:
            nome_produto = input("Digite o novo nome do produto: ")
            preco_produto = float(input("Digite o novo preço do produto: "))
            linha[1] = nome_produto
            linha[2] = preco_produto
            break
    with open('produtos.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(produtos)
    print("Produto atualizado com sucesso!")

def remover_produto():
    produtos = ler_produtos()  # Atribui o retorno de ler_produtos() à variável produtos
    id_produto = input("Digite o ID do produto a ser removido: ")
    for produto in produtos:
        if produto[0] == id_produto:
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            break
    else:
        print("Produto não encontrado!")
    with open('produtos.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["ID", "Nome", "Preço"])  # Escreve a linha de cabeçalho
        escritor.writerows(produtos)  # Escreve a lista de produtos

def listar_produtos():
    produtos = ler_produtos()
    for produto in produtos:
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}")

def buscar_produto():
    busca = input("Digite o nome ou ID do produto que deseja buscar: ")
    with open('produtos.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Pular a linha de cabeçalho
        for linha in leitor:
            if len(linha) >= 3:
                if linha[0] == busca or linha[1].lower() == busca.lower():
                    print(f"ID: {linha[0]}, Nome: {linha[1]}, Preço: {linha[2]}")
                    return
    print("Produto não encontrado!")

# Função para imprimir os produtos ordenados por nome
def imprimir_por_nome():
    produtos = []
    with open('produtos.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Pular a linha de cabeçalho
        for linha in leitor:
            if linha:  # Ignorar linhas vazias
                produtos.append(linha)
    produtos.sort(key=lambda x: x[1].lower())
    print("Produtos ordenados por nome:")
    for linha in produtos:
        print(f"ID: {linha[0]}, Nome: {linha[1]}, Preço: {linha[2]}")

def imprimir_por_preco():
    produtos = []
    with open('produtos.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Pular a linha de cabeçalho
        for linha in leitor:
            if linha:  # Ignorar linhas vazias
                produtos.append(linha)
    produtos.sort(key=lambda x: float(x[2]) if len(x) >= 3 else float('inf'))
    print("Produtos ordenados por preço:")
    for linha in produtos:
        if len(linha) >= 3:
            print(f"ID: {linha[0]}, Nome: {linha[1]}, Preço: {linha[2]}")
        else:
            print(f"Linha inválida: {linha}")

def sistema_gerenciamento():
    while True:
        print("Sistema de Gerenciamento de Produtos e Usuários")
        print("-------------------------------")
        print("1. Login")
        print("2. Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            login()
        elif opcao == 2:
            break
        else:
            print("Opção inválida. Tente novamente!")

def login():
    id_usuario = int(input("Digite o ID do usuário: "))
    senha_usuario = input("Digite a senha do usuário: ")
    with open('usuarios.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Pular a linha de cabeçalho
        for linha in leitor:
            if linha[0] == str(id_usuario) and linha[2] == senha_usuario:
                if linha[3] == "Gerente":
                    menu_gerente()
                elif linha[3] == "Funcionario":
                    menu_funcionario()
                else:
                    print("Tipo de usuário desconhecido.")
                break
        else:
            print("Usuário ou senha inválidos.")

def menu_gerente():
   while True:
        print("Menu do Gerente:")
        print("1. Criar produto")
        print("2. Ler produtos")
        print("3. Atualizar produto")
        print("4. Deletar produto")
        print("5. Buscar produto")
        print("6. Imprimir produtos por nome")
        print("7. Imprimir produtos por preço")
        print("8. Voltar ao menu principal")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            criar_produto()
        elif opcao == "2":
            ler_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            buscar_produto()
        elif opcao == "6":
            imprimir_por_nome()
        elif opcao == "7":
            imprimir_por_preco()
        elif opcao == "8":
            break
        else:
            print("Opção inválida. Tente novamente!")

def menu_funcionario():
    while True:
        print("Menu do Funcionário:")
        print("1. Ler produtos")
        print("2. Buscar produto")
        print("3. Imprimir produtos por nome")
        print("4. Imprimir produtos por preço")
        print("5. Voltar ao menu principal")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            ler_produtos()
        elif opcao == "2":
            buscar_produto()
        elif opcao == "3":
            imprimir_por_nome()
        elif opcao == "4":
            imprimir_por_preco()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente!")

sistema_gerenciamento()