from tkinter import *

t = Tk()
t.overrideredirect(1)
from win32api import GetSystemMetrics
t.geometry(f"650x675+{int(GetSystemMetrics(0) / 2) - 300}+40")
t.config(bg="#3b53a0")
t.iconbitmap("Icons/image.ico")
t.title((" " * 80) + "Sliding Puzzle")
t.resizable(0, 0)
f=Frame(t,bg="#000")
f.place(x=0,y=0,width=650,height=650)
lf=[]
lt=[]
ltc=[]
Lab=[]
cmp=0
from PIL import Image, ImageTk
path="Images/img.jpg"
for i in range(3):
    for j in range(3):
        lf.append(Frame(f))
        if i==2 and j==2:
            Lab.append(Label(lf[cmp],background="#242424"))
            lt.append(["",cmp])
            ltc.append(["",cmp])
        else:
            lt.append([ImageTk.PhotoImage(Image.open(path).resize((600,600)).crop(((j*200),(i*200),((j*200)+200), ((i*200)+200)))),cmp])
            ltc.append([ImageTk.PhotoImage(Image.open(path).resize((600,600)).crop(((j*200),(i*200),((j*200)+200), ((i*200)+200)))),cmp])
            Lab.append(Label(lf[cmp],image=lt[cmp][0],background="#3b53a0"))
        Lab[cmp].bind("<Button-1>",lambda event,h=cmp:lol(event,h))
        Lab[cmp].place(x=2,y=2,width=196,height=196)
        lf[cmp].place(x=(j*200),y=(i*200),width=200,height=200)
        cmp+=1
index=8
from threading import Thread
def lol(event,h):
    global index,t,b
    if Lab[h].cget("bg")=="#242424" and (h-1==index or h+1==index or h+3==index or h-3==index):
        Lab[h].config(image=ltc[index][0])
        ih=ltc[h][1]
        ltc[h]=[ltc[index][0],ltc[index][1]]
        ltc[index]=["",ih]
        Lab[index].config(image="")
        Lab[h].config(bg="#3b53a0")
        Lab[index].config(bg="#242424")
        k=0
        for i in range(len(ltc)):
            if ltc[i][1]==lt[i][1]:
                k+=1
        if k==(len(ltc)):
            changetheimage.place_forget()
            youwin.place(x=0,y=600,width=600,height=50)
            b=False
            Thread(target=lambda y=youwin:tim(y)).start()
    lf[index].config(bg="white")
    index=h
    lf[h].config(bg="black")
yw=ImageTk.PhotoImage((Image.open("Images/youwin.png")))
yww=ImageTk.PhotoImage((Image.open("Images/youwinwhite.png")))
youwin=Label(t,image=yw)
from time import sleep
def tim(youwin):
    w=0
    while True:
        try:
            if w%2 == 0:
                youwin.config(image=yww)
            else:
                youwin.config(image=yw)
            w+=1
            if w==100:
                w=0
            sleep(0.5)
            if b:
                return
        except:
            return
iim=ImageTk.PhotoImage((Image.open("Images/restart.png")))
iimw=ImageTk.PhotoImage((Image.open("Images/restartwhite.png")))
restart=Label(t,image=iim)
restart.place(x=600,y=0,width=50,height=600)
restart.bind("<Enter>",lambda event:restart.config(image=iimw))
restart.bind("<Leave>",lambda event:restart.config(image=iim))
_a89=ImageTk.PhotoImage((Image.open("Images/a89.png")))
a89=Label(t,image=_a89)
a89.place(x=600,y=600,width=50,height=50)
import subprocess
import sys
import os

def reset_image(event):
    #restart program
    python = sys.executable
    subprocess.Popen([python, "main.py"])
    os.execl(python, python, * sys.argv)
a89.bind("<Button-1>", reset_image)
from tkinter import messagebox
from tkinter import filedialog
cti=ImageTk.PhotoImage((Image.open("Images/changetheimage.png")))
ctiw=ImageTk.PhotoImage((Image.open("Images/changetheimagewhite.png")))
changetheimage=Label(t,image=cti)
changetheimage.place(x=0,y=600,width=600,height=50)
changetheimage.bind("<Enter>",lambda event:changetheimage.config(image=ctiw))
changetheimage.bind("<Leave>",lambda event:changetheimage.config(image=cti))
def cticlick(event):
    filetypes = (
        ('Images', '*.png'),
        ('All files', '*.png')
    )
    t.iconbitmap("Icons/image.ico")
    e = filedialog.askopenfile(title="Open the image (with the same dimensions)", initialdir='/', filetypes=filetypes)
    if e!=None:
        if Image.open(e.name).width!=Image.open(e.name).height:
            messagebox.askokcancel("","The image need to has the same dimensions")
        else:
            path=e.name
            lt.clear()
            ltc.clear()
            t.title((" " * 60) + "Sliding Puzzle | The image is loading ...")
            cmp=0
            for i in range(3):
                for j in range(3):
                    if i==2 and j==2:
                        lt.append(["",cmp])
                        ltc.append(["",cmp])
                    else:
                        lt.append([ImageTk.PhotoImage(Image.open(path).resize((600,600)).crop(((j*200),(i*200),((j*200)+200), ((i*200)+200)))),cmp])
                        ltc.append([ImageTk.PhotoImage(Image.open(path).resize((600,600)).crop(((j*200),(i*200),((j*200)+200), ((i*200)+200)))),cmp])
                    cmp+=1
            cos(None)
    t.title((" " * 80) + "Sliding Puzzle")
    t.iconbitmap("Icons/image.ico")
changetheimage.bind("<Button-1>",cticlick)
from random import shuffle
b=False
def f():
    global b
    b=True
    t.destroy()
t.protocol("WM_DELETE_WINDOW",f)
def cos(event):
    global ltc,Lab,b
    if event:
        shuffle(ltc)
    for i in range(len(ltc)):
        Lab[i].config(image=ltc[i][0])
        Lab[i].config(bg="#3b53a0")
    for j in range(len(ltc)):
        if ltc[j][0]=="":
            Lab[j].config(bg="#242424")
    b=True
    youwin.place_forget()
    changetheimage.place(x=0,y=600,width=600,height=50)
restart.bind("<Button-1>",cos)
# from playsound import playsound
introf=Frame(t)
introf.place(x=0,y=0,width=650,height=650)
introi=[]
for i in range(76):
    image_path = f"Images/loading/loading{i+1}.png"
    introi.append(ImageTk.PhotoImage(Image.open(image_path).resize((300,300))))
introl=Label(introf,bg="#3b53a0")
introl.place(x=0,y=0,width=650,height=650)
def intro():
    icmp=0
    ic=0
    # Thread(target=lambda:playsound("g/gs.wav")).start()
    while True:
        introl.config(image=introi[icmp])
        sleep(0.02)
        ic+=1
        icmp+=1
        if icmp==76:
            icmp=0
        if ic==76:
            break
    introf.place_forget()
    t.geometry(f"650x650")
    t.overrideredirect(0)
t.after(1,lambda :Thread(target=intro).start())
t.mainloop()