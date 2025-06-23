import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from arvore import ArvoreB

@pytest.fixture
def arvore_t3():
    return ArvoreB(3)

def test_inserir_e_buscar_chave(arvore_t3):
    arvore_t3.inserir(10)
    arvore_t3.inserir(20)
    arvore_t3.inserir(5)

    assert arvore_t3.contem(10)
    assert arvore_t3.contem(20)
    assert arvore_t3.contem(5)
    assert not arvore_t3.contem(15)

def test_remover_chave(arvore_t3):
    for chave in [10, 20, 5, 15]:
        arvore_t3.inserir(chave)

    arvore_t3.remover(10)
    assert not arvore_t3.contem(10)
    assert arvore_t3.validar_arvore()

def test_remocao_com_fusao(arvore_t3):
    for chave in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        arvore_t3.inserir(chave)

    arvore_t3.remover(3)  
    arvore_t3.remover(4)  
    arvore_t3.remover(5)  # Gera fusão, mas com nó ainda válido
    assert arvore_t3.validar_arvore()

def test_remocao_nao_existente(arvore_t3):
    arvore_t3.inserir(5)
    arvore_t3.inserir(10)

    with pytest.raises(Exception):
        arvore_t3.remover(99)

def test_insercao_repetida(arvore_t3):
    arvore_t3.inserir(42)
    with pytest.raises(Exception):
        arvore_t3.inserir(42)

def test_limites_de_chaves_pos_condicao(arvore_t3):
    # Insere muitas chaves e remove algumas para forçar fusão
    chaves = [5, 10, 15, 20, 25, 30, 35]
    for c in chaves:
        arvore_t3.inserir(c)

    arvore_t3.remover(15)

    assert arvore_t3.validar_arvore()

def test_arvore_b_valida_com_estrutura_grande():
    arvore = ArvoreB(3)
    for chave in [
        40, 20, 60, 80, 10, 15, 30, 50, 70, 90, 95, 5, 7, 12, 18,
        25, 35, 45, 55, 65, 75, 85, 92, 98, 99
    ]:
        arvore.inserir(chave)

    assert arvore.validar_arvore()




