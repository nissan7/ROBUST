from tkinter import *
import socket
import pickle
from tkinter import filedialog
import os

class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=3, highlightthickness=3,
                        yscrollcommand=vscrollbar.set)
        canvas.configure(height=200)
        #canvas.configure(relief='raised')
        
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)



def addlogin(self):
       
    self.logframe = Frame(self.master)
    self.logframe.place(relx=0.01, rely=0.024, relheight=0.959
            , relwidth=0.978)
    self.logframe.configure(relief='ridge')
    self.logframe.configure(borderwidth="2")
    self.logframe.configure(relief='ridge')
    self.logframe.configure(background="#8fa2d8")
    self.logframe.configure(width=785)

    self.msgcan = Canvas(self.logframe)
    self.msgcan.place(relx=0.216, rely=0.636, relheight=0.307
            , relwidth=0.629)
    self.msgcan.configure(background="#d9d9d9")
    self.msgcan.configure(borderwidth="2")
    self.msgcan.configure(insertbackground="black")
    self.msgcan.configure(relief='ridge')
    self.msgcan.configure(selectbackground="#c4c4c4")
    self.msgcan.configure(selectforeground="black")
    self.msgcan.configure(width=493)

    self.Entryl = Entry(self.logframe)
    self.Entryl.place(relx=0.451, rely=0.125,height=30, relwidth=0.247)
    self.Entryl.configure(background="white")
    self.Entryl.configure(disabledforeground="#a3a3a3")

    self.Entryl.configure(foreground="#000000")
    self.Entryl.configure(insertbackground="black")
    self.Entryl.configure(selectborderwidth="3")
    self.Entryl.configure(selectforeground="#e4c4ff")
    self.Entryl.configure(width=194)

    self.Entryp = Entry(self.logframe,show="*")
    self.Entryp.place(relx=0.451, rely=0.249,height=30, relwidth=0.247)
    self.Entryp.configure(background="white")
    self.Entryp.configure(disabledforeground="#a3a3a3")
    self.Entryp.configure(font="TkFixedFont")
    self.Entryp.configure(foreground="#000000")
    self.Entryp.configure(insertbackground="black")
    self.Entryp.configure(width=194)
    

    self.loginbtn = Button(self.logframe)
    self.loginbtn.place(relx=0.452, rely=0.411, height=34, width=67)
    self.loginbtn.configure(activebackground="#ececec")
    self.loginbtn.configure(activeforeground="#000000")
    self.loginbtn.configure(background="#d9d9d9")
    self.loginbtn.configure(disabledforeground="#a3a3a3")
    self.loginbtn.configure(foreground="#000000")
    self.loginbtn.configure(highlightbackground="#d9d9d9")
    self.loginbtn.configure(highlightcolor="black")
    self.loginbtn.configure(pady="0")
    self.loginbtn.configure(text='''LOGIN''')
    self.loginbtn.configure(width=67)
    self.loginbtn.bind('<Button-1>',self.validate)

    self.luser = Label(self.logframe)
    self.luser.place(relx=0.28, rely=0.125, height=31, width=114)
    self.luser.configure(background="#d9d9d9")
    self.luser.configure(disabledforeground="#a3a3a3")
    self.luser.configure(foreground="#000000")
    self.luser.configure(text='''User ID''')
    self.luser.configure(width=114)

    self.lpass = Label(self.logframe)
    self.lpass.place(relx=0.28, rely=0.249, height=31, width=114)
    self.lpass.configure(background="#d9d9d9")
    self.lpass.configure(disabledforeground="#a3a3a3")
    self.lpass.configure(foreground="#000000")
    self.lpass.configure(text='''Password''')
    self.lpass.configure(width=114)

    self.remradio = Checkbutton(self.logframe, text='''Remember this user ID''',command=self.setrem)
    self.remradio.place(relx=0.452, rely=0.337, relheight=0.062
            , relwidth=0.245)
    self.remradio.configure(justify='left')
    self.remradio.configure(text='''Remember this user ID''')
    self.remradio.configure(width=198)



