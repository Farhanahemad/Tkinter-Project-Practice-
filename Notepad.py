from tkinter import *
import tkinter.messagebox  as msg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root = Tk()
root.geometry("900x600+0+0")
file=None
root.title("Untitle FL-Notepad")
def nFile():
    global file
    root.title("Untitle FL-Notepad")
    file = None
    Textarea.delete(1.0,END)
def oFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+ "- FL Notepad")
        Textarea.delete(1.0,END)
        f = open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close()
def sFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file =None
        else :
            f = open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+ "- FL Notepad")
    else:
        f = open(file,"w")
        f.write(Textarea.get(1.0,END))
        f.close()
        root.title(os.path.basename(file)+ "- FL Notepad")

def cut():
    Textarea.event_generate(("<<Cut>>"))
def copy():
    Textarea.event_generate(("<<Copy>>"))
def paste():
    Textarea.event_generate(("<<Paste>>"))
def Help():
    msg.showinfo("help","We will reach at u Soon!")
def About():
    msg.showinfo("FL Notepad","Hey Guys,\nHere is Farhanahemad Loladiya and you using FL Notepad")
Textarea= Text(root,font="cambria 20 bold italic")
Textarea.pack(expand=True,fill=BOTH)

Menubar = Menu(root)
m1 = Menu(Menubar,tearoff=0)
m1.add_command(label="New File",command=nFile)
m1.add_command(label="Open",command=oFile)
m1.add_command(label="Save",command=sFile)
Menubar.add_cascade(label="File",menu=m1)

m2 = Menu(Menubar,tearoff=0)
m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy",command=copy)
m2.add_command(label="Paste",command=paste)
Menubar.add_cascade(label="Edit",menu=m2)

m3 = Menu(Menubar,tearoff=0)
m3.add_command(label="About",command=About)
m3.add_command(label="Help",command=Help)
Menubar.add_cascade(label="Help",menu=m3)



root.config(menu = Menubar)




root.mainloop()