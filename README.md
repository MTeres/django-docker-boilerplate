# Software Engineer Challenge

## Dependencias locais

* Docker
* Docker Compose


#### Rodando o projeto:

- Clone o projeto

- Entre no diretorio

- Agora levante o container do Docker Mysql `docker-compose up docker_mysql` (somente na primeira vez, para criar o banco de dados), quando terminar de criar o banco pare o docker (Ctrl+C)

- Agora levante todos os containers ao mesmo tempo `docker-compose up --build`

- A aplicação estará rodando `http://localhost:8000`

**OBS:** Importante levantar o container do Mysql (sozinho) na primeira vez que roda o projeto para que seja criada corretamenta a instancia, sem risco de conflitos. As proximas vezes já será possivel rodar todos os containers diretamente.


- A aplicação apresenta uma lisa com os loans em  `http://localhost:8000/dashboard`

- Os endpoints estão em: `http://localhost:8000/api/loans/` , `http://localhost:8000/api/loans/<:id>/payments` e `http://localhost:8000/api/loans/<:id>/balance`