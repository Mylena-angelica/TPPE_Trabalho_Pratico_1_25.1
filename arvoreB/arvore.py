from icontract import require, ensure
from typing import Optional
from no import NoArvoreB
from contratos import chaves_em_ordem, folhas_no_mesmo_nivel, filhos_corretos


class ArvoreB:
    def __init__(self, ordem: int):
        self.ordem = ordem
        self.raiz = NoArvoreB(ordem, folha=True)

    def contem(self, chave: int) -> bool:
        return self._busca(self.raiz, chave) is not None

    def _busca(self, no: NoArvoreB, chave: int) -> Optional[NoArvoreB]:
        i = 0
        while i < len(no.chaves) and chave > no.chaves[i]:
            i += 1
        if i < len(no.chaves) and chave == no.chaves[i]:
            return no
        elif no.folha:
            return None
        else:
            return self._busca(no.filhos[i], chave)

    @require(lambda self, chave: not self.contem(chave), "Chave já existe na árvore")
    @ensure(lambda self: chaves_em_ordem(self.raiz), "As chaves da raiz devem estar ordenadas")
    def inserir(self, chave: int):
        raiz = self.raiz
        if raiz.cheia():
            nova_raiz = NoArvoreB(self.ordem, folha=False)
            nova_raiz.filhos.append(raiz)
            self.raiz = nova_raiz
            print("Raiz cheia: lógica de divisão será implementada depois.")
        else:
            self._inserir_nao_cheio(raiz, chave)

    def _inserir_nao_cheio(self, no: NoArvoreB, chave: int):
        i = len(no.chaves) - 1
        if no.folha:
            no.chaves.append(0)  
            while i >= 0 and chave < no.chaves[i]:
                no.chaves[i + 1] = no.chaves[i]
                i -= 1
            no.chaves[i + 1] = chave
        else:
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            i += 1
            if no.filhos[i].cheia():
                print("Filho cheio: lógica de divisão futura.")
            self._inserir_nao_cheio(no.filhos[i], chave)
