import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Conectar ao banco de dados MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="//",
        password="//",
        database="user_auth"
    )

# Função para registrar um novo usuário
def register_user():
    username = entry_new_username.get()
    password = entry_new_password.get()

    if not username or not password:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        return

    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    if cursor.fetchone():
        messagebox.showwarning("Aviso", "Nome de usuário já existe.")
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        messagebox.showinfo("Sucesso", "Usuário registrado com sucesso.")
    
    db.close()

# Função para fazer login
def login_user():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        return

    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    if cursor.fetchone():
        messagebox.showinfo("Sucesso", "Login bem-sucedido.")
    else:
        messagebox.showwarning("Erro", "Nome de usuário ou senha incorretos.")
    
    db.close()

# Função para abrir a janela de login
def open_login_window():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("400x200")

    tk.Label(login_window, text="Nome de usuário").grid(row=0, column=0, padx=10, pady=10)
    global entry_username
    entry_username = tk.Entry(login_window)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="Senha").grid(row=1, column=0, padx=10, pady=10)
    global entry_password
    entry_password = tk.Entry(login_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    login_button = tk.Button(login_window, text="Login", command=login_user)
    login_button.grid(row=2, columnspan=2, pady=10)

# Função para abrir a janela de cadastro
def open_signup_window():
    signup_window = tk.Toplevel(root)
    signup_window.title("Cadastro")
    signup_window.geometry("400x200")

    tk.Label(signup_window, text="Novo nome de usuário").grid(row=0, column=0, padx=10, pady=10)
    global entry_new_username
    entry_new_username = tk.Entry(signup_window)
    entry_new_username.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(signup_window, text="Nova senha").grid(row=1, column=0, padx=10, pady=10)
    global entry_new_password
    entry_new_password = tk.Entry(signup_window, show="*")
    entry_new_password.grid(row=1, column=1, padx=10, pady=10)

    signup_button = tk.Button(signup_window, text="Cadastrar", command=register_user)
    signup_button.grid(row=2, columnspan=2, pady=10)

# Configuração da interface gráfica principal com Tkinter
root = tk.Tk()
root.title("Sistema de Autenticação")
root.geometry("300x200")

login_main_button = tk.Button(root, text="Login", command=open_login_window, width=15)
login_main_button.pack(pady=20)

signup_main_button = tk.Button(root, text="Cadastro", command=open_signup_window, width=15)
signup_main_button.pack(pady=20)

root.mainloop()
