
from tkinter import *
root = Tk()
root.geometry("370x500+0+0")
root.title("FL CALC")
def clicked(event):
    text = event.widget.cget("text")
    if text == "CE":
        entryValue.set("")
        return 0
        
    if text == "=":
        try:
            val = eval(entryValue.get())
            entryValue.set(val)
            return 0
        except Exception as e:
            entryValue.set("ERROR")
            print(e)
            return 0
            
    if text == "X":
        text = "*"
    entryValue.set(entryValue.get()+text)
entryValue=StringVar()
e1 = Entry(textvariable=entryValue,font="cambria 30 bold italic",)
e1.pack(fill=X,padx=10,pady=10)

f1=Frame(root)
f1.pack(fill=X,padx=10)

l1=Label(f1,text="9",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=25,pady=10)
l1.bind("<Button-1>",clicked)
l1.grid(row=0,column=0)
l2=Label(f1,text="8",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=25,pady=10)
l2.bind("<Button-1>",clicked)
l2.grid(row=0,column=1)
l3=Label(f1,text="7",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=25,pady=10)
l3.bind("<Button-1>",clicked)
l3.grid(row=0,column=2)
l4=Label(f1,text="/",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=25,pady=10)
l4.bind("<Button-1>",clicked)
l4.grid(row=0,column=3)

f2=Frame(root)
f2.pack(fill=X,padx=10)

l5=Label(f2,text="6",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=25,pady=10)
l5.bind("<Button-1>",clicked)
l5.grid(row=0,column=0)
l6=Label(f2,text="5",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=25,pady=10)
l6.bind("<Button-1>",clicked)
l6.grid(row=0,column=1)
l7=Label(f2,text="4",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=25,pady=10)
l7.bind("<Button-1>",clicked)
l7.grid(row=0,column=2)
l8=Label(f2,text="X",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=25,pady=10)
l8.bind("<Button-1>",clicked)
l8.grid(row=0,column=3)

f3=Frame(root)
f3.pack(fill=X,padx=10)

l9=Label(f3,text="3",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=25,pady=10)
l9.bind("<Button-1>",clicked)
l9.grid(row=0,column=0)
l10=Label(f3,text="2",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=25,pady=10)
l10.bind("<Button-1>",clicked)
l10.grid(row=0,column=1)
l11=Label(f3,text="1",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=25,pady=10)
l11.bind("<Button-1>",clicked)
l11.grid(row=0,column=2)
l12=Label(f3,text="-",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=25,pady=10)
l12.bind("<Button-1>",clicked)
l12.grid(row=0,column=3)

f4=Frame(root)
f4.pack(fill=X,padx=10)
l14=Label(f4,text="0",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=45,pady=10)
l14.bind("<Button-1>",clicked)
l14.grid(row=0,column=0)
l15=Label(f4,text=".",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=45,pady=10)
l15.bind("<Button-1>",clicked)
l15.grid(row=0,column=2)
l17=Label(f4,text="+",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=30,pady=10)
l17.bind("<Button-1>",clicked)
l17.grid(row=0,column=3)

f5=Frame(root)
f5.pack(fill=X,padx=10)
l13=Label(f5,text="CE",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=59,pady=10)
l13.bind("<Button-1>",clicked)
l13.grid(row=0,columnspan=2,column=0)
l16=Label(f5,text="=",relief=SUNKEN,borderwidth=7,font="cambria 30 bold",padx=61,pady=10)
l16.bind("<Button-1>",clicked)
l16.grid(row=0,columnspan=2,column=3)

root.mainloop()