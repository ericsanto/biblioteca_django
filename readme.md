# Biblioteca Municipal

>Status: Em Desenvolvimento 🚧

### Sobre o projeto
<p>O objetivo do projeto é simular uma biblioteca municipal, onde encontra-se vários livros no catálogo. Nessa aplicação é possível:
</p>
<ul>
  <li>Cadastro e Login de usuários com o email</li>
  <li>Navegar pelo catálogo da Bilbioteca</li>
  <li>Reservar livro</li>
  <li>Renovar a reserva do livro</li>
  <li>Fazer a devolução do livro</li>
  <li>Caso o usuário teha permissões, ele pode fazer um CRUD no catálogo da biblioteca</li>
  <li>O usuário pode criar uma lista de livros favoritos</li>
</ul>

## Instalação 🎈

⚠️ É necessário ter o Python instalado na máquina

1. Clone o reopositório
2. Cria uma virtualenv
3. Instale as dependências executando o comando: pip install requirements.txt
4. Execute as migrações digitando o comando: python manage.py migrate

## Uso

Para iniciar o servidor de desenvolvimento, execute o comando: python manage.py runserver