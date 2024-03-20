# Análise de Custos AWS

Este projeto é um script Python que permite ao usuário analisar os custos dos serviços AWS em um período de tempo específico. Ele usa a biblioteca boto3 para interagir com a AWS e a biblioteca datetime para manipular datas.

## Pré-requisitos

- Python 3.6 ou superior
- Uma conta AWS com acesso ao serviço de custos e uso (CE)
- A biblioteca boto3 instalada
- As credenciais da AWS configuradas (você pode configurá-las usando o comando `aws configure` do AWS CLI)

## Instalação

Para instalar as dependências necessárias, você pode usar o pip, que é o gerenciador de pacotes do Python. Se você estiver usando um ambiente virtual (recomendado), você pode instalar as dependências executando:

```bash
pip install -r requirements.txt
```

Se você não estiver usando um ambiente virtual, você pode instalar as dependências globalmente executando:

```
pip install --user -r requirements.txt
```

## Execução

Para executar o script, você pode usar o seguinte comando:

```
python3 analise-de-custos.py
```

Ou

```
python3 -m analise_de_custos
```

O script irá solicitar que você insira as datas de início e término para a análise de custos. As datas devem ser inseridas no formato AAAA-MM-DD. Em seguida, o script irá listar os custos dos serviços AWS para o período de tempo especificado.

## Extras

- 1. **Executando o teste**:

```
python3 -m unittest tests.test_analise_de_custos
```
