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

- rssz/cadastrar-sobrevivente/
- rssz/cadastrar-item/
- rssz/alterar-localizacao/
- rssz/sinalizar-infectado/
- rssz/trocar-itens/
- rssz/relatorio/infectados/
- rssz/relatorio/nao-infectados/
- rssz/relatorio/recurso-sobrevivente/
- rssz/relatorio/pontos-perdidos/

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
