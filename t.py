from tkinter import ttk
from tkinter import *
from time import sleep
from tkinter.filedialog import *



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

root.title(program_name)

def ft_add_file_button():
	print(askopenfilename(title="open file"))

add_file_button = Button(root, text="+", font=("Arial", 45, "bold"), width=7, height=4, command=ft_add_file_button)
add_file_button.place(relx=0.5, rely=0.5, anchor=CENTER)

go_button = Button(root, text="Go", font=("Arial", 16, "bold"), width=7, height=4)
go_button.place(relx=1.0, rely=0.0, anchor=NE, x=-5, y=5)

types = "json", "csv", "exel", "sql"
types_file_replace = ttk.Combobox(root, values=types, state='readonly', width=10, font=("Arial", 22))
types_file_replace.set("slect type")
types_file_replace.bind("<<ComboboxSelected>>", lambda arg: print(types_file_replace.get()))
types_file_replace.place(relx=0.0, rely=0.0, anchor=NW, x=5, y=5)

types = "auto detect", "json", "csv", "exel", "sql"
types_file_entry = ttk.Combobox(root, values=types, state='readonly', width=15, font=("Arial", 22))
types_file_entry.set(types[0])
types_file_entry.bind("<<ComboboxSelected>>", lambda arg: print(types_file_entry.get()))
types_file_entry.place(relx=0.5, rely=0.72, anchor=CENTER)


def ft_path_file_replace():
	print(asksaveasfilename(title="save as"))


path_file_replace = Button(root, text="...", font=("Arial", 16), command=ft_path_file_replace)
path_file_replace.place(relx=0.0, rely=1.0, anchor=SW, x=5, y=-5)

root.mainloop()
