import tkinter
from tkinter import ttk

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


name_selected = None
combobox = None
list_borderWire_names = None

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
		# line.set_data(points_transposed[0],points_transposed[1])
		pass
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

	# check if any navigation toolbar button is active or not
	if ax.get_navigate_mode() == None:

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
	frame.place(relwidth=0.75,relheight=1)

	global fig
	fig = Figure(figsize=(7,6), dpi=100)
	global ax
	ax = fig.add_subplot(111)
	ax.set_xlim(0, 100)
	ax.set_ylim(0, 100)
	ax.set_aspect('equal',adjustable='box',anchor='C')
	fig.set_facecolor("orange")
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
	frame2.place(relx=0.75,relwidth=0.25,relheight=1)

	button_upload_garden = ttk.Button(frame2, text="Upload garden", width=100)
	button_upload_garden.pack(side=tkinter.TOP,padx=20,pady=(50,10))


	global list_borderWire_names
	list_borderWire_names = []
	global name_selected, combobox
	name_selected = tkinter.StringVar()
	combobox = ttk.OptionMenu(frame2, name_selected, *list_borderWire_names,command=change_selected)
	combobox.config(width=50)	
	combobox.pack(side=tkinter.TOP,padx=20,pady=10)

	button_add_list_optionmenu = ttk.Button(frame2, text="add list option menu", width=100, command=add_list)
	button_add_list_optionmenu.pack(side=tkinter.TOP,padx=20,pady=10)

	button_display_data = ttk.Button(frame2, text="Display data", width=100)
	button_display_data.pack(side=tkinter.TOP,padx=20,pady=10)

	button_display_all_data = ttk.Button(frame2, text="Display all data", width="20")
	button_display_all_data.pack(side=tkinter.TOP)

	button_scale_perimeter = ttk.Button(frame2, text="Scale perimeter", width="20")
	button_scale_perimeter.pack(side=tkinter.TOP)

	switch_lines_length = ttk.Checkbutton(frame2, text="Display length", style="Switch.TCheckbutton")
	switch_lines_length.pack(side=tkinter.TOP)


def change_selected(value):

	global name_selected
	name_selected.set(value)
	print(name_selected.get())


def add_list():
	global name_selected,combobox,list_borderWire_names
	list_borderWire_names.append("1")
	print(list_borderWire_names)
	menu = combobox["menu"]
	menu.delete(0, "end")
	for string in list_borderWire_names:
	    menu.add_command(label=string, 
	                     command=lambda value=string: change_selected(value))



if __name__ == "__main__":

	root = tkinter.Tk()
	root.wm_title("Embedding in Tk")
	root.geometry("800x600")
	root.minsize(720,0)

	# Simply set the theme
	root.tk.call("source", "azure.tcl")
	root.tk.call("set_theme", "light")

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