# Main usada para testar as implementações
from arvore import ArvoreB

menu = """
    ====== Menu ======
    1 - Inserir Chave
    2 - Remover Chave
    3 - Buscar Chave
    4 - Imprimir Árvore
    5 - SAIR
"""
print("="*40)
T = int(input("Defina a ordem da árvore: "))
print("="*40)

arvore = ArvoreB(T)

while True:
    print(menu)
    op = int(input("Digite o número da opção: "))
    
    if op == 1:
        value = input("\nQual a Chave a ser inserido: ")
        value = int(value)
        arvore.inserir(value)
        print("\nChave inserido com sucesso!\n")
    elif op == 2:
        value = input("\nQual a Chave a ser removido: ")
        value = int(value)
        arvore.remover(value)
        print("\nChave Removida com sucesso!\n")
    elif op == 3:
        value = input("\nQual a Chave a ser buscada: ")
        value = int(value)
        res = arvore._busca(arvore.raiz, value)
        if res == None:
            print("Não encontrado nenhuma chave")
        else:
            print(res)
    elif op == 4:
        print("="*40)
        arvore.imprimir()
        print("="*40)
    elif op == 5:
        print("\nObrigado por usar nosso programa, até mais!\n")
        break
    else:
        print("\nDigite uma opção válida do menu!\n")
