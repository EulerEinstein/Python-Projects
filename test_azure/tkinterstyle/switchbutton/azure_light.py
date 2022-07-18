from tkinter import ttk
from PIL import Image, ImageTk
import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def configure_style(s):
	s.configure(".",
				background="#ffffff",
				foreground="#000000",
				troughcolor="#ffffff",
				focuscolor="#ffffff",
				selectbackground="#ffffff",
				selectforeground="#ffffff",
				insertcolor="#000000",
				insertwidth=1,
				fieldbackground="#007fff",
				font=("Segoi Ui",10),
				borderwidth=1,
				relief="flat"
			   )

def style_switch(s):

	global off_basic,on_basic,on_accent,off_hover,on_hover

	loc_off_basic = resource_path("off-basic.png")

	off_basic = Image.open('off-basic.png')
	on_basic = Image.open('on-basic.png')
	on_accent = Image.open('on-accent.png')
	off_hover = Image.open('off-hover.png')
	on_hover = Image.open('on-hover.png')

	off_basic = off_basic.resize((40,20))
	on_basic = on_basic.resize((40,20))
	on_accent = on_accent.resize((40,20))
	off_hover = off_hover.resize((40,20))
	on_hover = on_hover.resize((40,20))

	off_basic = ImageTk.PhotoImage(off_basic)
	on_basic = ImageTk.PhotoImage(on_basic)
	on_accent = ImageTk.PhotoImage(on_accent)
	off_hover = ImageTk.PhotoImage(off_hover)
	on_hover = ImageTk.PhotoImage(on_hover)

	s.element_create("Switch.indicator","image", off_basic, ("selected disabled",on_basic),("disabled",off_basic),("pressed selected",on_hover),("active selected",on_hover),("selected",on_accent),("pressed !selected",off_hover),("active",off_hover),width=46,sticky="w")
	print(s.layout('Switch.TCheckbutton', 
					[("Switch.button",
					 {"children":[("Switch.padding",
					 	          {"children":[("Switch.indicator",
					 	          	            {"side":"left"}),
					 	                       ("Switch.label",
					 	                       	{"side":"right","expand":True})
					 	                      ]
								  }
								 )]
					 }
					)],
				  )
		 )

