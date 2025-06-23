from icontract import require, ensure, invariant
from typing import Optional, Tuple
from no import NoArvoreB
from contratos import (
    folhas_no_mesmo_nivel, 
    todas_chaves_ordenadas_internos,
    todas_chaves_ordenadas_folhas,
    limites_chaves_pos_condicao,
    limites_filhos_pos_condicao,
    altura_alterada_corretamente
)

@invariant(lambda self: folhas_no_mesmo_nivel(self.raiz), 
          "Todas as folhas devem estar no mesmo nível")
@invariant(lambda self: todas_chaves_ordenadas_internos(self.raiz), 
          "Chaves dos nós internos devem estar ordenadas")
@invariant(lambda self: todas_chaves_ordenadas_folhas(self.raiz), 
          "Chaves dos nós folhas devem estar ordenadas")
class ArvoreB:
    def __init__(self, ordem: int):
        self.ordem = ordem
        self.raiz = NoArvoreB(ordem, folha=True)
        self._altura = 0

    def contem(self, chave: int) -> bool:
        """Verifica se a chave existe na árvore"""
        return self._busca(self.raiz, chave) is not None

    def _busca(self, no: NoArvoreB, chave: int) -> Optional[NoArvoreB]:
        """Busca uma chave na árvore recursivamente"""
        i = 0
        while i < len(no.chaves) and chave > no.chaves[i]:
            i += 1
        
        if i < len(no.chaves) and chave == no.chaves[i]:
            return no
        elif no.folha:
            return None
        else:
            return self._busca(no.filhos[i], chave)

    @require(lambda self, chave: not self.contem(chave), 
            "Chave a ser inserida não deve existir na árvore")
    @ensure(lambda self: limites_chaves_pos_condicao(self.raiz), 
           "Limites de chaves devem ser válidos após inserção")
    @ensure(lambda self: limites_filhos_pos_condicao(self.raiz), 
           "Limites de filhos devem ser válidos após inserção")
    def inserir(self, chave: int):
        """Insere uma chave na árvore"""
        altura_anterior = self._altura
        raiz = self.raiz
        
        if raiz.cheia():
            # Criar nova raiz e dividir a raiz antiga
            nova_raiz = NoArvoreB(self.ordem, folha=False)
            nova_raiz.filhos.append(raiz)
            self.raiz = nova_raiz
            self._dividir_filho(nova_raiz, 0)
            self._altura += 1
            self._inserir_nao_cheio(nova_raiz, chave)
        else:
            self._inserir_nao_cheio(raiz, chave)

    @require(lambda self, chave: self.contem(chave), 
            "Chave a ser removida deve existir na árvore")
    @ensure(lambda self: limites_chaves_pos_condicao(self.raiz), 
           "Limites de chaves devem ser válidos após remoção")
    @ensure(lambda self: limites_filhos_pos_condicao(self.raiz), 
           "Limites de filhos devem ser válidos após remoção")
    def remover(self, chave: int):
        """Remove uma chave da árvore"""
        altura_anterior = self._altura
        self._remover_recursivo(self.raiz, chave)
        
        # Se a raiz ficou vazia e tem filhos, promover o único filho
        if len(self.raiz.chaves) == 0 and not self.raiz.folha:
            if len(self.raiz.filhos) > 0:
                self.raiz = self.raiz.filhos[0]
                self._altura -= 1

    def _inserir_nao_cheio(self, no: NoArvoreB, chave: int):
        """Insere uma chave em um nó que não está cheio"""
        i = len(no.chaves) - 1
        
        if no.folha:
            # Inserir em folha
            no.chaves.append(0)
            while i >= 0 and chave < no.chaves[i]:
                no.chaves[i + 1] = no.chaves[i]
                i -= 1
            no.chaves[i + 1] = chave
        else:
            # Encontrar filho correto
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            i += 1
            
            # Se filho está cheio, dividi-lo
            if no.filhos[i].cheia():
                self._dividir_filho(no, i)
                if chave > no.chaves[i]:
                    i += 1
            
            self._inserir_nao_cheio(no.filhos[i], chave)

    def _dividir_filho(self, pai: NoArvoreB, indice: int):
        """Divide um filho cheio do nó pai"""
        ordem = self.ordem
        no_cheio = pai.filhos[indice]
        novo_no = NoArvoreB(ordem, folha=no_cheio.folha)
        
        # Índice da chave do meio
        meio = ordem - 1
        chave_meio = no_cheio.chaves[meio]
        
        # Mover segunda metade das chaves para o novo nó
        novo_no.chaves = no_cheio.chaves[meio + 1:]
        no_cheio.chaves = no_cheio.chaves[:meio]
        
        # Se não é folha, mover também os filhos
        if not no_cheio.folha:
            novo_no.filhos = no_cheio.filhos[meio + 1:]
            no_cheio.filhos = no_cheio.filhos[:meio + 1]
        
        # Inserir chave do meio no pai
        pai.chaves.insert(indice, chave_meio)
        pai.filhos.insert(indice + 1, novo_no)

    def _remover_recursivo(self, no: NoArvoreB, chave: int):
        """Remove uma chave recursivamente"""
        i = 0
        while i < len(no.chaves) and chave > no.chaves[i]:
            i += 1
        
        if i < len(no.chaves) and chave == no.chaves[i]:
            # Chave encontrada
            if no.folha:
                # Caso 1: Chave em nó folha
                no.chaves.pop(i)
            else:
                # Caso 2: Chave em nó interno
                self._remover_de_no_interno(no, chave, i)
        elif not no.folha:
            # Caso 3: Chave não está neste nó, descer para filho
            filho = no.filhos[i]
            
            # Verificar se o filho tem chaves suficientes
            if filho.underflow():
                self._corrigir_underflow(no, i)
                # Reajustar índice após possível fusão/redistribuição
                if i < len(no.chaves) and chave > no.chaves[i]:
                    i += 1
            
            if i < len(no.filhos):
                self._remover_recursivo(no.filhos[i], chave)

    def _remover_de_no_interno(self, no: NoArvoreB, chave: int, indice: int):
        """Remove chave de um nó interno"""
        filho_esquerdo = no.filhos[indice]
        filho_direito = no.filhos[indice + 1]
        
        if filho_esquerdo.pode_emprestar():
            # Caso 2a: Filho esquerdo tem chaves extras
            predecessor = self._obter_predecessor(filho_esquerdo)
            no.chaves[indice] = predecessor
            self._remover_recursivo(filho_esquerdo, predecessor)
        elif filho_direito.pode_emprestar():
            # Caso 2b: Filho direito tem chaves extras
            sucessor = self._obter_sucessor(filho_direito)
            no.chaves[indice] = sucessor
            self._remover_recursivo(filho_direito, sucessor)
        else:
            # Caso 2c: Ambos os filhos têm apenas t-1 chaves
            self._fusao(no, indice)
            self._remover_recursivo(filho_esquerdo, chave)

    def _obter_predecessor(self, no: NoArvoreB) -> int:
        """Obtém o predecessor (maior chave da subárvore esquerda)"""
        while not no.folha:
            no = no.filhos[-1]
        return no.chaves[-1]

    def _obter_sucessor(self, no: NoArvoreB) -> int:
        """Obtém o sucessor (menor chave da subárvore direita)"""
        while not no.folha:
            no = no.filhos[0]
        return no.chaves[0]

    def _corrigir_underflow(self, pai: NoArvoreB, indice: int):
        """Corrige underflow em um filho"""
        filho = pai.filhos[indice]
        
        # Tentar redistribuição com irmão esquerdo
        if indice > 0 and pai.filhos[indice - 1].pode_emprestar():
            self._redistribuir_do_esquerdo(pai, indice)
        # Tentar redistribuição com irmão direito
        elif indice < len(pai.filhos) - 1 and pai.filhos[indice + 1].pode_emprestar():
            self._redistribuir_do_direito(pai, indice)
        # Fusão com irmão esquerdo
        elif indice > 0:
            self._fusao(pai, indice - 1)
        # Fusão com irmão direito
        else:
            self._fusao(pai, indice)

    def _redistribuir_do_esquerdo(self, pai: NoArvoreB, indice: int):
        """Redistribui uma chave do irmão esquerdo"""
        filho = pai.filhos[indice]
        irmao = pai.filhos[indice - 1]
        
        # Mover chave do pai para o filho
        filho.chaves.insert(0, pai.chaves[indice - 1])
        
        # Mover última chave do irmão para o pai
        pai.chaves[indice - 1] = irmao.chaves.pop()
        
        # Se não é folha, mover também o filho
        if not filho.folha:
            filho.filhos.insert(0, irmao.filhos.pop())

    def _redistribuir_do_direito(self, pai: NoArvoreB, indice: int):
        """Redistribui uma chave do irmão direito"""
        filho = pai.filhos[indice]
        irmao = pai.filhos[indice + 1]
        
        # Mover chave do pai para o filho
        filho.chaves.append(pai.chaves[indice])
        
        # Mover primeira chave do irmão para o pai
        pai.chaves[indice] = irmao.chaves.pop(0)
        
        # Se não é folha, mover também o filho
        if not filho.folha:
            filho.filhos.append(irmao.filhos.pop(0))

    def _fusao(self, pai: NoArvoreB, indice: int):
        """Funde dois filhos adjacentes"""
        filho_esquerdo = pai.filhos[indice]
        filho_direito = pai.filhos[indice + 1]
        
        # Mover chave do pai para o filho esquerdo
        chave_pai = pai.chaves.pop(indice)
        filho_esquerdo.chaves.append(chave_pai)
        
        # Mover todas as chaves do filho direito para o esquerdo
        filho_esquerdo.chaves.extend(filho_direito.chaves)
        
        # Se não são folhas, mover também os filhos
        if not filho_esquerdo.folha:
            filho_esquerdo.filhos.extend(filho_direito.filhos)
        
        # Remover referência ao filho direito
        pai.filhos.pop(indice + 1)

    def imprimir(self, no: Optional[NoArvoreB] = None, nivel: int = 0):
        """Imprime a árvore de forma hierárquica"""
        if no is None:
            no = self.raiz
        print("  " * nivel + f"Nível {nivel}: {no.chaves}")
        for filho in no.filhos:
            self.imprimir(filho, nivel + 1)

    def altura(self) -> int:
        """Retorna a altura da árvore"""
        return self._altura

    def validar_arvore(self) -> bool:
        """Valida se a árvore satisfaz todas as propriedades da Árvore-B"""
        try:
            return (folhas_no_mesmo_nivel(self.raiz) and
                   todas_chaves_ordenadas_internos(self.raiz) and
                   todas_chaves_ordenadas_folhas(self.raiz) and
                   limites_chaves_pos_condicao(self.raiz) and
                   limites_filhos_pos_condicao(self.raiz))
        except:
            return False