def initialiser(self):

    self.Aframe = Frame(self.master)
    self.Aframe.place(relx=0.186, rely=0.012, relheight=0.981
                        , relwidth=0.807)
    self.Aframe.configure(relief='ridge')
    self.Aframe.configure(borderwidth="3")
    self.Aframe.configure(relief='ridge')
    self.Aframe.configure(background="#d9d9d9")
    self.Aframe.configure(highlightbackground="#d9d9d9")
    self.Aframe.configure(highlightcolor="black")
    self.Aframe.configure(width=645)
    
    self.Tframe = Frame(self.master)
    self.Tframe.place(relx=0.0, rely=0.012, relheight=0.981, relwidth=0.18)
    self.Tframe.configure(relief='ridge')
    self.Tframe.configure(borderwidth="3")
    self.Tframe.configure(relief='ridge')
    self.Tframe.configure(background="#d8d3bc")
    self.Tframe.configure(highlightbackground="#d9d9d9")
    self.Tframe.configure(highlightcolor="black")
    self.Tframe.configure(width=145)

    self.Nfilebtn = Button(self.Tframe)
    self.Nfilebtn.place(relx=0.034, rely=0.024, height=34, width=127)
    self.Nfilebtn.configure(activebackground="#ececec")
    self.Nfilebtn.configure(activeforeground="#000000")
    self.Nfilebtn.configure(background="#d9d9d9")
    self.Nfilebtn.configure(cursor="hand2")
    self.Nfilebtn.configure(disabledforeground="#a3a3a3")
    self.Nfilebtn.configure(foreground="#000000")
    self.Nfilebtn.configure(highlightbackground="#d9d9d9")
    self.Nfilebtn.configure(highlightcolor="black")
    self.Nfilebtn.configure(pady="0")
    self.Nfilebtn.configure(text='''FILE SHARING''')
    

    self.Nlogoutbtb = Button(self.Tframe)
    self.Nlogoutbtb.place(relx=0.552, rely=0.902, height=34, width=57)
    self.Nlogoutbtb.configure(activebackground="#ececec")
    self.Nlogoutbtb.configure(activeforeground="#000000")
    self.Nlogoutbtb.configure(background="#d9d9d9")
    self.Nlogoutbtb.configure(cursor="hand2")
    self.Nlogoutbtb.configure(disabledforeground="#a3a3a3")
    self.Nlogoutbtb.configure(foreground="#000000")
    self.Nlogoutbtb.configure(highlightbackground="#d9d9d9")
    self.Nlogoutbtb.configure(highlightcolor="black")
    self.Nlogoutbtb.configure(pady="0")
    self.Nlogoutbtb.configure(text='''LOG OUT''')
    self.Nlogoutbtb.bind('<Button-1>',self.logout)

    self.userlabel = Label(self.Tframe)
    self.userlabel.place(relx=0.069, rely=0.902, height=31, width=64)
    self.userlabel.configure(activebackground="#f9f9f9")
    self.userlabel.configure(activeforeground="black")
    self.userlabel.configure(background="#d9d9d9")
    self.userlabel.configure(disabledforeground="#a3a3a3")
    self.userlabel.configure(foreground="#000000")
    self.userlabel.configure(highlightbackground="#d9d9d9")
    self.userlabel.configure(highlightcolor="black")
    self.userlabel.configure(text=self.user)

