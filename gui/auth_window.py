import tkinter as tk
from tkinter import messagebox
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from game import start_game
from database import Session
from PIL import Image, ImageTk

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
    root.geometry('1280x720')
    root.title("Baldurs Programming")

    # Add a background image 
    background_image = Image.open("gui/background.png")
    resized_image = background_image.resize((1280, 720))
    background_image = ImageTk.PhotoImage(resized_image)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    

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

    title_label = tk.Label(root, text="BALDURS PROGRAMMING", bg='black', fg='white', font=("verdana", 24))
    title_label.place(x=640, y=100, anchor='center')            # Place the title label at the center of the window
    
    username_label = tk.Label(root, text="Username", bg='black', fg='white')
    username_label.place(x=640, y=200, anchor='center')

    username_entry = tk.Entry(root, bg='grey', fg='white')
    username_entry.place(x=640, y=230, anchor='center')

    password_label = tk.Label(root, text="Password", bg='black', fg='white')
    password_label.place(x=640, y=260, anchor='center')
 
    password_entry = tk.Entry(root, show='*', bg='grey', fg='white')
    password_entry.place(x=640, y=290, anchor='center')

    register_btn = tk.Button(root, text="Register", command=register_btn_clicked)
    register_btn.place(x=640, y=320, anchor='center')

    login_btn = tk.Button(root, text="Login", command=login_btn_clicked)
    login_btn.place(x=640, y=350, anchor='center')

    root.mainloop()



