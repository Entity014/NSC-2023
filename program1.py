import os
from tkinter  import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from tkinter import messagebox
import sys 
import shutil
from netlist2Circuit import netlist2Circuit
from image2net import toNetlist
from image2net import toNetlist
from lcapy import Circuit

#สร้างหน้าจอ ขึ้นมาเพื่อแสดงผล
mainmenu = Tk()
mainmenu.title("InspectCir Lite") #ชื่อของหน้าต่าง
mainmenu.geometry("800x600+100+50") #กำหนดขนาดของหน้าจอเริ่มต้น
mainmenu.minsize(800, 600)
mainmenu.maxsize(800, 600)
global path_ofprogram
path_ofprogram = sys.path[0] 
print(path_ofprogram)
pathf =None
global TopV
TopV = False
bGpath=path_ofprogram+"/BG/background.png"
Exbg =path_ofprogram+"/BG/Exbg.png"
Pbg = path_ofprogram+"/BG/Pbackground.png"
global netlist
global background
global Ebackground
global Pbackground
background = PhotoImage( file = bGpath)
Ebackground = PhotoImage( file = Exbg)
Pbackground = PhotoImage( file = Pbg)
#นำเข้ารูปภาพ
def switch():
    global TopV
    if(TopV):
        TopV = False
        print(TopV)
        A1.config(text="Front View")
    else:
        TopV = True
        print(TopV)
        A1.config(text="Top View")
def Detectpage():
    global TopV
    global A1
    Detectpage= Toplevel(mainmenu)
    Detectpage.geometry("750x250")
    Detectpage.minsize(750, 250)
    Detectpage.maxsize(750, 250)
    
    Elabel = Label(Detectpage, image = Ebackground)
    Elabel.place(x = 0,y = 0)

    Button(Detectpage,text="Detect Image",height= 1, width=60,fg="Black",bg="#77CFFF",font=("Arial", 15),command = select_files2d).pack(padx=5, pady=5)
    Button(Detectpage,text="Switch",height= 1, width=60,fg="Black",bg="#77CFFF",font=("Arial", 15),command = switch).pack(padx=5, pady=5)
    A1 = Label(Detectpage,text="Top View",font=250,fg="Black",bg="#BCC9F9")
    A1.pack()
def select_files2d():
    path=fd.askopenfilename(filetypes=[("Image File",'.jpg')])
    if(path !=""):

        namej = (path.split("/"))[-1]
        name = (namej.split("."))[0]
        print(namej)
        global detectedp
        global netlist
        path = '"'+path +'"'
        detectedp = path_ofprogram+ "/runs/detect/exp/"+namej
        txtpath = path_ofprogram + "/runs/detect/exp/labels/"+name+".txt"
        resultpath = path_ofprogram +"/Result/result.png"
        epath = path_ofprogram + "/ERROR/error.png"
        print(detectedp)
        try:
            comand_d = f"py detect.py --weights nsc2.pt --conf 0.5 --img-size 640 --source {path} --view-img --no-trace --save-txt" 
            os.system(comand_d)
        
            if(TopV):
                netlist = toNetlist(txtpath,"HIGH")
            else:
                netlist = toNetlist(txtpath,"LOW")
                text,cct = netlist2Circuit(netlist)
                cct.draw("Result/result.png")
        except:
            resultpath = epath
        # detectedi= Toplevel(mainmenu)
        # detectedi.geometry("750x250")
        # detectedi.title("Detected photo")

        Resulti= Toplevel(mainmenu)
        Resulti.geometry("750x600")
        Resulti.title("Circuit")
        Resulti.minsize(750, 600)
        Resulti.maxsize(750, 600)

        # im = Image.open(detectedp)
        # img = im.resize((600,400))
        # new_image= ImageTk.PhotoImage(img)
        # myvar=Label(detectedi,image = new_image)
        # myvar.image = new_image
        # myvar.pack()

        Rim = Image.open(resultpath)
        Rimg  = Rim.resize((600,400))
        Rnew_image= ImageTk.PhotoImage(Rimg)
        Rmyvar=Label(Resulti,image = Rnew_image)
        Rmyvar.image = Rnew_image
        Rmyvar.pack()
        #function convert to circuit diagram
        #path of circuit diagram photo
        # diagram= Toplevel(mainmenu)
        # diagram.geometry("750x250")
        # diagram.title("circuit diagram")
        # c_im = Image.open(detectedp)
        # c_img = im.resize((600,400))
        # c_new_image= ImageTk.PhotoImage(img)
        # myvar=Label(diagram,image = new_image)
        # myvar.image = new_image
        # myvar.pack()
        exppath = path_ofprogram+ "/runs/detect/"
        if any(os.scandir(exppath)):
            shutil.rmtree(path_ofprogram+ "/runs/detect/exp/")


