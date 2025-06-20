# Main usada para testar as implementações
from arvore import ArvoreB


T = int(input("Defina a ordem da árvore: "))

arvore = ArvoreB(T)

while True:
    value = input("Qual o valor a ser inserido: ")
    
    if value == "":
        break
    
    value = int(value)
    arvore.inserir(value)

arvore.imprimir()