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