def addfile(self):
    self.tdownbtn =Button(self.Aframe)
    self.tdownbtn.place(relx=0.138, rely=0.012, height=24, width=77)
    self.tdownbtn.configure(activebackground="#ececec")
    self.tdownbtn.configure(activeforeground="#000000")
    self.tdownbtn.configure(background="#d9d9d9")
    self.tdownbtn.configure(disabledforeground="#a3a3a3")
    self.tdownbtn.configure(foreground="#000000")
    self.tdownbtn.configure(highlightbackground="#d9d9d9")
    self.tdownbtn.configure(highlightcolor="black")
    self.tdownbtn.configure(pady="0")
    self.tdownbtn.configure(text='''DOWNLOAD''')
    self.tdownbtn.configure(width=77)
    self.tdownbtn.configure(cursor="hand2")
    self.tdownbtn.bind('<Button-1>',self.toggleu2d)
    

    self.tupbtn = Button(self.Aframe)
    self.tupbtn.place(relx=0.277, rely=0.012, height=24, width=57)
    self.tupbtn.configure(activebackground="#ececec")
    self.tupbtn.configure(activeforeground="#000000")
    self.tupbtn.configure(background="#d9d9d9")
    self.tupbtn.configure(disabledforeground="#a3a3a3")
    self.tupbtn.configure(foreground="#000000")
    self.tupbtn.configure(highlightbackground="#d9d9d9")
    self.tupbtn.configure(highlightcolor="black")
    self.tupbtn.configure(pady="0")
    self.tupbtn.configure(text='''UPLOAD''')
    self.tupbtn.configure(cursor="hand2")
    self.tupbtn.bind('<Button-1>',self.toggled2u)

    self.trefbtn = Button(self.Aframe)
    self.trefbtn.place(relx=0.38, rely=0.012, height=24, width=57)
    self.trefbtn.configure(activebackground="#ececec")
    self.trefbtn.configure(activeforeground="#000000")
    self.trefbtn.configure(background="#d9d9d9")
    self.trefbtn.configure(disabledforeground="#a3a3a3")
    self.trefbtn.configure(foreground="#000000")
    self.trefbtn.configure(highlightbackground="#d9d9d9")
    self.trefbtn.configure(highlightcolor="black")
    self.trefbtn.configure(pady="0")
    self.trefbtn.configure(text='''REFRESH''')
    self.trefbtn.configure(cursor="hand2")
    self.trefbtn.bind('<Button-1>',self.frefresh)
    
    self.Uframe = LabelFrame(self.Aframe)
    self.Uframe.place(relx=0.008, rely=0.073, relheight=0.902
            , relwidth=0.977)
    self.Uframe.configure(relief='groove')
    self.Uframe.configure(foreground="black")
    self.Uframe.configure(text='''UPLOAD''')
    self.Uframe.configure(background="#d9d9d9")
    self.Uframe.configure(highlightbackground="#d9d9d9")
    self.Uframe.configure(highlightcolor="black")
    self.Uframe.configure(width=630)
    
    self.forlbl = Label(self.Uframe)
    self.forlbl.place(relx=0.126, rely=0.081, height=31, width=78
            , bordermode='ignore')
    self.forlbl.configure(background="#d9d9d9")
    self.forlbl.configure(disabledforeground="#a3a3a3")
    self.forlbl.configure(foreground="#000000")
    self.forlbl.configure(text='''Upload for :''')
    self.forlbl.configure(width=78)

    self.Entryfor = Entry(self.Uframe)
    self.Entryfor.place(relx=0.252, rely=0.081, height=28, relwidth=0.26
            , bordermode='ignore')
    self.Entryfor.configure(background="white")
    self.Entryfor.configure(disabledforeground="#a3a3a3")
    self.Entryfor.configure(font="TkFixedFont")
    self.Entryfor.configure(foreground="#000000")
    self.Entryfor.configure(insertbackground="black")

    self.browserbtn = Button(self.Uframe)
    self.browserbtn.place(relx=0.583, rely=0.081, height=32, width=87
            , bordermode='ignore')
    self.browserbtn.configure(activebackground="#ececec")
    self.browserbtn.configure(activeforeground="#000000")
    self.browserbtn.configure(background="#d9d9d9")
    self.browserbtn.configure(disabledforeground="#a3a3a3")
    self.browserbtn.configure(foreground="#000000")
    self.browserbtn.configure(highlightbackground="#d9d9d9")
    self.browserbtn.configure(highlightcolor="black")
    self.browserbtn.configure(pady="0")
    self.browserbtn.configure(relief='sunken')
    self.browserbtn.configure(text='''Browse ...''')
    self.browserbtn.configure(width=87)
    self.browserbtn.bind('<Button-1>',self.browse)

    self.radnormal=Radiobutton(self.Uframe, text="NORMAL", variable=self.mode , value=0,command=self._0)
    self.radsign=Radiobutton(self.Uframe, text="SIGNED", variable=self.mode , value=1,command=self._1)
    self.radenc=Radiobutton(self.Uframe, text="ENCIPTED",variable=self.mode , value=2,command=self._2)
    self.radencsign=Radiobutton(self.Uframe, text="SIGNED AND ENCRIPTED",variable=self.mode , value=3,command=self._3)

    self.radnormal.select()

    self.radnormal.place(relx=0.157, rely=0.243, relheight=0.068
            , relwidth=0.107, bordermode='ignore')
    self.radnormal.configure(activebackground="#ececec")
    self.radnormal.configure(activeforeground="#000000")
    self.radnormal.configure(background="#d9d9d9")
    self.radnormal.configure(disabledforeground="#a3a3a3")
    self.radnormal.configure(foreground="#000000")
    self.radnormal.configure(highlightbackground="#d9d9d9")
    self.radnormal.configure(highlightcolor="black")
    self.radnormal.configure(justify='left')
    self.radnormal.configure(text='''Normal''')

    
    self.radenc.place(relx=0.15, rely=0.297, relheight=0.078, relwidth=0.112
            , bordermode='ignore')
    self.radenc.configure(activebackground="#ececec")
    self.radenc.configure(activeforeground="#000000")
    self.radenc.configure(background="#d9d9d9")
    self.radenc.configure(disabledforeground="#a3a3a3")
    self.radenc.configure(foreground="#000000")
    self.radenc.configure(highlightbackground="#d9d9d9")
    self.radenc.configure(highlightcolor="black")
    self.radenc.configure(justify='left')
    self.radenc.configure(text='''Encript''')

   
    self.radsign.place(relx=0.157, rely=0.365, relheight=0.068, relwidth=0.08
            , bordermode='ignore')
    self.radsign.configure(activebackground="#ececec")
    self.radsign.configure(activeforeground="#000000")
    self.radsign.configure(background="#d9d9d9")
    self.radsign.configure(disabledforeground="#a3a3a3")
    self.radsign.configure(foreground="#000000")
    self.radsign.configure(highlightbackground="#d9d9d9")
    self.radsign.configure(highlightcolor="black")
    self.radsign.configure(justify='left')
    self.radsign.configure(text='''Sign''')

  
    self.radencsign.place(relx=0.157, rely=0.419, relheight=0.068
            , relwidth=0.184, bordermode='ignore')
    self.radencsign.configure(activebackground="#ececec")
    self.radencsign.configure(activeforeground="#000000")
    self.radencsign.configure(background="#d9d9d9")
    self.radencsign.configure(disabledforeground="#a3a3a3")
    self.radencsign.configure(foreground="#000000")
    self.radencsign.configure(highlightbackground="#d9d9d9")
    self.radencsign.configure(highlightcolor="black")
    self.radencsign.configure(justify='left')
    self.radencsign.configure(text='''Sign and Encrypt''')

    self.msg = Text(self.Uframe)
    self.msg.place(relx=0.394, rely=0.189, relheight=0.308, relwidth=0.542
            , bordermode='ignore')
    self.msg.configure(background="white")
    self.msg.configure(font="TkTextFont")
    self.msg.configure(foreground="black")
    self.msg.configure(highlightbackground="#d9d9d9")
    self.msg.configure(highlightcolor="black")
    self.msg.configure(insertbackground="black")
    self.msg.configure(selectbackground="#c4c4c4")
    self.msg.configure(selectforeground="black")
    self.msg.configure(width=344)
    self.msg.configure(wrap='word')

    self.uploadbtn = Button(self.Uframe)
    self.uploadbtn.place(relx=0.843, rely=0.514, height=24, width=57
            , bordermode='ignore')
    self.uploadbtn.configure(activebackground="#ececec")
    self.uploadbtn.configure(activeforeground="#000000")
    self.uploadbtn.configure(background="#d9d9d9")
    self.uploadbtn.configure(disabledforeground="#a3a3a3")
    self.uploadbtn.configure(foreground="#000000")
    self.uploadbtn.configure(highlightbackground="#d9d9d9")
    self.uploadbtn.configure(highlightcolor="black")
    self.uploadbtn.configure(pady="0")
    self.uploadbtn.configure(text='''UPLOAD''')
    self.uploadbtn.bind('<Button-1>',self.upload)

    self.Canvas1 =  Canvas(self.Uframe)
    self.Canvas1.place(relx=0.094, rely=0.608, relheight=0.332
            , relwidth=0.839, bordermode='ignore')
    self.Canvas1.configure(background="#d9d9d9")
    self.Canvas1.configure(borderwidth="2")
    self.Canvas1.configure(insertbackground="black")
    self.Canvas1.configure(relief='ridge')
    self.Canvas1.configure(selectbackground="#c4c4c4")
    self.Canvas1.configure(selectforeground="black")
    self.Canvas1.configure(width=533)

    self.Dframe = LabelFrame(self.Aframe)
    self.Dframe.place(relx=0.008, rely=0.073, relheight=0.92
            , relwidth=0.987)
    self.Dframe.configure(relief='groove')
    self.Dframe.configure(foreground="black")
    self.Dframe.configure(text='''DOWNLOAD''')
    self.Dframe.configure(background="#d9d9d9")
    self.Dframe.configure(width=635)

    self.Canvasd =  Canvas(self.Dframe)
    self.Canvasd.place(relx=0.015, rely=0.64, relheight=0.332
            , relwidth=0.839, bordermode='ignore')
    self.Canvasd.configure(background="#d9d9d9")
    self.Canvasd.configure(borderwidth="2")
    self.Canvasd.configure(insertbackground="black")
    self.Canvasd.configure(relief='ridge')
    self.Canvasd.configure(selectbackground="#c4c4c4")
    self.Canvasd.configure(selectforeground="black")
    self.Canvasd.configure(width=533)

    self.down = Button(self.Dframe)
    self.down.place(relx=0.855, rely=0.649, height=48, width=87
                         , bordermode='ignore')
    self.down.configure(activebackground="#ececec")
    self.down.configure(activeforeground="#000000")
    self.down.configure(disabledforeground="#a3a3a3")
    self.down.configure(foreground="#000000")
    self.down.configure(highlightbackground="#d9d9d9")
    self.down.configure(highlightcolor="black")
    self.down.configure(pady="0")
    self.down.configure(text='''DOWNLOAD''')
    self.down.configure(width=87)
    self.down.bind('<Button-1>',self.download)
    self.remv = Button(self.Dframe)
    self.remv.place(relx=0.855, rely=0.8, height=48, width=87
                         , bordermode='ignore')
    self.remv.configure(activebackground="#ececec")
    self.remv.configure(activeforeground="#000000")
    self.remv.configure(background="#d85959")
    self.remv.configure(disabledforeground="#a3a3a3")
    self.remv.configure(foreground="#000000")
    self.remv.configure(highlightbackground="#d9d9d9")
    self.remv.configure(highlightcolor="black")
    self.remv.configure(pady="0")
    self.remv.configure(text='''REMOVE''')
    self.remv.configure(width=87)


    self.DLframe = VerticalScrolledFrame(self.Dframe)
    self.DLframe.pack()
    testfra=Label(self.DLframe.interior,text="\tSENDER\t\t\t\t\tFILE",width=85,anchor='w')
    testfra.grid()
    #print(self.myfiles)
    self.filel=[]
    self.point=-1
    counter=0
    for item in self.myfiles:
        self.filel.append(Label(self.DLframe.interior, text="\t"+item['sender']+"\t\t\t"+item['fname'],width=85,anchor='w',borderwidth=2, relief="groove"))
        self.filel[-1].bind('<Button-1>',lambda event, a=counter: self.daction(event,a))
        self.filel[-1].grid(row=counter)
        counter+=1
    #buttons = []
    #self.DLframe.interior.configure(height=100)
    
