from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np

def pr():
  print("HALLO")

fig = Figure(figsize = (9, 6), facecolor = "white")
axis = fig.add_subplot(111)

x = np.linspace(-10, 10, 1000)

axis.plot(x, np.sin(x), "-r", label = "Sinus")
axis.plot(x, np.cos(x), "--g", label = "Cosinus")

axis.set_xticks([-10, 0, 10])
axis.set_yticks([-1, 0, 1])
axis.set_ylim(-2, 2)
axis.set_xlabel("Sinus- und Cosinus-Kurve")

axis.legend()
axis.grid()

root = tk.Tk()
root.title("Sinus vs. Cosinus")

canvas = FigureCanvasTkAgg(fig, master = root)
canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

b = tk.Button(root, text="OK", command=pr)
b.pack()

root.mainloop()