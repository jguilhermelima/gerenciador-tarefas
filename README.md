# 📋 Gerenciador de Tarefas

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📌 Sobre o Projeto

Este é um sistema web completo para **gerenciamento de tarefas**, desenvolvido com uma arquitetura RESTful. O projeto permite que usuários organizem suas atividades diárias de forma simples e eficiente, com operações básicas de CRUD (Criar, Ler, Atualizar, Deletar).

A aplicação utiliza **Flask** no backend, **Flask SQLAlchemy** para gerenciamento do banco de dados e templates **HTML** para a interface do usuário.

## ✨ Funcionalidades

- ✅ **Criar tarefas** – Adicione novas tarefas com título, descrição e status
- ✏️ **Editar tarefas** – Modifique informações de tarefas existentes
- ❌ **Excluir tarefas** – Remova tarefas que não são mais necessárias
- 👁️ **Listar tarefas** – Visualize todas as tarefas em uma interface organizada
- 🔄 **API RESTful** – Comunicação padronizada para integração com outros sistemas

## 🛠️ Tecnologias Utilizadas

- **Python** – Linguagem principal (51.6% do código)
- **Flask** – Framework web para criação da API e rotas
- **Flask SQLAlchemy** – ORM para interação com o banco de dados
- **HTML** – Estrutura da interface do usuário (48.4% do código)
- **SQLite** – Banco de dados padrão (configurável)

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado
- Pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/jguilhermelima/gerenciador-tarefas.git
   cd gerenciador-tarefas
2. **Crie um ambiente virtual (recomendado)**
    ```bash  
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate   
3. **Instale as dependências**
    ```bash
   pip install -r requirements.txt
4. **Execute a aplicação**  
    ```bash
   python main.py
5. **Acesse no navegador**  
    ```bash
    http://localhost:5000
