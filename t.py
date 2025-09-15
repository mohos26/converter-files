from tkinter import *
from tkinter import ttk
from time import sleep
from tkinter.filedialog import *
from data import *

# init

program_name = "converter_files"

root = Tk()

window_width = 700
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.minsize(window_width, window_height)
root.maxsize(window_width, window_height)

root.title(program_name)

# add file

path = ""

def ft_add_file_button():
	global path
	path = askopenfilename(title="open file")
label_1 = Label(root, text="select your file", font=("Arial", 12))
label_1.place(relx=0.5, rely=0.3, anchor=CENTER)
add_file_button = Button(root, text="+", font=("Arial", 45, "bold"), width=7, height=4, command=ft_add_file_button)
add_file_button.place(relx=0.5, rely=0.5, anchor=CENTER)


# select type

types = "Json", "Csv", "Excel", "Sql"
types_file_replace = ttk.Combobox(root, values=types, state='readonly', width=10, font=("Arial", 22))
types_file_replace.set("select type")
types_file_replace.bind("<<ComboboxSelected>>", lambda arg: print(types_file_replace.get()))
types_file_replace.place(relx=0.0, rely=0.0, anchor=NW, x=5, y=5)

# select type of file input

types = "auto-detect", "json", "csv", "excel", "sql", "xml", "txt"
types_file_entry = ttk.Combobox(root, values=types, state='readonly', width=15, font=("Arial", 22))
types_file_entry.set(types[0])
types_file_entry.bind("<<ComboboxSelected>>", lambda arg: print(types_file_entry.get()))
types_file_entry.place(relx=0.5, rely=0.72, anchor=CENTER)

# convert

def ft_go_button():
	global path, types_file_replace, types_file_entry, types
	if not path:
		print("Error: 1")
		return
	if types_file_replace.get() == "select type":
		print("Error: 2")
		return
	name_of_converted = asksaveasfilename(title="save as")
	if not name_of_converted:
		print("Error: 3")
		return
	type_entered = types_file_entry.get()
	# if type_entered == types[0]:
	# 	type_entered = get_type(path)
	print(type_entered, types_file_replace.get(), path, name_of_converted)
	convert(type_entered, types_file_replace.get().lower(), path, name_of_converted)
	print("Succesful")

label_2 = Label(root, text="type to convert", font=("Arial", 12))
label_2.place(relx=0.985, rely=0.135, anchor=NE, x=-5, y=5)
go_button = Button(root, text="Go", font=("Arial", 16, "bold"), width=7, height=4, command=ft_go_button)
go_button.place(relx=1.0, rely=0.0, anchor=NE, x=-5, y=5)

# loop

root.mainloop()
