import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
from matplotlib import backend_bases

#mpl.rcParams['toolbar'] = 'None'
# backend_bases.NavigationToolbar2.toolitems = (
#     ('Home', 'Reset original view', 'home', 'home'),
#     ('Back', 'Back to  previous view', 'back', 'back'),
#     ('Forward', 'Forward to next view', 'forward', 'forward'),
#     (None, None, None, None),
#     ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
#     ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
#     ('Subplots', 'Configure subplots', 'subplots', 'configure_subplots'),
#     (None, None, None, None),
#     ('Save', 'Save the figure', 'filesave', 'save_figure'),
#   )
#backend_bases.NavigationToolbar2.toolitems = ()

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)

t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect("key_press_event", on_key_press)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.