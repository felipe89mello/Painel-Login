import customtkinter as ctk

# Configurar a Aparência
ctk.set_appearance_mode('dark')

# Criação das funções de funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # Verificar se o usuário é felipe e a senha 123456
    if usuario == 'felipe' and senha == '123456':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
        abrir_tela_principal(usuario)
    else:
        resultado_login.configure(text='Login incorreto!', text_color='red')

def abrir_tela_principal(usuario):
    # Esconder a janela de login
    app.withdraw()

    # Criar nova janela
    tela_principal = ctk.CTkToplevel()
    tela_principal.title('Área Principal')
    tela_principal.geometry('400x300')

    # Conteúdo da tela principal
    label_boas_vindas = ctk.CTkLabel(
        tela_principal,
        text=f'Bem-vindo, {usuario}! 👋',
        font=ctk.CTkFont(size=24, weight='bold')
    )
    label_boas_vindas.pack(pady=40)

    label_info = ctk.CTkLabel(
        tela_principal,
        text='Você está logado com sucesso.',
        font=ctk.CTkFont(size=14),
        text_color='gray'
    )
    label_info.pack(pady=5)

    # Botão de logout
    def logout():
        tela_principal.destroy()
        app.deiconify()  # Reexibir a janela de login
        campo_usuario.delete(0, 'end')
        campo_senha.delete(0, 'end')
        resultado_login.configure(text='')

    botao_logout = ctk.CTkButton(
        tela_principal,
        text='Sair (Logout)',
        command=logout,
        fg_color='red',
        hover_color='darkred'
    )
    botao_logout.pack(pady=40)

    # Se fechar a janela pelo X, também faz logout
    tela_principal.protocol('WM_DELETE_WINDOW', logout)

# Criação da Janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

# Criação dos Campos
# Label
label_usuario = ctk.CTkLabel(app,text='Usuário:')
label_usuario.pack(pady=10)
# Entry
campo_usuario = ctk.CTkEntry(app,placeholder_text= 'Digite seu usuário:')
campo_usuario.pack(pady=10)
# Label
label_senha = ctk.CTkLabel(app,text='Senha:')
label_senha.pack(pady=10)
# Entry
campo_senha = ctk.CTkEntry(app,placeholder_text= 'Digite sua senha:',show='*')
campo_senha.pack(pady=10)
# Button
botao_login = ctk.CTkButton(app,text='Login',command=validar_login)
botao_login.pack(pady=10)

# Campo Feedback de Login
resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)

# Iniciar a aplicação
app.mainloop()