def daction(self,event,a):
    if self.point==a:
        return
    if self.point!=-1:
        item=self.myfiles[self.point]
        self.filel[self.point].grid_forget()
        self.filel[self.point]=Label(self.DLframe.interior, text="\t"+item['sender']+"\t\t\t"+item['fname'],width=85,anchor='w',borderwidth=2, relief="groove")
        self.filel[self.point].bind('<Button-1>',lambda event, a=self.point: self.daction(event,a))
        self.filel[self.point].grid(row=self.point)

    self.point=a    
    item=self.myfiles[self.point]
    self.filel[self.point].grid_forget()
    self.filel[self.point]=Label(self.DLframe.interior, text="\t"+item['sender']+"\t\t\t"+item['fname'],width=85,background='#c4feff',anchor='w',borderwidth=2, relief="groove")
    self.filel[self.point].bind('<Button-1>',lambda event, a=self.point: self.daction(event,a))
    self.filel[self.point].grid(row=self.point)
    
    mode=""
    if self.myfiles[self.point]['mode']==1:
        mode="Normal"
    elif self.myfiles[self.point]['mode']==2:
        mode="Encrypted"
    elif self.myfiles[self.point]['mode']==3:
        mode="Signed"
    else:
        mode="Signed and Encrypted"
    
    test = Label(self.Canvasd)
    test.place(relx=0.01, rely=0.04, height=116, width=523)
    #test.config(font=(1))
    test.configure(disabledforeground="#a3a3a3")
    test.configure(foreground="#000000")
    test.configure(background="#c4feff")
    test.configure(text="File:"+self.myfiles[self.point]['fname']+"\t\t"+"Mode:"+mode+"\n"+"Sender:"+self.myfiles[self.point]['sender']+"\t"+"Date/Time:"+str(self.myfiles[self.point]['date'])+"\t"+"Size"+str(self.myfiles[self.point]['size']/1000.0)+" Kb"+"\nRemark:"\
                   +self.myfiles[self.point]['msg'])
                   
    test.configure(width=214)

    return



