# +Sangue
Projeto para incentivar a doação de sangue 

# Primeiros passos...

1 - Criar uma virtualenv e ativá-la:  
  * python -m venv venv  
  * cd venv\Scripts\activate 
  
2 - Clonar o repositório e instalar as dependências:
  * git clone https://github.com/victorveiga/plus-sangue.git
  * cd plus-sangue
  * pip install -r requirements.txt

3 - Criar um arquivo ".env" e adicionar as informações:
  * SECRET_KEY=alguma coisa
  * DEBUG=True
  * Outras informações usadas pelo config do decouple no arquivo plus_sangue/settings.py  
  
4 - Aplicar as migrations:
  * python manage.py migrate
  
5 - Criar um usuário administrador:
  * python manage.py createsuperuser
  * Informar um nome de usuário, email e senha
  
6 - Executar o serviço:
  * python manage.py runserver
  * acessar a homepage através do link: http://localhost:8000/
