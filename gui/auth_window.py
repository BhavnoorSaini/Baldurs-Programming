import tkinter as tk
from tkinter import messagebox
import sqlite3
#basic login

def login():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = c.fetchone()

    conn.close()

    if user:
        messagebox.showinfo('Login', 'Login successful!')
    else:
        messagebox.showerror('Login', 'Invalid username or password')

root = tk.Tk()
root.title('Login')

label_username = tk.Label(root, text='Username:')
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text='Password:')
label_password.pack()
entry_password = tk.Entry(root, show='*')
entry_password.pack()

btn_login = tk.Button(root, text='Login', command=login)
btn_login.pack()

root.mainloop()
