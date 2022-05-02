import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os

filename=""
data={}
list_Info4_1_keys=[]
list_Info4_1_values=[]

# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('1000x500')



def select_file():
    filetypes = (
        ('yaml files', '*.yaml'),
        ('All files', '*.*')
    )

    # Get the current working directory
    cwd = os.getcwd()

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=cwd + '/',
        filetypes=filetypes)

    textfilename.set(filename)

def displayData():
	import yaml

	with open(textfilename.get()) as file:
		global data
		data = yaml.load(file, Loader=yaml.FullLoader)
		textdata.set(data)

############################################################################

def getInfo1():
	textInfo1.set(str(data["Info1"]))

def getInfo4_1():
	#textInfo4_1.set(str(data["Info4"]["Info4.1"]))

	global list_Info4_1_keys
	for key in data["Info4"]["Info4.1"].keys():
		list_Info4_1_keys.append(key)

	textInfo4_1.set(str(list_Info4_1_keys))

def getListInfo4_1():
	global list_Info4_1_values
	for key in list_Info4_1_keys:
		list_Info4_1_values.append(data["Info4"]["Info4.1"][key])

	combobox_Info4_1['values'] = list_Info4_1_values
	combobox_Info4_1['state'] = 'readonly'
	combobox_Info4_1.pack()
	combobox_Info4_1.set(data["Info4"]["Info4.1"][list_Info4_1_keys[0]])

############################################################################


# open button
button_openfile = tk.Button(root,text='Open a File',command=select_file)
button_openfile.pack()

textfilename = tk.StringVar()
textfilename.set("No file choosen")
label_filename = tk.Label(root,textvariable=textfilename)
label_filename.pack()

button_displayData = tk.Button(root,text="Display data",command=displayData)
button_displayData.pack()

textdata = tk.StringVar()
textdata.set("No data")
label_data = tk.Label(root,textvariable=textdata)
label_data.pack()

button_getInfo1 = tk.Button(root,text="Get info 1",command=getInfo1)
button_getInfo1.pack()

textInfo1 = tk.StringVar()
textInfo1.set("No data")
label_Info1= tk.Label(root,textvariable=textInfo1)
label_Info1.pack()

button_getInfo4_1 = tk.Button(root,text="Get info 4.1",command=getInfo4_1)
button_getInfo4_1.pack()

textInfo4_1 = tk.StringVar()
textInfo4_1.set("No data")
label_Info4_1= tk.Label(root,textvariable=textInfo4_1)
label_Info4_1.pack()

button_getListInfo4_1 = tk.Button(root,text="Get info 4.1",command=getListInfo4_1)
button_getListInfo4_1.pack()

listInfo4_1 = tk.StringVar()
combobox_Info4_1= ttk.Combobox(root,textvariable=listInfo4_1)
combobox_Info4_1.pack()

# run the application
root.mainloop()