def practiceprob(k):
    indexprob=["0_0","0_1","0_2","1_0","1_1","1_2","1_3","1_4","1_5","2_0","2_1","2_2","3_0","3_1","3_2","3_3"]
    E = ["1.1","1.2","1.3","2.1","2.2","2.3","2.4","2.5","2.6","3.1","3.2","3.3","4.1","4.2","4.3","4.4"]
    global practicepath
    practicepath = path_ofprogram + "/chapter/" + indexprob[k-1] +".png"
    practiceproblem= Toplevel(mainmenu)
    practiceproblem.geometry("750x500")
    practiceproblem.title("Exercise "+E[k-1])
    practiceproblem.minsize(800, 600)
    practiceproblem.maxsize(800, 600)
    
    
    Elabel = Label(practiceproblem, image = Ebackground)
    Elabel.place(x = 0,y = 0)

    Button(practiceproblem,text="Put your Answer",height=1, width=30,fg="white",bg="#77CFFF",font=("Arial", 15),command = select_files2d).pack()
    chapim = Image.open(practicepath)
    chapimg = chapim.resize((600,400))
    chapnew_image= ImageTk.PhotoImage(chapimg)
    chapmyvar=Label(practiceproblem,image = chapnew_image)
    chapmyvar.image = chapnew_image
    chapmyvar.pack()
    

#ใส่ข้อความในหน้าจอ
label1 = Label( mainmenu, image = background)
label1.place(x = 0,y = 0)
myLabel1 = Label(mainmenu,text="Welcome to InspectCir Lite!",font=250,fg="Black",bg="#BCC9F9").pack()


