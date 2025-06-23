import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from arvore import ArvoreB
from icontract.errors import ViolationError

def test_viola_minimo_de_chaves_apos_remocao():
    arvore = ArvoreB(3)
    for chave in [1, 2, 3, 4, 5, 6]:
        arvore.inserir(chave)

    with pytest.raises(ViolationError) as info:
        arvore.remover(1)
        arvore.remover(2)
        arvore.remover(3)
    print("Erro esperado: %s", info.value)

def test_viola_folhas_no_mesmo_nivel():
    arvore = ArvoreB(3)
    for chave in [10, 20, 30, 40, 50, 60, 70]:
        arvore.inserir(chave)

    with pytest.raises(ViolationError) as info:
        arvore.remover(10)
        arvore.remover(20)
        arvore.remover(30)
        arvore.remover(40)
    print("Erro esperado: %s", info.value)

def test_viola_ordenacao_das_chaves():
    arvore = ArvoreB(3)
    arvore.inserir(10)
    arvore.inserir(20)
        
    arvore.raiz.chaves = [20, 10]
    with pytest.raises(ViolationError) as info:
        arvore.remover(10)
    print("Erro esperado: %s", info.value)

def test_insercao_chave_duplicada():
    arvore = ArvoreB(3)
    arvore.inserir(10)

    with pytest.raises(ViolationError) as info:
        arvore.inserir(10)
    print("Erro esperado: %s", info.value)

def test_remocao_chave_inexistente_quebra():
    arvore = ArvoreB(3)
    arvore.inserir(1)
    arvore.inserir(2)

    with pytest.raises(ViolationError) as info:
        arvore.remover(99)
    print("Erro esperado: %s", info.value)