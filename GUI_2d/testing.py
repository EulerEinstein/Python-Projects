import yaml
from yaml.loader import SafeLoader

newdict = {}
lists = []

def recursive_items(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, __builtins__.dict):
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)

def list_every_dictionary_items(dictionary):
    newdict = {}
    for key, value in recursive_items(dictionary):
        #print(key, value)
        newdict[key] = value

    return newdict

def get_list_keys(dictionary):
    lists = []
    for key in dictionary.keys():
        lists.append(key)

    return lists

# Open the file and load the file
with open('Desktop/testing/GUI_2d/data_sample.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    newdict = list_every_dictionary_items(data)
    lists = get_list_keys(newdict)
    print(lists)



import tkinter as tk
from tkinter import Button, ttk

def get_the_keys_from_combobox():
    for key,value in newdict.items():
        if key == key_dictionary_choosen.get():
            msg.configure(text=str(key) + ": " + str(value))

# Creating tkinter window
window = tk.Tk()
window.geometry('850x550')
# Label
ttk.Label(window, text = "Select the data :", 
        font = ("Times New Roman", 10)).grid(column = 0, 
        row = 0, padx = 10, pady = 25)
  
key_dictionary_choosen = ttk.Combobox(window, width = 27, 
                            state="readonly")
  
# Adding combobox drop down list
key_dictionary_choosen['values'] = lists
key_dictionary_choosen.grid(column = 1, row = 0)
# Shows as a default value
key_dictionary_choosen.current(1) 

btn = ttk.Button(window, text="Show data",command=get_the_keys_from_combobox)
btn.grid(column = 2, row = 0)

msg = tk.Message(window, text="None")      
msg.grid(column = 3, row = 0)

for i in range(1,5):
    btn = ttk.Button(window, text="Button"+str(i))
    btn.grid(column = i, row = 1)

window.mainloop()