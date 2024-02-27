Blog CodeCraze

O Blog de Programação é um projeto que visa fornecer informações, tutoriais e artigos sobre diversos tópicos de programação.

Requisitos de Instalação
asgiref==3.7.2
astroid==3.0.3
colorama==0.4.6
dill==0.3.8
Django==5.0.2
isort==5.13.2
mccabe==0.7.0
pillow==10.2.0
platformdirs==4.2.0
psycopg2-binary==2.9.9
pylint==3.0.3
sqlparse==0.4.4
tomlkit==0.12.3
tzdata==2024.1
Clone o repositório do GitHub:

git clone https://github.com/seu-usuario/nome-do-repositorio.git
Navegue até o diretório do projeto:

cd nome-do-repositorio
Instale as dependências:

pip install -r requirements.txt
Configuração
Configure as variáveis de ambiente necessárias, se aplicável.
Execução do Projeto
Execute as migrações do banco de dados:

python manage.py migrate
Inicie o servidor de desenvolvimento:

python manage.py runserver
Acesse o blog no navegador em http://localhost:8000/home/

Funcionalidades Principais
 Cadastro e login de usuários
 Visualização de artigos e tutoriais
 Filtragem por categoria e linguagem
 Administração de conteúdo através do painel de administração do Django
 Administração de conteúdo diretamente no site

 ![Texto Alternativo](imagens/imag1.png)