def download(self,event):
    if self.point==-1:
        return
    name=self.myfiles[self.point]['fname']
    f_path=filedialog.askdirectory(initialdir = "/home")
    if f_path=="":
        test = Label(self.Canvasd)
        test.place(relx=0.01, rely=0.04, height=116, width=523)
        test.config(font=(2))
        test.configure(disabledforeground="#a3a3a3")
        test.configure(foreground="#000000")
        test.configure(background="#c4feff")
        test.configure(text="Please Select Location to download.")
        test.configure(width=214)
        return
    
    s=socket.socket()
    try:
            s.connect((self.ip,self.port))
    except:
            test = Label(self.Canvasd)
            test.place(relx=0.01, rely=0.04, height=116, width=523)
            test.config(font=(2))
            test.configure(disabledforeground="#a3a3a3")
            test.configure(foreground="#000000")
            test.configure(background="#c4feff")
            test.configure(text="Server Not Responding!")
            test.configure(width=214)
    
    s.send(pickle.dumps("download"))
    dummy=s.recv(24)
    
    s.send(pickle.dumps(name))
    		
    f= open(f_path+"/"+name,"w")
    f.close()
    #s.send("send")
    
    
    while True:
            data=s.recv(1024)
            #print data
            f= open(f_path+"/"+name,"a+b")
            #print "recieving length"+str(len(data))
            f.write(data)
            f.close()
            if (len(data)<1024):
                    break
    s.close()
    test = Label(self.Canvasd)
    test.place(relx=0.01, rely=0.04, height=116, width=523)
    test.config(font=(2))
    test.configure(disabledforeground="#a3a3a3")
    test.configure(foreground="#000000")
    test.configure(background="#c4feff")
    test.configure(text="File Downloaded!")
    test.configure(width=214)

