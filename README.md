# Lista de Chamada (MVC / FastAPI)

[🇧🇷 Português](#-português) | [🇺🇸 English](#-english)

---

## 🇧🇷 Português

Aplicação web simples de **Lista de Chamada** utilizando **FastAPI** e templates **Jinja2** com separação entre lógica de rotas (`app.py`), visualização (`templates/`) e estilos (`static/css/styles.css`).

### ✨ Funcionalidades
- Exibição da lista na página inicial (`GET /`)
- Adição de novos nomes via formulário (`POST /add`)
- Rota dinâmica para visualização de itens (`GET /items/{id}`)

### 🛠️ Tecnologias
- Python 3
- FastAPI & Uvicorn
- Jinja2 Templates
- HTML5 & CSS3

### 🚀 Como executar
1. Instale as dependências:
   ```bash
   pip install fastapi uvicorn jinja2 python-multipart
   ```
2. Execute o servidor:
   ```bash
   uvicorn app:app --reload
   ```
3. Acesse `http://127.0.0.1:8000` no navegador.

---

## 🇺🇸 English

Simple **Attendance List** web application built with **FastAPI** and **Jinja2** templates, separating route logic (`app.py`), views (`templates/`), and stylesheets (`static/css/styles.css`).

### ✨ Features
- Displays the attendance list on the home page (`GET /`)
- Adds new names via form submission (`POST /add`)
- Dynamic route for item inspection (`GET /items/{id}`)

### 🛠️ Technologies
- Python 3
- FastAPI & Uvicorn
- Jinja2 Templates
- HTML5 & CSS3

### 🚀 How to run
1. Install the dependencies:
   ```bash
   pip install fastapi uvicorn jinja2 python-multipart
   ```
2. Start the server:
   ```bash
   uvicorn app:app --reload
   ```
3. Open `http://127.0.0.1:8000` in your browser.
