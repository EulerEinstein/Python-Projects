# import tkinter

# from matplotlib.backends.backend_tkagg import (
#     FigureCanvasTkAgg, NavigationToolbar2Tk)
# # Implement the default Matplotlib key bindings.
# from matplotlib.backend_bases import key_press_handler
# from matplotlib.figure import Figure

# import numpy as np
# from matplotlib import backend_bases

# #mpl.rcParams['toolbar'] = 'None'
# # backend_bases.NavigationToolbar2.toolitems = (
# #     ('Home', 'Reset original view', 'home', 'home'),
# #     ('Back', 'Back to  previous view', 'back', 'back'),
# #     ('Forward', 'Forward to next view', 'forward', 'forward'),
# #     (None, None, None, None),
# #     ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
# #     ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
# #     ('Subplots', 'Configure subplots', 'subplots', 'configure_subplots'),
# #     (None, None, None, None),
# #     ('Save', 'Save the figure', 'filesave', 'save_figure'),
# #   )
# #backend_bases.NavigationToolbar2.toolitems = ()

# root = tkinter.Tk()
# root.wm_title("Embedding in Tk")

# root.geometry("1000x400")

# ## Embedding matplotlib graph in tkinter
# fig = Figure(figsize=(5, 4), dpi=100)

# t = np.arange(0, 3, .01)
# fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
# canvas.draw()
# canvas.get_tk_widget().place(width=500, x=0, y=0)

# tkinter.mainloop()

from tkinter import *
from tkinter import ttk

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
root = Tk()
root.title("Garden 2D-Simulation Editor")
root.geometry("600x400")
## Build interface for menu
menubar = Menu(root)

# Menu file 
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Create new file", command=donothing)
filemenu.add_command(label="Open file", command=donothing)
filemenu.add_command(label="Save file", command=donothing)
filemenu.add_command(label="Save file as", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Save and exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Menu edit
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Add new wire", command=donothing)
editmenu.add_command(label="Delete wire", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

# Menu help
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=donothing)
helpmenu.add_command(label="Documentation", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

nameOfTheFile = Label(root, text="Name of the file: ")
nameOfTheFile.place(x=10,y=5)

filename = Label(root, text="EGMF_garden.yaml")
filename.place(x=110,y=5)

selectWire = Label(root, text="Select the wire:     ")
selectWire.place(x=10,y=30)

wireType = ttk.Combobox(root, width = 27, state="readonly", values=["wireBorder", "wireGuide1", "wireGuide2"])
wireType.place(x=110,y=30)

buttonShowData = Button(root,text="Show data",padx=10)
buttonShowData.place(x=320,y=27)

buttonShowGraph = Button(root,text="Show graph",padx=10)
buttonShowGraph.place(x=420,y=27)

labelxCoordinate = Label(root,text="X-Coordinate")
labelxCoordinate.place(x=30,y=70)

labelyCoordinate = Label(root,text="Y-Coordinate")
labelyCoordinate.place(x=170,y=70)

root.config(menu=menubar)
root.mainloop()