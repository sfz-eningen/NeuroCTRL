import Tkinter as tk

class App(tk.Tk):
    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.label = tk.Label(self, text="", width=20, anchor="w")
        self.label.pack(side="top",fill="both",expand=True)
        self.print_label_slowly("Hello, world!")

    def print_label_slowly(self, message):
        '''Print a label one character at a time using the event loop'''
        t = self.label.cget("text")
        t += message[0]
        self.label.config(text=t)
        if len(message) > 1:
            self.after(500, self.print_label_slowly, message[1:])

app = App()
app.mainloop()