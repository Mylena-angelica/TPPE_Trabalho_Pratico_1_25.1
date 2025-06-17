# Main usada para testar as implementações
from arvore import ArvoreB

arvore = ArvoreB(ordem=3)
print(arvore.contem(10))   # False
arvore.inserir(10)
print(arvore.contem(10))   # True
arvore.inserir(10)         # Testar erro no contrato
