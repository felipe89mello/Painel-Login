import customtkinter as ctk
from funcoes import criar_banco, validar_login, abrir_tela_cadastro, resource_path

ctk.set_appearance_mode('dark')

criar_banco()

app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('400x400')
app.iconbitmap(resource_path('bolaico.ico'))

ctk.CTkLabel(app, text='Usuário:').pack(pady=10)
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário:')
campo_usuario.pack(pady=10)

ctk.CTkLabel(app, text='Senha:').pack(pady=10)
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha:', show='*')
campo_senha.pack(pady=10)

resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=5)

botao_login = ctk.CTkButton(
    app,
    text='Login',
    command=lambda: validar_login(
        campo_usuario, campo_senha, resultado_login, botao_login, app
    )
)
botao_login.pack(pady=5)

botao_cadastro = ctk.CTkButton(
    app,
    text='Novo Usuário',
    command=lambda: abrir_tela_cadastro(app),
    fg_color='transparent',
    border_width=1,
    text_color=('gray10', 'gray90')
)
botao_cadastro.pack(pady=5)

app.mainloop()