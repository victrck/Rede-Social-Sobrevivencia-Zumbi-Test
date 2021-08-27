# Rede-Social-Sobrevivencia-Zumbi-Test
### Versão 1.0
## Descrição do Problema

ZSSN (Rede Social de Sobrevivência Zumbi). O mundo como o conheceu caiu em
um cenário apocalíptico. Um vírus produzido em laboratório está transformando
seres humanos e animais em zumbis, famintos por carne fresca.
Você, como membro da resistência aos zumbis (e o último sobrevivente que sabe
codificar), foi designado para desenvolver um sistema para compartilhar recursos
entre humanos não infectados.

## Tecnologias usadas: 
- Python 3.9.5
- Django 3.2.6
- Django REST Framework 3.12.4
- PostgreSQL 13

## Rotas

### - ***POST*** rssz/cadastrar-sobrevivente/
  - Exemplo de Entrada:   
    ```
    {
    "nome": "seek",

    "idade": 23,

    "sexo": "Masculino",

    "latitude": "17889°",

    "longitude": "1532°",

    "inventario": [

        {

            "item": "Agua", 

            "quantidade": 1

        }
    ]

    }
    ```
    Campos:
      - "nome"
      - "idade"
      - "sexo": Valores possíveis: "Masculino" ou " Feminino"
      - "latitude": String
      - "longitude": String
      - "inventario": Array de Itens. Cada elemento deve conter os campos "item" e "quantidade". ***Esse campo é opcional.***
      - "item": É o nome do Item. ***Lembrando que os Itens devem ser cadastrados antes do cadastro de Sobreviventes.***
      - "quantidade": É a quantidade informada do item que o Sobrevivente contém.
    
    
### - ***POST*** rssz/cadastrar-item/
  - Exemplo de Entrada:   
    ```
    {

    "nome": "Agua",

    "pontos": 1

    }
    ```
    Campos:
      - "nome": É o nome do Item.
      - "pontos": É a quantidade de pontos que o item possui.
      
    
### - ***PUT*** rssz/alterar-localizacao/
  - Exemplo de Entrada:   
    ```
    {

    "latitude": "70°",

    "longitude": "90°"

    }
    ```
    Campos:
      - "latitude": nova latitude do sobrevivente.
      - "longitude": nova longitude do sobrevivente.
      
      
### - ***POST*** rssz/sinalizar-infectado/
  - Exemplo de Entrada:   
    ```
    {
    "sinalizado_por": 1,
    "possivel_infectado": 2

    }
    ```
    Campos:
      - "sinalizado_por": id do sobrevivente que está sinalizando um sobrevivente infectado.
      - "possivel_infectado": id do possivel sobrevivente infectado.


### - ***POST*** rssz/trocar-itens/
  - Exemplo de Entrada:   
    ```
    }
        "sobrevivente1":{
            "id_sobrevivente": 1,
            "inventario":[
                {
                    "item": "Agua",
                    "quantidade": 2
                },
                {
                    "item": "Alimentacao",
                    "quantidade": 2
                }
            ]
        },
        "sobrevivente2":{
            "id_sobrevivente": 2,
            "inventario":[
                {
                    "item": "Municao",
                    "quantidade": 10
                }
            ]
        }
    }
    ```
    Campos:
      - "sobrevivente1": contem o id do Sobrevivente 1 e tambem o inventario com os itens na qual o Sobrevivente 1 quer trocar.
      - "sobrevivente2": contem o id do Sobrevivente 2 e tambem o inventario com os itens na qual o Sobrevivente 2 quer trocar.
      - "id_sobrevivente": id do sobrevivente.
      - "inventario": array de itens. Cada elemento dentro de recursos deve conter os campos "item" e "quantidade".
      - "item": É o nome do Item. Lembrando que o Item informado deve estar cadastrado no Sistema.
      - "quantidade": É a quantidade informada do item que o Sobrevivente contém.


### - ***GET*** rssz/relatorio/infectados/

### - ***GET*** rssz/relatorio/nao-infectados/

### - ***GET*** rssz/relatorio/recurso-sobrevivente/

### - ***GET*** rssz/relatorio/pontos-perdidos/


## Configuração 

- Crie um virtualenv.
- Instale os pacotes com o seguinte comando: 
  ```
  pip install -r requirements.txt
  ```
- Agore execute os seguintes comandos: 
  ```
  python manage.py makemigrations
  python manage.py migrate sobrevivente
  python manage.py migrate
   ```
- Agora para executar o projeto:
  ```
  python manage.py runserver
  ```
  
### Tarefas a fazer:
- Criar testes
- Realizar melhorias na estrutura do projeto.
