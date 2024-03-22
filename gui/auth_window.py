import tkinter as tk
from tkinter import messagebox
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from game import start_game
from database import Session


# Creates a base class for declarative class definitions in SQLAlchemy.
Base = declarative_base()

# User Table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

# Setting up the database connection and creating a session to interact with the 
# database using SQLAlchemy
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def start_gui():
    root = tk.Tk()
    root.geometry('300x200')

    def register_btn_clicked():
        username = username_entry.get()
        password = password_entry.get()
        register(username, password)
        messagebox.showinfo("Registration info", "Registered Successfully")

    def login_btn_clicked():
        username = username_entry.get()
        password = password_entry.get()
        if login(username, password):
            messagebox.showinfo("Login info", "Logged in Successfully")
            on_successful_login()
        else:
            messagebox.showinfo("Login info", "Invalid username or password")

    def register(username, password):
        session = Session()
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        session.close()

    def login(username, password):
        session = Session()
        user = session.query(User).filter_by(username=username, password=password).first()
        session.close()
        return user is not None

    def on_successful_login():
        root.destroy() # Close the login window
        start_game()

    username_label = tk.Label(root, text="Username")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="Password")
    password_label.pack()
    password_entry = tk.Entry(root, show='*')
    password_entry.pack()

    register_btn = tk.Button(root, text="Register", command=register_btn_clicked)
    register_btn.pack()

    login_btn = tk.Button(root, text="Login", command=login_btn_clicked)
    login_btn.pack()

    root.mainloop()