def toggleu2d(self,event):
    self.Uframe.place_forget()
    self.Dframe.place(relx=0.008, rely=0.073, relheight=0.902
            , relwidth=0.977)
def toggled2u(self,event):
    self.Dframe.place_forget()
    self.Uframe.place(relx=0.008, rely=0.073, relheight=0.902
            , relwidth=0.977)
def frefresh(self,event):
    self.Uframe.place_forget()
    self.Dframe.place_forget()
    s=socket.socket()
    try:
        s.connect((self.ip,self.port))
    except:
        test = Label(self.msgcan)
        test.place(relx=0.01, rely=0.04, height=113, width=484)
        test.config(font=(10))
        test.configure(disabledforeground="#a3a3a3")
        test.configure(foreground="#000000")
        test.configure(text='''SERVER NOT RESPONDING!''')
        test.configure(width=214)
        return
    s.send(pickle.dumps("myfiles"))
    dummy=s.recv(24)
    
    s.send(pickle.dumps(self.user))
    self.myfiles=s.recv(10240)
    self.myfiles=pickle.loads(self.myfiles)
    print(self.myfiles)
    self.addfile()
    
def validate(self,event):
    print(self.rem)
    self.user=self.Entryl.get()
    pas=self.Entryp.get()
    s=socket.socket()
    try:
        s.connect((self.ip,self.port))
    except:
        test = Label(self.msgcan)
        test.place(relx=0.01, rely=0.04, height=113, width=484)
        test.config(font=(10))
        test.configure(disabledforeground="#a3a3a3")
        test.configure(foreground="#000000")
        test.configure(text='''SERVER NOT RESPONDING!''')
        test.configure(width=214)
        return
    data={'user':self.user,'pass':pas}
    s.send(pickle.dumps("verify"))
    dummy=s.recv(24)
    s.send(pickle.dumps(data))
    result=s.recv(100)
    result=pickle.loads(result)
    #result="1"
    if result=="1":
        self.logframe.place_forget()
        self.initialiser()
        
        s.close()
        s=socket.socket()
        try:
            s.connect((self.ip,self.port))
        except:
            test = Label(self.msgcan)
            test.place(relx=0.01, rely=0.04, height=113, width=484)
            test.config(font=(10))
            test.configure(disabledforeground="#a3a3a3")
            test.configure(foreground="#000000")
            test.configure(text='''SERVER NOT RESPONDING!''')
            test.configure(width=214)
            return
        s.send(pickle.dumps("myfiles"))
        dummy=s.recv(24)
        
        s.send(pickle.dumps(self.user))
        self.myfiles=s.recv(10240)
        self.myfiles=pickle.loads(self.myfiles)
        print(self.myfiles)
        self.addfile()
        #print(self.myfile)
        #fil=pickle.loads(fil)
        #print(fil)
    elif result=="0":
        test = Label(self.msgcan)
        test.place(relx=0.01, rely=0.04, height=113, width=484)
        test.configure(disabledforeground="#a3a3a3")
        test.configure(foreground="#000000")
        test.configure(text='''Well! That password did not match''')
        test.configure(width=214)
        test.config(font=(10))
    else:
        test = Label(self.msgcan)
        test.place(relx=0.01, rely=0.04, height=113, width=484)
        test.config(font=(10))
        test.configure(disabledforeground="#a3a3a3")
        test.configure(foreground="#000000")
        test.configure(text='''Incorrect/unregistered user\nplease check user account!!''')
        test.configure(width=214)
    
    


