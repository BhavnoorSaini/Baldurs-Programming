import tkinter as tk

class GameApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Create a container to hold all the pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Create and add the main menu page
        main_menu = MainMenu(parent=container, controller=self)
        main_menu.grid(row=0, column=0, sticky="nsew")
        self.frames["MainMenu"] = main_menu

        # Create and add additional pages here
        # For example:
        # options_page = OptionsPage(parent=container, controller=self)
        # options_page.grid(row=0, column=0, sticky="nsew")
        # self.frames["OptionsPage"] = options_page

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_label = tk.Label(self, text="Main Menu", font=("Helvetica", 24))
        title_label.pack(pady=20)

        start_button = tk.Button(self, text="New Game", command=lambda: controller.show_frame("StartGamePage"))
        start_button.pack(pady=10)

        load_button = tk.Button(self, text="Load Game", command=lambda: controller.show_frame("StartGamePage"))
        load_button.pack(pady=10)

        options_button = tk.Button(self, text="Options", command=lambda: controller.show_frame("OptionsPage"))
        options_button.pack(pady=10)

        quit_button = tk.Button(self, text="Quit", command=self.quit_game)
        quit_button.pack(pady=10)

    def quit_game(self):
        self.controller.destroy()

class StartGamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_label = tk.Label(self, text="Start Game Page", font=("Helvetica", 24))
        title_label.pack(pady=20)

        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame("MainMenu"))
        back_button.pack(pady=10)

class OptionsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_label = tk.Label(self, text="Options Page", font=("Helvetica", 24))
        title_label.pack(pady=20)

        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame("MainMenu"))
        back_button.pack(pady=10)

if __name__ == "__main__":
    app = GameApp()
    app.title("Game Homepage")
    app.mainloop()

#from chatgpt HELLO!!!!!!