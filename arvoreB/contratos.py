from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from no import NoArvoreB

def chaves_em_ordem(no: 'NoArvoreB') -> bool:
    """Verifica se as chaves do nó estão em ordem crescente"""
    if len(no.chaves) <= 1:
        return True
    return all(no.chaves[i] < no.chaves[i+1] for i in range(len(no.chaves)-1))

def todas_chaves_ordenadas_internos(raiz: 'NoArvoreB') -> bool:
    """Invariante: Para os nós internos, as chaves estão em ordem crescente"""
    def verificar_no(no: 'NoArvoreB') -> bool:
        # Verifica apenas nós internos (não-folhas)
        if not no.folha and not chaves_em_ordem(no):
            return False
        return all(verificar_no(filho) for filho in no.filhos)
    
    return verificar_no(raiz)

def todas_chaves_ordenadas_folhas(raiz: 'NoArvoreB') -> bool:
    """Invariante: Para os nós folhas, todos os valores estão em ordem crescente"""
    def verificar_no(no: 'NoArvoreB') -> bool:
        # Verifica apenas nós folhas
        if no.folha and not chaves_em_ordem(no):
            return False
        return all(verificar_no(filho) for filho in no.filhos)
    
    return verificar_no(raiz)

def folhas_no_mesmo_nivel(raiz: 'NoArvoreB') -> bool:
    """Invariante: Todos os nós folhas estão no mesmo nível"""
    if not raiz:
        return True
        
    niveis_folhas = []

    def dfs(no: 'NoArvoreB', nivel: int):
        if no.folha:
            niveis_folhas.append(nivel)
        else:
            for filho in no.filhos:
                dfs(filho, nivel + 1)

    dfs(raiz, 0)
    return len(set(niveis_folhas)) <= 1

def limites_chaves_pos_condicao(raiz: 'NoArvoreB') -> bool:
    """Pós-condição: Limites de chaves válidos"""
    def verificar_no(no: 'NoArvoreB', eh_raiz: bool = False) -> bool:
        ordem = no.ordem
        num_chaves = len(no.chaves)
        
        if eh_raiz:
            # Para nó-raiz: 1 ≤ numChaves ≤ 2*t-1
            if num_chaves == 0:
                return True  # Árvore vazia é válida
            return 1 <= num_chaves <= (2 * ordem - 1)
        else:
            # Para nós internos: t-1 ≤ numChaves ≤ 2*t-1
            return (ordem - 1) <= num_chaves <= (2 * ordem - 1)
    
    def dfs(no: 'NoArvoreB', eh_raiz: bool = False) -> bool:
        if not verificar_no(no, eh_raiz):
            return False
        return all(dfs(filho, False) for filho in no.filhos)
    
    return dfs(raiz, True)

def limites_filhos_pos_condicao(raiz: 'NoArvoreB') -> bool:
    """Pós-condição: Limites de filhos válidos"""
    def verificar_no(no: 'NoArvoreB', eh_raiz: bool = False) -> bool:
        ordem = no.ordem
        num_filhos = len(no.filhos)
        
        if no.folha:
            return num_filhos == 0
        
        if eh_raiz:
            # Para nó raiz: 2 ≤ numFilhos ≤ 2*t
            return 2 <= num_filhos <= (2 * ordem)
        else:
            # Para nós internos: t ≤ numFilhos ≤ 2*t
            return ordem <= num_filhos <= (2 * ordem)
    
    def dfs(no: 'NoArvoreB', eh_raiz: bool = False) -> bool:
        if not verificar_no(no, eh_raiz):
            return False
        return all(dfs(filho, False) for filho in no.filhos)
    
    return dfs(raiz, True)

def altura_alterada_corretamente(altura_anterior: int, altura_atual: int, 
                                operacao: str) -> bool:
    """Pós-condição: Altura alterada corretamente após divisão/fusão"""
    if operacao == "divisao":
        return altura_atual == altura_anterior + 1
    elif operacao == "fusao":
        return altura_atual == altura_anterior - 1
    else:
        return altura_atual == altura_anterior