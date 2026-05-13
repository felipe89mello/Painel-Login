# Painel Login
Abri uma tela para login em um sistema

# 🔐 Sistema de Login

Sistema de login desktop desenvolvido em Python com interface gráfica moderna, autenticação segura e banco de dados local.

## 🖥️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — Interface gráfica moderna
- [bcrypt](https://pypi.org/project/bcrypt/) — Hash seguro de senhas
- [SQLite](https://www.sqlite.org/) — Banco de dados local

## ✅ Funcionalidades

- Login com usuário e senha
- Cadastro de novos usuários
- Senhas armazenadas com hash (bcrypt)
- Limite de 3 tentativas de login
- Tela principal após login bem-sucedido
- Logout com retorno à tela de login

## 📁 Estrutura do projeto

\`\`\`
sistema-login/
├── main.py        # Interface principal
├── funcoes.py     # Lógica da aplicação
├── icone.ico      # Ícone do app
└── usuarios.db    # Banco de dados (criado automaticamente)
\`\`\`

## ⚙️ Como rodar

### 1. Clone o repositório
\`\`\`
git clone https://github.com/seu-usuario/seu-repositorio.git
\`\`\`

### 2. Instale as dependências
\`\`\`
pip install customtkinter bcrypt
\`\`\`

### 3. Execute
\`\`\`
python main.py
\`\`\`

## 📦 Gerar executável

\`\`\`
pyinstaller --onefile --windowed --icon=icone.ico --add-data "icone.ico;." main.py
\`\`\`

O executável será gerado na pasta `dist/`.

## ⚠️ Observações

- O arquivo `usuarios.db` é criado automaticamente na primeira execução
- Não compartilhe o `usuarios.db` publicamente pois contém dados de usuários