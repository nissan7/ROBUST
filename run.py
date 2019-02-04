from tkinter import *
import tkinter.ttk as ttk
import methods as fun




class tool:
    initialiser=fun.initialiser
    addfile=fun.addfile
    addlogin=fun.addlogin
    toggled2u=fun.toggled2u
    toggleu2d=fun.toggleu2d
    validate=fun.validate
    logout=fun.logout
    browse=fun.browse
    upload=fun.upload
    daction=fun.daction
    download=fun.download
    setrem=fun.setrem
    frefresh=fun.frefresh
    _0=fun._0
    _1=fun._1
    _2=fun._2
    _3=fun._3
    def __init__(self, master):
        
        self.myfiles=[]
        self.fpath=""
        self.mode=0
        self.rem=0
        file=open("address.txt","r").read()
        file=file.split("\n")
        self.ip=file[0]
        self.port=int(file[1])
        self.master = master
        self.master.geometry("805x418+240+68")
        self.master.title("ROBUST TOOL")
        self.master.configure(background="#d9d9d9")
        self.master.configure(highlightbackground="#d9d9d9")
        self.master.configure(highlightcolor="black")
        self.addlogin()
        

        

        
root = Tk()
my_gui = tool(root)
root.mainloop()
