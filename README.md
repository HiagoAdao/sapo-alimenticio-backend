<p align="center">
  <a href="https://www.django-rest-framework.org/" target="blank"><img src="https://www.django-rest-framework.org/img/logo.png" width="120" alt="Django REST Logo" /></a>
</p>

<p align="center">Build with django <a href="https://www.django-rest-framework.org/" target="_blank"> REST</a> framework</p>
<p align="center">
<br>

## Sapo Alimenticio

Este projeto é um aplicativo de backend que usa a API REST para permitir que os clientes da Sapo Alimentícios visualizem os produtos da rede classificados pela
quantidade majoritária de seus macronutrientes, para facilitar a elaboração de alguma dieta da moda.

## Descrição
O usuário faz upload de arquivos TXT num formato padrão pré-estabelecido, para extração dos dados do mesmo e inserção no Banco de Dados.

## Principais tecnologias utilizadas
- Django [REST](https://www.django-rest-framework.org/) Framework
- [PostgresSQL](https://www.postgresql.org) as database


## Destaques
- API REST FULL

## Requerimentos

- Dependências do LINUX:
```bash
sudo apt install python3-pip python3-venv libpq-dev python-dev
```

- Criar ambiente virtual
```bash
python3 -m venv venv
```
- Ativar o ambiente virtual (LINUX e MAC)
```bash
source venv/bin/activate
```
- Ativar o ambiente virtual (WINDOWS)
```bash
venv/bin/activate.bat
```

- Instalar as dependências
```bash
pip3 install -r requirements.txt
```
- Criar as migrations
```bash
python3 manage.py makemigrations core
```
- Executar as migrations
```bash
python3 manage.py migrate
```

## Execução

- Ativar o ambiente virtual conforme o respectivo SO

- Executar o Server
```bash
python3 manage.py runserver
```

## Uso
- Consumir a API REST disponibilizadas pela página Root criada pelo servidor host:8000

## Executando testes de unidade
...

## Estrutura do Projeto
...


