import sqlite3

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

cursor.execute('SELECT id, usuario FROM usuarios')
usuarios = cursor.fetchall()

conn.close()

print(f'{"ID":<5} {"Usuário":<20}')
print('-' * 25)
for usuario in usuarios:
    print(f'{usuario[0]:<5} {usuario[1]:<20}')