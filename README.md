## Como subir a aplicação


- Pré-requisitos: Docker e Docker Compose instalados;
- Faça o download do projeto;
- Na pasta raiz, execute o comando 'docker-compose up'.

---

## Informações

A API possui as seguintes rotas:

- GET http://127.0.0.1:8000/filmes

- GET http://127.0.0.1:8000/filmes/{id}

- POST http://127.0.0.1:8000/filmes

Para usar todas as rotas de modo fácil, utilize a página http://127.0.0.1:8000/docs

Para usar o método de encontrar filmes por ID, utilize o UUID64 que é retornado ao usar os outros métodos.
