from no import NoArvoreB

def chaves_em_ordem(no: NoArvoreB) -> bool:
    return all(no.chaves[i] <= no.chaves[i+1] for i in range(len(no.chaves)-1))

def folhas_no_mesmo_nivel(raiz: NoArvoreB) -> bool:
    niveis = []

    def dfs(no: NoArvoreB, nivel: int):
        if no.folha:
            niveis.append(nivel)
        for filho in no.filhos:
            dfs(filho, nivel + 1)

    dfs(raiz, 0)
    return all(n == niveis[0] for n in niveis)

def filhos_corretos(no: NoArvoreB) -> bool:
    if no.folha:
        return len(no.filhos) == 0
    return len(no.filhos) == len(no.chaves) + 1