# def open_popup():
#    global top
#    top= Toplevel(mainmenu)
#    top.geometry("750x250")
#    top.title("Detected photo")
#    Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)
#    Button(top,text="chose picture",fg="White",bg="Black",command=select_files2d).pack()
#Practice window
def Practice():
    practice = Toplevel(mainmenu)#สำหรับแบบฝึกหัด
    practice.geometry("800x600")
    practice.minsize(800, 600)
    practice.maxsize(800, 600)
    Plabel = Label(practice, image = Pbackground)
    Plabel.place(x = 0,y = 0)
    # practiceproblem.geometry("750x250")
    practice.title("Practice your Circuit")
    Button(practice,text="Exercise 1.1",fg="Black",bg="#72FF85",font="150",command=lambda:practiceprob(1)).place( relx=0.3, rely=0.1, anchor=N)
    Button(practice,text="Exercise 1.2",fg="Black",bg="#72FF85",font="150",command=lambda:practiceprob(2)).place( relx=0.3, rely=0.2, anchor=N)
    Button(practice,text="Exercise 1.3",fg="Black",bg="#72FF85",font="150",command=lambda:practiceprob(3)).place( relx=0.3, rely=0.3, anchor=N)
    Button(practice,text="Exercise 2.1",fg="Black",bg="#EDFF72",font="150",command=lambda:practiceprob(4)).place( relx=0.3, rely=0.4, anchor=N)
    Button(practice,text="Exercise 2.2",fg="Black",bg="#EDFF72",font="150",command=lambda:practiceprob(5)).place( relx=0.3, rely=0.5, anchor=N)
    Button(practice,text="Exercise 2.3",fg="Black",bg="#EDFF72",font="150",command=lambda:practiceprob(6)).place( relx=0.3, rely=0.6, anchor=N)
    Button(practice,text="Exercise 2.4",fg="Black",bg="#EDFF72",font="150",command=lambda:practiceprob(7)).place( relx=0.3, rely=0.7, anchor=N)
    Button(practice,text="Exercise 2.5",fg="Black",bg="#EDFF72",font="150",command=lambda:practiceprob(8)).place( relx=0.3, rely=0.8, anchor=N)
    Button(practice,text="Exercise 2.6",fg="Black",bg="#EDFF72",font="150",command=lambda:practiceprob(9)).place( relx=0.7, rely=0.1, anchor=N)
    Button(practice,text="Exercise 3.1",fg="Black",bg="#FFAC70",font="150",command=lambda:practiceprob(10)).place( relx=0.7, rely=0.2, anchor=N)
    Button(practice,text="Exercise 3.2",fg="Black",bg="#FFAC70",font="150",command=lambda:practiceprob(11)).place( relx=0.7, rely=0.3, anchor=N)
    Button(practice,text="Exercise 3.3",fg="Black",bg="#FFAC70",font="150",command=lambda:practiceprob(12)).place( relx=0.7, rely=0.4, anchor=N)
    Button(practice,text="Exercise 4.1",fg="Black",bg="#FF6D6D",font="150",command=lambda:practiceprob(13)).place( relx=0.7, rely=0.5, anchor=N)
    Button(practice,text="Exercise 4.2",fg="Black",bg="#FF6D6D",font="150",command=lambda:practiceprob(14)).place( relx=0.7, rely=0.6, anchor=N)
    Button(practice,text="Exercise 4.3",fg="Black",bg="#FF6D6D",font="150",command=lambda:practiceprob(15)).place( relx=0.7, rely=0.7, anchor=N)
    Button(practice,text="Exercise 4.4",fg="Black",bg="#FF6D6D",font="150",command=lambda:practiceprob(16)).place( relx=0.7, rely=0.8, anchor=N)
    # mainmenu.destroy()
    #Practice.geometry("800x600+100+50")

#กล่องโต้ตอบ
def ExitProgram():
    confirm = messagebox.askquestion("Exit","Are you sure about to exit?" )
    exppath = path_ofprogram+ "/runs/detect/"
    if confirm == "yes" :
        if not any(os.scandir(exppath)):
            mainmenu.destroy()
        else:
            mainmenu.destroy()

#สร้างแถบเมนู
#Mymenu = Menu()
#mainmenu.config(menu=Mymenu)
#Add Sub-Menu bar
#menuitem = Menu()
#menuitem.add_command(label="New Window")
#menuitem.add_command(label="Open File")
#menuitem.add_command(label="Save File")
#menuitem.add_command(label="Exit",command = ExitProgram)
#Add Menu bar
#Mymenu.add_cascade(label="File",menu=menuitem)
#Mymenu.add_cascade(label="Edit")
#Mymenu.add_cascade(label="View")
#Mymenu.add_cascade(label="Run")

#ใส่ปุ่มกด
bt1=Button(mainmenu,text="Circuit Sandbox",height= 5, width=60,fg="Black",bg="#77CFFF",font=("Arial", 15),command = Detectpage).pack(padx=5, pady=15)
bt2=Button(mainmenu,text="Circuit Practice",height= 5, width=60,fg="Black",bg="#A9FFFD",font=("Arial", 15),command = Practice).pack(padx=5, pady=30)
bt3=Button(mainmenu,text="Exit",height= 5, width=60,fg="Black",bg="#FF6861",font=("Arial", 15),command = ExitProgram).pack(padx=5, pady=45)


mainmenu.mainloop()

#Sandbox window
#def Sandbox():
    #SandboxCir = Tk() #สำหรับทำ Sandbox Circuit
    #SandboxCir.title("Sandbox your Circuit")
    ##Label(SandboxCir,text="Click on Select Picture to scan your citcuit\n",font=175,fg="Red").pack()
    #Button(SandboxCir,text="Select Picture",fg="Black",bg="Grey",font="150",command=select_files2d).pack()
    #Button(SandboxCir,text="Back",fg="Black",bg="Grey",font="100").pack()
    #mainmenu.destroy() #ปิดหน้าต่างหลัก
    #SandboxCir.geometry("800x600+100+50")

