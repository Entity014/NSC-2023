import os
from tkinter  import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from tkinter import messagebox
import sys 
import shutil
import netlist2Circuit
import image2net

#สร้างหน้าจอ ขึ้นมาเพื่อแสดงผล
mainmenu = Tk()
mainmenu.title("InspectCir Lite") #ชื่อของหน้าต่าง
global path_ofprogram
path_ofprogram = sys.path[0] 
print(path_ofprogram)
pathf =None

#นำเข้ารูปภาพ
def select_files2d():
    path=fd.askopenfilename(filetypes=[("Image File",'.jpg')])
    if(path !=""):
        name = (path.split("/"))[-1]
        global detectedp
        detectedp = path_ofprogram+ "/runs/detect/exp/"+name
        print(detectedp)
        comand_d = f"py detect.py --weights nsc2.pt --conf 0.5 --img-size 640 --source {path} --view-img --no-trace --save-txt" 
        os.system(comand_d)

        detectedi= Toplevel(mainmenu)
        detectedi.geometry("750x250")
        detectedi.title("Detected photo")

        im = Image.open(detectedp)
        img = im.resize((600,400))
        new_image= ImageTk.PhotoImage(img)
        myvar=Label(detectedi,image = new_image)
        myvar.image = new_image
        myvar.pack()
    
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
    practicepath = path_ofprogram + "/chapter/" + indexprob[k-1] +".png"
    practiceproblem= Toplevel(mainmenu)
    practiceproblem.geometry("750x250")
    practiceproblem.title("indexprob[k]")
    
    chapim = Image.open(practicepath)
    chapimg = chapim.resize((600,400))
    chapnew_image= ImageTk.PhotoImage(chapimg)
    chapmyvar=Label(practiceproblem,image = chapnew_image)
    chapmyvar.image = chapnew_image
    chapmyvar.pack()

#ใส่ข้อความในหน้าจอ
myLabel1 = Label(mainmenu,text="Welcome to InspectCir Lite!",font=250,fg="Black").pack()


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
    # practiceproblem.geometry("750x250")
    practice.title("Practice your Circuit")
    Button(practice,text="Exercise 1.1",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(1)).pack()
    Button(practice,text="Exercise 1.2",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(2)).pack()
    Button(practice,text="Exercise 1.3",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(3)).pack()
    Button(practice,text="Exercise 2.1",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(4)).pack()
    Button(practice,text="Exercise 2.2",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(5)).pack()
    Button(practice,text="Exercise 2.3",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(6)).pack()
    Button(practice,text="Exercise 2.4",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(7)).pack()
    Button(practice,text="Exercise 2.5",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(8)).pack()
    Button(practice,text="Exercise 2.6",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(9)).pack()
    Button(practice,text="Exercise 3.1",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(10)).pack()
    Button(practice,text="Exercise 3.2",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(11)).pack()
    Button(practice,text="Exercise 3.3",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(12)).pack()
    Button(practice,text="Exercise 4.1",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(13)).pack()
    Button(practice,text="Exercise 4.2",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(14)).pack()
    Button(practice,text="Exercise 4.3",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(15)).pack()
    Button(practice,text="Exercise 4.4",fg="Black",bg="Grey",font="150",command=lambda:practiceprob(16)).pack()
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
bt1=Button(mainmenu,text="Circuit Sandbox",fg="Black",bg="Light Grey",font="150",command = select_files2d).pack()
bt2=Button(mainmenu,text="Circuit Practice",fg="Black",bg="Light Grey",font="150",command = Practice).pack()

# bt3=Button(text="New window",fg="White",bg="Black",command=open_popup).pack()
bt3=Button(mainmenu,text="Exit",fg="Black",bg="Light Grey",font="150",command = ExitProgram).pack()

mainmenu.geometry("800x600+100+50") #กำหนดขนาดของหน้าจอเริ่มต้น
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

