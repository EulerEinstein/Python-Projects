from tkinter import *
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from azure_light import *


root = Tk()
root.configure(background='white')

s = ttk.Style()
# print(s.theme_names())
# print(s.theme_use())

configure_style(s)
style_switch(s)


var1 = tk.IntVar(value=1)
var2 = tk.IntVar(value=0)
switch_checkbutton = ttk.Checkbutton(root,text="Display length", style="Switch.TCheckbutton")
switch_checkbutton.pack(padx=20, pady=10)


root.mainloop()