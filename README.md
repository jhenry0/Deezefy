# Deezefy
O Deezefy é uma API para salvar músicas, albuns e artistas. 

## Ferramentas 
- Django
- Postgresql

## Como rodar o código
É necessário fazer a instalação do [Python](https://www.python.org/downloads/) e instalar o [venv](https://docs.python.org/3/library/venv.html).

### 1. Instalar dependência
>  pip install -r requirements.txt 

### 2. Mudar para pasta deezefy
> cd deezefy

### 3. Criando banco de dados local
Como iremos trabalhar localmente, vamos usar o banco de dados de sqlite3.
> python manage.py migrate

### 4. Criando usuário admin
Preencha as informações de usuário, e-mail e senha. Esses dados vão ser usados no admin.
> python manage.py createsuperuser

### 5. Rodando a aplicação
> python manage.py runserver

### 6. Testando
Basta acessar a rota do admin e logar, você terá acesso ao painel administrativo.
> localhost:8000/admin/


