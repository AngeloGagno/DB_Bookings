# DB Bookings

Esta aplicação utiliza as bibliotecas **Requests** e **SQLAlchemy** para buscar dados de reservas realizadas em um determinado período a partir de uma API e armazená-las em um banco de dados.

## Recursos Principais

- Busca de dados de reservas de uma API.
- Armazenamento de dados em um banco de dados relacional usando SQLAlchemy.
- Fácil configuração e personalização para diferentes APIs e bancos de dados.

---

## Pré-requisitos

Certifique-se de ter o seguinte instalado no seu ambiente de desenvolvimento:

- Python 3.8 ou superior
- Docker Instalado
- Um banco de dados relacional (MySQL, PostgreSQL, SQLite, etc.)

---

## Instalação

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/AngeloGagno/DB_Bookings.git
   cd DB_Bookings
    ```

2. **Configure o banco de dados**: 
```
    Crie um arquivo .env na raiz do projeto com a string de conexão do banco de dados e a API Key da Avantio
```
3. **Executando o docker compose build**
  - Caso queira obter reservas em determinadas datas de check-in
 ```bash
   docker-compose run --build
 ```
