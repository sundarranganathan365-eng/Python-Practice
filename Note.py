#Import Tkinter for creating GUI apps 
import tkinter as tk
from tkinter import filedialog,messagebox

#Code for creating Text  mainwindow

root = tk.Tk()
root.title(" Simple Text Eidtor")
root.geometry("800x600")

#create text area 

text =tk.Text(
        root,
        wrap=tk.WORD,# make the words readbale  like at the end it will wrp the words
        font = ("Helvetica",22)
    )


text.pack(expand = True,fill=tk.BOTH) #giving access to write the code all over area 

#main logic 

def new_file ():
    text.delete(1.0, tk.END) # to create a new file

def open_file ():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )
    if file_path:
        with open (file_path,"r") as file :
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read())

def save_file ():
    file_path = filedialog.asksaveasfilename(
        filetypes=[("Text Files","*.txt")]
    )
    
    if file_path:
        with open (file_path,"w") as file :
            file.write(text.get(1.0,tk.END))

    messagebox.showinfo("Info","File Save Successfully")
#menu bar
menu = tk.Menu(root)
root.config(menu=menu)
file_menu =tk.Menu(menu)

menu.add_cascade(label="File",menu=file_menu)#add file menu on menu bar

#showing the options after clicking the file option on UI 
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator() #creating the box to seprate the options
file_menu.add_command(label="Exit",command=root.quit)



#starts and keep teh window open 
root.mainloop()

