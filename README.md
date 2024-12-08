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
- Pip (gerenciador de pacotes do Python)
- Um banco de dados relacional (MySQL, PostgreSQL, SQLite, etc.)

---

## Instalação

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/AngeloGagno/DB_Bookings.git
   cd DB_Bookings
    ```
2. **Instalacao das Dependencias**:
 ```bash
    pip install -r requirements.txt
 ```

3. **Configure o banco de dados**: 
```
    Crie um arquivo .env na raiz do projeto com a string de conexão do banco de dados
```
4. **Executando o Script para uma determinada data**
 ```bash
    python ./src/main.py --start_date data_inicio --end_date data_fim
 ```