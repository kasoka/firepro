from tkinter import *
app=Tk()
app.state("zoomed")
app.title("FIREPRO  REGISTER")
app.configure(bg="skyblue")
import importlib
import fileinput
import os
if not os.path.isfile('data.py'):
    with open('data.py','w') as d:
        d.write('windows=0')
        d.write('\nlinux=0')
global data
import data
from tkinter import messagebox
b1=Button()
b2=Button()
b3=Button()
l1=Label()
l2=Label()
l3=Label()
l4=Label()
fx=Frame(bg="skyblue")
e1=Entry()
var=StringVar()
var2=StringVar()
var3=StringVar()
#globals
global pid
pid=0
global windows
windows=data.windows
global linux
linux=data.linux
var.set("Windows users : "+str(windows))
var3.set("Linux users : "+str(linux))
var2.set("The registration code is : 0")
def dummy():
    1+1
def calculate_event(event):
    calculate()
def calculate():
    len1=e1.get()
    print(len(len1))
    l=0
    if len(len1)>0 and len(len1)<=3:
        l=1
    while l==1:
        try:
            global pid
            pid=int(e1.get())
            if pid>0:
                code=((pid+4568)*pid)+(pid+76548)
                b1.configure(text="ADD",command=add)
            else:
                code=0
            var2.set("The registration code is : "+str(code))
            l=0
            break
        except:
            l=0
            messagebox.showerror("failed","you did not enter an interger")
def home():
    f1=Frame(fx,bg="skyblue")
    f2=Frame(fx,bg="skyblue")
    f3=Frame(fx,bg="skyblue")
    e1.focus()
    app.bind("<Return>",calculate_event)
    l1.configure(text="FIREPRO REGISTER",font=(app,"55","underline"),bg="skyblue")
    l2.configure(text="Enter  product ID below",font=(app,"25"),bg="skyblue")
    e1.configure(justify="center",font=(app,"25"))
    b3=Button(f3,text="CALCULATE",font=(app,"20"),width=12,command=calculate,fg="white",bg="purple")
    global b1
    b1=Button(f3,text="",font=(app,"20"),command=dummy,width=12,fg="white",bg="purple")
    b2=Button(f1,text="REMOVE",font=(app,"20"),command=remove_windows,width="10",fg="white",bg="purple")
    b4=Button(f2,text="REMOVE",font=(app,"20"),command=remove_linux,width="10",fg="white",bg="purple")
    
    l3=Label(f1,textvariable=var,font=(app,"30"),bg="skyblue",width=20)
    l5=Label(f2,textvariable=var3,font=(app,"30"),bg="skyblue",width=20)
    l4.configure(textvariable=var2,font=(app,"25"),bg="skyblue")
    l1.pack(pady="20")
    l2.pack(pady="10")
    e1.pack(pady="10")
    b3.pack(side="left",pady="10")
    b1.pack(side="left",padx="20",pady=20)
    f3.pack()
    l4.pack(pady="10")
    l3.pack(side="left",pady=10)
    b2.pack(side="right",padx="20")
    l5.pack(side="left",pady=10)
    b4.pack(side="right",padx="20")
    
    f1.pack()
    f2.pack()
    fx.pack(pady="30")
    
    
def add():
    if pid>=100 and pid<=999:
        global windows
        windows=windows+1
        with open("data.py","w") as d:
            d.write("windows="+str(windows))
            d.write("\nlinux="+str(linux))
        var.set("Windows users : "+str(windows))
    if pid>=1 and pid<=99:
        global linux
        linux=linux+1
        with open("data.py","w") as d:
            d.write("windows="+str(windows))
            d.write("\nlinux="+str(linux))
        var3.set("Linux users : "+str(linux))
    b1.configure(text="",command=dummy)
    global data
    importlib.reload(data)
def remove_windows():
    global windows
    windows=windows-1
    if windows<0:
        global windows
        windows=0
    with open("data.py","w") as d:
        d.write("windows="+str(windows))
        d.write("\nlinux="+str(linux))
    var.set("Windows users : "+str(windows))
    global data
    importlib.reload(data)
def remove_linux():
    global linux
    linux=linux-1
    if linux<0:
        global linux
        linux=0
    with open("data.py","w") as d:
        d.write("linux="+str(linux))
        d.write("\nwindows="+str(windows))
    var3.set("Linux users : "+str(linux))
    global data
    importlib.reload(data)





home()
app.mainloop()
