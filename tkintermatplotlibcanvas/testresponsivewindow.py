import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

points = []
ax = None
canvas = None
fig = None

def on_click(event):
	print("event.inaxes: ",event.inaxes)
	print("event x and y:",event.x,event.y)
	print("event x- and y-data:",event.xdata,event.ydata)
	print("xrange:",ax.get_xlim()[0],ax.get_xlim()[1])
	print("dpi:",fig.get_dpi())
	print("markersize:" ,(100 / 72.0 * fig.get_dpi()) * 0.5)
	print("get_window_extent:",ax.get_window_extent())

	if event.button == 1 and event.inaxes != None:
		points.append([event.xdata,event.ydata])
	if event.button == 3 and event.inaxes != None:
		pass

	points_transposed = np.transpose(points)
	print(points_transposed)
	
	ax.plot(points_transposed[0],points_transposed[1],marker=".",markersize=10)
	canvas.draw()


def set_frame1(window):
	frame = tkinter.Frame(window)
	frame.place(relwidth=0.7,relheight=1)

	global fig
	fig = Figure(figsize=(5, 4), dpi=100)
	global ax
	ax = fig.add_subplot(111)
	ax.set_xlim(0, 100)
	ax.set_ylim(0, 100)
	ax.grid(which="both")

	global canvas
	canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea.
	canvas.mpl_connect('button_press_event',on_click)
	canvas.draw()
	canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
	

	toolbar = NavigationToolbar2Tk(canvas, frame)
	toolbar.update()
	canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def set_frame2(window):
	frame2 = tkinter.Frame(window)
	frame2.place(relx=0.7,relwidth=0.3,relheight=1)

	fig2 = Figure(figsize=(5, 4), dpi=100)
	t2 = np.arange(0, 3, .01)
	fig2.add_subplot(311).plot(t2, 2 * np.sin(2 * np.pi * t2))
	fig2.add_subplot(312).plot(t2, 2 * np.sin(2 * np.pi * t2))
	fig2.add_subplot(313).plot(t2, 2 * np.sin(2 * np.pi * t2))

	canvas2 = FigureCanvasTkAgg(fig2, master=frame2)  # A tk.DrawingArea.
	canvas2.draw()
	canvas2.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

if __name__ == "__main__":
	root = tkinter.Tk()
	root.wm_title("Embedding in Tk")
	root.geometry("640x480")

	set_frame1(root)
	set_frame2(root)

	tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.

#########################################################################
# tkinter place method
#########################################################################

# anchor − The exact spot of widget other options refer to: may be N, E, S, W, NE, NW, SE, or SW, compass directions indicating the corners and sides of widget; default is NW (the upper left corner of widget)

# bordermode − INSIDE (the default) to indicate that other options refer to the parent's inside (ignoring the parent's border); OUTSIDE otherwise.

# height, width − Height and width in pixels.

# relheight, relwidth − Height and width as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.

# relx, rely − Horizontal and vertical offset as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.

# x, y − Horizontal and vertical offset in pixels.