def browse(self,event):
    self.fpath =  filedialog.askopenfilename(initialdir = "/home",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg"),("text files","*.txt"),("pdf files","*.pdf"),("mp4 files","*.mp4")))	
    print (self.fpath)
    print (filename(self.fpath))
    return
def upload(self,event):
    if self.Entryfor.get()=="":
        test = Label(self.Canvas1)
        test.place(relx=0.01, rely=0.04, height=112, width=518)
        test.config(font=(10))
        test.configure(background="#c4feff")
        test.configure(disabledforeground="#a3a3a3")
        test.configure(foreground="#000000")
        test.configure(text='''Please mention Reciever!''')
        test.configure(width=214)
        return
    if self.fpath=="":
        test = Label(self.Canvas1)
        test.place(relx=0.01, rely=0.04, height=112, width=518)
        test.config(font=(10))
        test.configure(background="#c4feff")
        test.configure(disabledforeground="#a3a3a3")
        test.configure(foreground="#000000")
        test.configure(text='''Please Select any file!''')
        test.configure(width=214)
        return
    s=socket.socket()
    try:
        s.connect((self.ip,self.port))
    except:
        test = Label(self.Canvas1)
        test.place(relx=0.01, rely=0.04, height=112, width=518)
        test.config(font=(10))
        test.configure(background="#c4feff")
        test.configure(disabledforeground="#a3a3a3")
        test.configure(foreground="#000000")
        test.configure(text='''Server did nit respond!''')
        test.configure(width=214)
        return
    s.send(pickle.dumps("upload"))
    dummy=s.recv(24)
    info={'fname':filename(self.fpath),'size':os.path.getsize(self.fpath),'msg':self.msg.get("1.0",END),'mode':1,'sender':self.user,'reciever':self.Entryfor.get()}
    s.send(pickle.dumps(info))
    dummy=s.recv(20)
    try:
            file=open(self.fpath,"r+b")
    except:
        test = Label(self.Canvas1)
        test.place(relx=0.01, rely=0.04, height=112, width=518)
        test.config(font=(10))
        test.configure(background="#c4feff")
        test.configure(disabledforeground="#a3a3a3")
        test.configure(foreground="#000000")
        test.configure(text='''Unable to open this file!''')
        test.configure(width=214)
        self.fpath=""
        s.close()
        return
    test = Label(self.Canvas1)
    test.place(relx=0.01, rely=0.04, height=112, width=518)
    test.config(font=(10))
    test.configure(background="#c4feff")
    test.configure(disabledforeground="#a3a3a3")
    test.configure(foreground="#000000")
    test.configure(text='''File is being uploaded!''')
    test.configure(width=214)
    read=file.read(1024)
    while True:
            s.send(read)
            if (len(read)<=0):
                    break
            read=file.read(1024)

    test = Label(self.Canvas1)
    test.place(relx=0.01, rely=0.04, height=112, width=518)
    test.config(font=(10))
    test.configure(background="#c4feff")
    test.configure(disabledforeground="#a3a3a3")
    test.configure(foreground="#000000")
    test.configure(text='''File Uploaded Successfully!''')
    test.configure(width=214)
    self.fpath=""
    s.close()

def filename(fpath):
    fname=""
    for ch in fpath[::-1]:
            if ch=='/':
                    break
            fname=ch+fname
    return fname
def logout(self,event):
    self.Aframe.destroy()
    self.Tframe.destroy()
    self.addlogin()
def setrem(self):
    if self.rem==0:
        self.rem=1
    else:
        self.rem=0
    
def _0(self):
    self.type=0
def _1(self):
    self.type=1
def _2(self):
    self.type=2
def _3(self):
    self.type=3
