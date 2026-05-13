import bcrypt
import sqlite3
import customtkinter as ctk
import os
import sys

MAX_TENTATIVAS = 3
tentativas = 0

# ── Banco de Dados ──────────────────────────────────────────
def criar_banco():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            senha_hash BLOB NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def cadastrar_usuario(usuario, senha):
    hash_senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (usuario, senha_hash) VALUES (?, ?)',
                   (usuario, hash_senha))
    conn.commit()
    conn.close()

def verificar_login(usuario, senha):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT senha_hash FROM usuarios WHERE usuario = ?', (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        return bcrypt.checkpw(senha.encode(), resultado[0])
    return False

# ── Tela de Cadastro ────────────────────────────────────────
def abrir_tela_cadastro(app):
    tela = ctk.CTkToplevel(app)
    tela.title('Novo Usuário')
    tela.geometry('400x400')
    tela.grab_set()

    ctk.CTkLabel(tela, text='Cadastro de Usuário',
                 font=ctk.CTkFont(size=18, weight='bold')).pack(pady=15)

    ctk.CTkLabel(tela, text='Usuário:').pack()
    campo_novo_usuario = ctk.CTkEntry(tela, placeholder_text='Digite o usuário:')
    campo_novo_usuario.pack(pady=5)

    ctk.CTkLabel(tela, text='Senha:').pack()
    campo_nova_senha = ctk.CTkEntry(tela, placeholder_text='Digite a senha:', show='*')
    campo_nova_senha.pack(pady=5)

    ctk.CTkLabel(tela, text='Confirmar Senha:').pack()
    campo_confirmar = ctk.CTkEntry(tela, placeholder_text='Confirme a senha:', show='*')
    campo_confirmar.pack(pady=5)

    feedback = ctk.CTkLabel(tela, text='')
    feedback.pack(pady=5)

    def salvar():
        usuario = campo_novo_usuario.get().strip()
        senha = campo_nova_senha.get()
        confirmar = campo_confirmar.get()

        if not usuario or not senha or not confirmar:
            feedback.configure(text='Preencha todos os campos.', text_color='orange')
            return
        if len(senha) < 6:
            feedback.configure(text='A senha deve ter pelo menos 6 caracteres.', text_color='orange')
            return
        if senha != confirmar:
            feedback.configure(text='As senhas não coincidem.', text_color='red')
            return

        try:
            cadastrar_usuario(usuario, senha)
            feedback.configure(text='Usuário cadastrado com sucesso!', text_color='green')
            campo_novo_usuario.delete(0, 'end')
            campo_nova_senha.delete(0, 'end')
            campo_confirmar.delete(0, 'end')
        except sqlite3.IntegrityError:
            feedback.configure(text='Erro: Usuário já existe.', text_color='red')

    ctk.CTkButton(tela, text='Cadastrar', command=salvar).pack(pady=10)

# ── Lógica de Login ─────────────────────────────────────────
def validar_login(campo_usuario, campo_senha, resultado_login, botao_login, app):
    global tentativas

    if tentativas >= MAX_TENTATIVAS:
        resultado_login.configure(text='Conta bloqueada! Reinicie o app.', text_color='red')
        return

    usuario = campo_usuario.get()
    senha = campo_senha.get()

    campo_senha.delete(0, 'end')

    if not usuario or not senha:
        resultado_login.configure(text='Preencha todos os campos.', text_color='orange')
        return

    if verificar_login(usuario, senha):
        tentativas = 0
        abrir_tela_principal(usuario, campo_usuario, campo_senha, resultado_login, botao_login, app)
    else:
        tentativas += 1
        restantes = MAX_TENTATIVAS - tentativas

        if restantes == 0:
            resultado_login.configure(text='Conta bloqueada! Reinicie o app.', text_color='red')
            botao_login.configure(state='disabled')
        else:
            resultado_login.configure(
                text=f'Usuário ou senha incorretos. {restantes} tentativa(s) restante(s).',
                text_color='red'
            )

# ── Tela Principal ──────────────────────────────────────────
def abrir_tela_principal(usuario, campo_usuario, campo_senha, resultado_login, botao_login, app):
    app.withdraw()

    tela = ctk.CTkToplevel()
    tela.title('Área Principal')
    tela.geometry('400x300')

    ctk.CTkLabel(
        tela,
        text=f'Bem-vindo, {usuario}! 👋',
        font=ctk.CTkFont(size=24, weight='bold')
    ).pack(pady=40)

    ctk.CTkLabel(
        tela,
        text='Você está logado com sucesso.',
        font=ctk.CTkFont(size=14),
        text_color='gray'
    ).pack(pady=5)

    def logout():
        global tentativas
        tentativas = 0
        tela.destroy()
        app.deiconify()
        campo_usuario.delete(0, 'end')
        campo_senha.delete(0, 'end')
        campo_senha.configure(show='*')
        resultado_login.configure(text='')
        botao_login.configure(state='normal')

    ctk.CTkButton(
        tela,
        text='Sair (Logout)',
        command=logout,
        fg_color='red',
        hover_color='darkred'
    ).pack(pady=40)

    tela.protocol('WM_DELETE_WINDOW', logout)

def resource_path(arquivo): # Encontra o icone do app e do executavel
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, arquivo)
    return os.path.join(os.path.dirname(__file__), arquivo)