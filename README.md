# TPPE_Trabalho_Pratico_1_25.1

Repositório do trabalho prático 1 da disciplina Técnicas de Programação para Plataformas Emergentes do Prof. André Lanna

# Membros 

|Nome | Matrícula |
|-----|-----------|
|Ana Carolina Costa César | 190101450 |
| Ester Flores Lino da Silva |  202063201 | 
| Mylena Angélica Silva Farias | 211029497|
| Wildemberg Sales da Silva Junior | 20201503 |

# Objetivo

O trabalho consiste na elaboração do "algoritmo Árvore-B" por meio do Design by Contracts. Para mais informações, acessar o [enunciado oficial do trabalho](https://github.com/andrelanna/fga0242/tree/master/trabalhoPratico1)

#### Estrutura de Pastas
O Trabalho foi organizado da seguinte maneira

      TPPE_TRABALHO_PRATICO__25.1
      |
      ├── arvoreB/                              # Pasta principal com os códigos desenvolvidos
      │   ├── arvore.py                         # Arquivo com a implementação da árvore
      │   ├── contratos.py                      # Arquivo com a implementação dos contratos
      │   ├── main.py
      │   ├── no.py                             # Arquivo com a implementação de nó
      │   ├── tests/                            # Pasta com os arquivos de testes
      │         ├── test_arvore.py              # Arquivo de teste da arvore
      │         ├── test_violacoes.py           # Arquivo de teste das violações dos contratos
      │   
      ├── README.md
      │   
      └── requirements.txt                      # Arquivo com as bibliotecas e dependências necessárias

# Como executar os testes automatizados
Este projeto utiliza o framework pytest para testes automatizados, e o icontract para validação por contratos.

## Pré-requisitos
- Python 3.12+
- pip e venv


## Etapas para rodar os testes

1. Crie e ative o ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute os testes a partir da raiz do projeto:

```bash
pytest
```

Você verá o relatório dos testes, com detalhes dos que passaram ou falharam.

4. Caso queira visualizar as violações do arquivo `test_violacoes.py`, execute os testes com:

```bash
pytest arvoreB/tests/test_violacoes.py -v -s
```

5. Caso deseje rodar a implementação

```bash
python arvoreB/main.py 
```

## Critérios do trabalho
## ✅ Avaliação por Critério do Enunciado

| Critério          | Descrição                                                           | Entregue? | Evidência                                                                 |
|-------------------|---------------------------------------------------------------------|-----------|---------------------------------------------------------------------------|
| Invariante 1      | Todos os nós folhas estão no mesmo nível                           | ✅         | `@invariant(lambda self: folhas_no_mesmo_nivel(...))` no `arvore.py`     |
| Invariante 2      | Chaves dos nós internos ordenadas                                  | ✅         | `@invariant(lambda self: todas_chaves_ordenadas_internos(...))`          |
| Invariante 3      | Chaves dos nós folhas ordenadas                                    | ✅         | `@invariant(lambda self: todas_chaves_ordenadas_folhas(...))`            |
| Pré-condição 1    | Inserção só se chave não existe                                     | ✅         | `@require(lambda self, chave: not self.contem(...))`                     |
| Pré-condição 2    | Remoção só se chave existe                                          | ✅         | `@require(lambda self, chave: self.contem(...))`                         |
| Pós-condição 1    | Limites de chaves após inserção e remoção                          | ✅         | `@ensure(...limites_chaves_pos_condicao...)`                             |
| Pós-condição 2    | Limites de filhos após inserção e remoção                          | ✅         | `@ensure(...limites_filhos_pos_condicao...)`                             |
| Pós-condição 3    | Aumento/diminuição da altura após divisão/fusão                    | ✅         | Implementado em `altura_alterada_corretamente(...)` e usado em lógica    |
