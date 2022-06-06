import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler, MouseEvent
from matplotlib.figure import Figure

import numpy as np

import math

points = []
ax = None
line = None
canvas = None
fig = None
dragging_point = None
dragging_point_index = None
annot = None

def remove_point(point):
	if point:
		point = list(point)
		if point in points:
			points.remove(point)

def change_point_position(event):
	if dragging_point_index is not None:
		if isinstance(event, MouseEvent):
			x, y = round(float(event.xdata),3), round(float(event.ydata),3)
			points[dragging_point_index] = [x,y]
		update_plot()

def update_annot(ind):
	global line
	x,y = line.get_data()
	global annot
	annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
	print("annot.xy",annot.xy)
	text = "Point {}\nX: {}\nY: {}".format(" ".join(list(map(str,ind["ind"]+1))),
	                        round(x[ind["ind"][0]],3),
	                        round(y[ind["ind"][0]],3))
	print(text)
	annot.set_text(text)
	annot.get_bbox_patch().set_alpha(0.4)
	canvas.draw()

def hover_tooltip(event):

	if event.inaxes != None:
		point = find_neighbor_point(event)
		if point != None:
			temp_point = list(point)
			point_index = points.index(list(point))
			annot.set_visible(True)
			annot.xy = [temp_point[0],temp_point[1]]
			annot.set_text("Point {}\nX: {}\nY: {}".format(point_index+1,round(temp_point[0],3),round(temp_point[1],3)))
			canvas.draw()
		else:
			annot.set_visible(False)
			canvas.draw()

def update_plot():
	global line
	points_transposed = np.transpose(points)

	if points == []:
		line.set_data(points_transposed[0],points_transposed[1])
	else:
		line.set_data(points_transposed[0],points_transposed[1])
		line.set_marker(".")
		line.set_markersize(10)

	canvas.draw()

def find_neighbor_point(event):
        u""" Find point around mouse position
        :rtype: ((int, int)|None)
        :return: (x, y) if there are any point around mouse else None
        """
        distance_threshold = 1
        nearest_point = None
        min_distance = math.sqrt(2 * (100 ** 2))
        for x, y in points:
            distance = math.hypot(event.xdata - x, event.ydata - y)
            if distance < min_distance:
                min_distance = distance
                nearest_point = (x, y)
        if min_distance < distance_threshold:
            return nearest_point
        return None

def on_click(event):
	# print("event.inaxes: ",event.inaxes)
	# print("event x and y in pixels:",event.x,event.y)
	# print("event x- and y-data in points:",event.xdata,event.ydata)
	# print("xrange:",ax.get_xlim()[0],ax.get_xlim()[1])
	# print("dpi:",fig.get_dpi())
	# print("markersize radius in pixels:" ,(100 / 72.0 * fig.get_dpi()) * 0.5)
	# print("get_window_extent:",ax.get_window_extent())

	if event.button == 1 and event.inaxes != None:

		point = find_neighbor_point(event)

		global dragging_point_index

		if point == None:
			points.append([round(event.xdata,3),round(event.ydata,3)])
			dragging_point_index = None
		else:
			dragging_point_index = points.index(list(point))

	if event.button == 3 and event.inaxes != None:
		point = find_neighbor_point(event)
		remove_point(point)
		
	update_plot()

def on_motion(event):

    hover_tooltip(event)

    if dragging_point_index is None:
    	return
    elif event.xdata is None or event.ydata is None:
    	return
    else:
    	change_point_position(event)

def on_release(event):
        u""" callback method for mouse release event
        :type event: MouseEvent
        """
        if event.button == 1 and event.inaxes != None:
        	global dragging_point_index
        	dragging_point_index = None
        	update_plot()

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
	global line
	line, = ax.plot(0,0,marker=".",markersize=1)
	global annot
	annot = ax.annotate("", xy=(0,0), xytext=(-20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
	annot.set_visible(False)

	global canvas
	canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea.
	canvas.mpl_connect('button_press_event',on_click)
	canvas.mpl_connect('motion_notify_event',on_motion)
	canvas.mpl_connect('button_release_event',on_release)
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