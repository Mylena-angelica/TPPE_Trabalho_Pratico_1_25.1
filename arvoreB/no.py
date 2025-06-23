from typing import List

class NoArvoreB:
    def __init__(self, ordem: int, folha: bool = True):
        self.ordem: int = ordem
        self.folha: bool = folha
        self.chaves: List[int] = []          
        self.filhos: List['NoArvoreB'] = []  

    def cheia(self) -> bool:
        """Verifica se o nó está cheio (2*t-1 chaves)"""
        return len(self.chaves) >= (2 * self.ordem - 1)

    def underflow(self) -> bool:
        """Verifica se o nó tem underflow (menos que t-1 chaves)"""
        return len(self.chaves) < (self.ordem - 1)

    def numero_de_chaves(self) -> int:
        return len(self.chaves)

    def numero_de_filhos(self) -> int:
        return len(self.filhos)

    def pode_emprestar(self) -> bool:
        """Verifica se o nó pode emprestar uma chave (tem mais que t-1 chaves)"""
        return len(self.chaves) > (self.ordem - 1)
