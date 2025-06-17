from typing import List

# cada nó tem no minimo t-1 chaves
# cada no tem no máximo 2*t-1 chaves

    #                           [Raiz: 40]
    #                |----------/         \-----|
    #               [20]                     [60, 80]
    #        |-----/    \-|            |-----/   |  \----------|
    #     [10, 15]       [30]        [50]       [70]       [90, 95]
    #    /   |   \       /   \       /   \      /   \      /   |   \
    # [5,7] [12] [18] [25] [35]  [45]    [55] [65] [75]  [85] [92] [98, 99]

class Node:
    def __init__(self, folha:bool = False):
        self.folha = folha
        self.chaves: List[int] = []
        self.filhos: List['Node'] = []

class Arvore:
    def __init__(self, t:int):
        self.T = t
        self.minKeys = t-1
        self.maxKeys = 2*t-1
        self.raiz = Node(True)
    
    def inserirChave(self, value:int):
        raiz = self.raiz

        # Se a raiz está cheia, precisamos dividi-la antes de inserir
        if len(raiz.chaves) == self.maxKeys:
            nova_raiz = Node(folha=False)
            nova_raiz.filhos.append(self.raiz)

            # Divide o antigo nó raiz
            self.dividir_filho(nova_raiz, 0)

            # Atualiza a raiz da árvore
            self.raiz = nova_raiz

            # Continua a inserção com a nova raiz
            self._inserir_nao_cheio(nova_raiz, value)
        else:
            # Se a raiz ainda tem espaço, insere diretamente
            self._inserir_nao_cheio(raiz, value)
    
    def _inserir_nao_cheio(self, no, k):
        i = len(no.chaves) - 1

        if no.folha:
            no.chaves.append(None)
            # Ele vai deslocando para a direita os valores, 
            # até liberar a posição certa do número que vai ser inserido
            while i >= 0 and k < no.chaves[i]:
                no.chaves[i + 1] = no.chaves[i]
                i -= 1
            no.chaves[i + 1] = k
        else:
            while i >= 0 and k < no.chaves[i]:
                i -= 1
            i += 1
            if len(no.filhos[i].chaves) == self.maxKeys:
                self.dividir_filho(no, i)
                if k > no.chaves[i]:
                    i += 1
            self._inserir_nao_cheio(no.filhos[i], k)
    
    def dividir_filho(self, nova_raiz, i):
        t = self.T
        no_cheio_velho = nova_raiz.filhos[i] 
        no_novo = Node(folha=no_cheio_velho.folha)  

        # Transfere t-1 chaves do final para o no_novo nó
        no_novo.chaves = no_cheio_velho.chaves[t:]       # direita
        chave_meio = no_cheio_velho.chaves[t - 1]            # chave que vai virar meio
        no_cheio_velho.chaves = no_cheio_velho.chaves[:t - 1]   # esquerda

        if not no_cheio_velho.folha:
            no_novo.filhos = no_cheio_velho.filhos[t:]        
            no_cheio_velho.filhos = no_cheio_velho.filhos[:t]       

        nova_raiz.chaves.insert(i, chave_meio) # nova raiz adiciona a chave do meio 
        nova_raiz.filhos.insert(i + 1, no_novo)


if __name__ == "__main__":
    T = int(input("Defina a ordem da árvore: "))

    arvore = Arvore(T)

    while True:
        value = input("Qual o valor a ser inserido: ")
        
        if value == "":
            break
        
        
        value = int(value)
        arvore.inserirChave(value)
