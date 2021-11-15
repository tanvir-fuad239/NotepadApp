# Home page window starts

from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter.messagebox as msg
import time
from tkinter import filedialog
from tkinter import colorchooser
import os

home_page_window = Tk()
home_page_window.title("Home page")
home_page_window.geometry("770x530")
home_page_window.wm_iconbitmap("Home icon.ico")

image_for_home_page=Image.open("home page.jpg")
photo=ImageTk.PhotoImage(image_for_home_page)

picture_label=Label(image=photo)
picture_label.place(x=0,y=0)

def button():
    if username_value.get() == "AAAM" and password_value.get() == "Notepad 3.9.5":

        loading_label = Label(home_page_window, text="Loading.......", font="comicsansms 13 bold")
        loading_label.grid(row=6, column=2)
        percentage_label = Label(home_page_window, text="", font="comicsansms 13 bold")
        percentage_label.grid(row=7, column=2, pady=10)
        progressbar = ttk.Progressbar(home_page_window, orient=HORIZONTAL, length=280, mode="determinate")
        progressbar.grid(row=8, column=2)

        for i in range(1, 100):
            progressbar['value'] = i
            progressbar.update_idletasks()
            percentage_label.configure(text=f"{str(i)}%")
            time.sleep(0.04)

        # Home page window exit here
        home_page_window.destroy()

        # Notepad window starts

        notepad_window = Tk()
        notepad_window.title("Untitled -Notepad")
        notepad_window.geometry("890x590")
        notepad_window.wm_iconbitmap("title bar.ico")

        def new_file():
            text_area.delete(1.0, END)
            notepad_window.title("New file -Notepad")

        def open_file():
            text_area.delete(1.0, END)
            file = filedialog.askopenfilename(defaultextension=".txt", title="Open file",
                                              filetypes=(
                                              ("Text files", "*.txt"), ("All files", "*.*"), ("python file", "*.py")))
            notepad_window.title(os.path.basename(file))

            with open(file, "r") as f:
                text_area.insert(1.0, f.read())

        def save_file():
            file = filedialog.asksaveasfilename(initialfile="Untitled.txt", title="Save file",
                                                filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
            with open(file, "w") as f:
                f.write(text_area.get(1.0, END))

        def exit_file():
            notepad_window.destroy()

        def cut():
            text_area.event_generate('<<Cut>>')

        def copy():
            text_area.event_generate('<<Copy>>')

        def paste():
            text_area.event_generate('<<Paste>>')

        def delete():
            text_area.delete(1.0, END)
            notepad_window.title("Untitled -Notepad")

        def font_8():
            text_area.configure(font=f"velvetica {l[0]}")

        def font_9():
            text_area.configure(font=f"velvetica {l[1]}")

        def font_10():
            text_area.configure(font=f"velvetica {l[2]}")

        def font_11():
            text_area.configure(font=f"velvetica {l[3]}")

        def font_12():
            text_area.configure(font=f"velvetica {l[4]}")

        def font_13():
            text_area.configure(font=f"velvetica {l[5]}")

        def font_14():
            text_area.configure(font=f"velvetica {l[6]}")

        def font_15():
            text_area.configure(font=f"velvetica {l[7]}")

        def color():
            c = colorchooser.askcolor()[1]
            text_area.configure(background=c)

        def zoom_in():
            text_area.configure(font=f"velvetica {l[8]}")

        def zoom_out():
            text_area.configure(font=f"velvetica {l[9]}")

        def default_view():

            text_area.configure(font=f"velvetica {l[2]}")

        def about():
            msg.showinfo("Notepad", "This notepad is created by Ayesha,Aanan,Alid and Mahmuda")

        # Main function starts here
        if __name__ == '__main__':
            l = [8, 9, 10, 11, 12, 13, 14, 15, 24,7]

            # Text area and packing it
            text_area = Text(notepad_window, font="velvetica 10 ")
            text_area.pack(fill=BOTH, expand=True)

            # Creating a scrollbar and packing it
            scrollbar_y = Scrollbar(text_area)
            scrollbar_y.pack(side=RIGHT, fill=Y)
            scrollbar_y.config(command=text_area.yview)
            text_area.config(yscrollcommand=scrollbar_y.set)

            # Adding menubar
            main_menu = Menu(notepad_window)

            # File menu starts
            file_menu = Menu(main_menu, tearoff=False)
            file_menu.add_command(label="New", command=new_file)
            file_menu.add_separator()
            file_menu.add_command(label="Open", command=open_file)
            file_menu.add_separator()
            file_menu.add_command(label="Save", command=save_file)
            file_menu.add_separator()
            file_menu.add_command(label="Exit", command=exit_file)
            main_menu.add_cascade(label="File", menu=file_menu)
            # File menu ends

            # Edit menu starts
            edit_menu = Menu(main_menu, tearoff=False)
            edit_menu.add_command(label="Cut", command=cut)
            edit_menu.add_separator()
            edit_menu.add_command(label="Copy", command=copy)
            edit_menu.add_separator()
            edit_menu.add_command(label="Paste", command=paste)
            edit_menu.add_separator()
            edit_menu.add_command(label="Delete", command=delete)
            main_menu.add_cascade(label="Edit", menu=edit_menu)

            # Edit menu ends

            # Font size menu starts

            font_size_menu = Menu(main_menu, tearoff=False)
            font_size_menu.add_command(label="8", command=font_8)
            font_size_menu.add_separator()
            font_size_menu.add_command(label="9", command=font_9)
            font_size_menu.add_separator()
            font_size_menu.add_command(label="10", command=font_10)
            font_size_menu.add_separator()
            font_size_menu.add_command(label="11", command=font_11)
            font_size_menu.add_separator()
            font_size_menu.add_command(label="12", command=font_12)
            font_size_menu.add_separator()
            font_size_menu.add_command(label="13", command=font_13)
            font_size_menu.add_separator()
            font_size_menu.add_command(label="14", command=font_14)
            font_size_menu.add_separator()
            font_size_menu.add_command(label="15", command=font_15)
            main_menu.add_cascade(label="Font size", menu=font_size_menu)

            # Font size menu ends

            # Background menu starts

            background_menu = Menu(main_menu, tearoff=False)
            background_menu.add_command(label="Pick a color", command=color)
            main_menu.add_cascade(label="Background", menu=background_menu)

            # Background ends

            # View menu starts

            view_menu = Menu(main_menu, tearoff=False)
            zoom_menu = Menu(view_menu, tearoff=False)
            zoom_menu.add_command(label="Zoom in", command=zoom_in)
            zoom_menu.add_separator()
            zoom_menu.add_command(label="Zoom out", command=zoom_out)
            zoom_menu.add_separator()
            zoom_menu.add_command(label="Default view", command=default_view)
            view_menu.add_cascade(label="Zoom", menu=zoom_menu)
            main_menu.add_cascade(label="View", menu=view_menu)

            # View menu ends

            # Help menu starts

            help_menu = Menu(main_menu, tearoff=False)
            help_menu.add_command(label="About Notepad", command=about)
            main_menu.add_cascade(label="Help", menu=help_menu)

            # Help menu ends

            notepad_window.config(menu=main_menu)

            # Menubar ends here

            notepad_window.mainloop()

            # Notepad window ends here

    else:
        if username_value.get() != "AAAM" and password_value.get() == "Notepad 3.9.5":

            msg.showinfo("Error","Wrong username")

        elif username_value.get() == "AAAM" and password_value.get() != "Notepad 3.9.5":

            msg.showinfo("Error", "Wrong password")
        else:
            msg.showinfo("Error", "Wrong information")


# Creating a heading and packing it

heading = Label(home_page_window,text="Welcome to Notepad",font="comicsansms 18 italic")
heading.grid(row=0, column=2, pady=30, padx=30)

# Creating labels and packing it

username = Label(home_page_window, text="Username", font="Comicsansms 13 bold")
password = Label(home_page_window, text="Password", font="Comicsansms 13 bold")
username.grid(row=1, column=0, padx=10, pady=10)
password.grid(row=2, column=0, padx=3)

username_value = StringVar()
password_value = StringVar()

username_entry = Entry(home_page_window, textvariable=username_value)
password_entry = Entry(home_page_window, textvariable=password_value)

username_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)

# Creating a enter button and packing it

enter_button = Button(home_page_window, text="Enter", font="Comicsansms 13 bold", command=button)
enter_button.grid(row=5, column=0, pady=20)

home_page_window.mainloop()

# Home page window ends