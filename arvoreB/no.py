
from typing import List, Optional

class NoArvoreB:
    def __init__(self, ordem: int, folha: bool):
        self.ordem: int = ordem
        self.folha: bool = folha
        self.chaves: List[int] = []          
        self.filhos: List['NoArvoreB'] = []  

    def cheia(self) -> bool:
        return len(self.chaves) >= (2 * self.ordem - 1)

    def underflow(self) -> bool:
        return len(self.chaves) < (self.ordem - 1)

    def numero_de_chaves(self) -> int:
        return len(self.chaves)

    def numero_de_filhos(self) -> int:
        return len(self.filhos)
