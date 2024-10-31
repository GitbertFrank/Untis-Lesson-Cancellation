import tkinter as tk
from CalendarApi import loginlogic

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        
        self._add_placeholder()
        
    def _clear_placeholder(self, e):
        if self['fg'] == self.placeholder_color:
            self.delete(0, tk.END)
            self['fg'] = self.default_fg_color

    def _add_placeholder(self, e=None):
        if not self.get():
            self['fg'] = self.placeholder_color
            self.insert(0, self.placeholder)

class Startscreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Untis")
        self.root.configure(bg='gray')

        self.logo = tk.PhotoImage(file="C:/Users/Robert Frank/Desktop/Coding/Python/UntisToCalender/resources/Untis.png")

        self.text_label = tk.Label(self.root, text="WebUntis", font=("Helvetica", 30), bg='orange')
        self.text_label.place(x=0, y=0, anchor='nw')

        self.image_label = tk.Label(self.root, image=self.logo, bg='orange')
        self.image_label.place(x=1920, y=0, anchor='n')

        self.entry1 = PlaceholderEntry(self.root, placeholder="Username", font=("Helvetica", 14))
        self.entry1.pack(pady=30, padx= 100)

        self.entry2 = PlaceholderEntry(self.root, placeholder="Password", font=("Helvetica", 14))
        self.entry2.pack(padx= 100)

        self.button = tk.Button(self.root, text="Login", command=loginlogic, font=("Helvetica", 14))
        self.button.pack(pady=50)
        self.button.configure(bg='green', width= 50, height= 3)

        self.button = tk.Button(self.root, text="Quit", command=self.root.quit, font=("Helvetica", 18))
        self.button.pack(pady=150)
        self.button.configure(bg='red', width= 50, height= 3)

    def run(self):
        self.root.mainloop()
