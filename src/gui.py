import tkinter as tk

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

        self.logo = tk.PhotoImage(file="C:/Users/Robert Frank/Desktop/Coding/Python/Untis-Lesson-Cancellation/resources/Untis.png")

        self.label = tk.Label(self.root, text="WebUntis", image=self.logo, compound="right", font=("Helvetica", 20))
        self.label.pack(pady=10)
        self.label.configure(bg='orange')

        self.entry1 = PlaceholderEntry(self.root, placeholder="Username", font=("Helvetica", 14))
        self.entry1.pack(pady=5)

        self.entry2 = PlaceholderEntry(self.root, placeholder="Password", font=("Helvetica", 14))
        self.entry2.pack(pady=20)

        self.button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.button.pack(pady=10)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Startscreen()
    app.run()