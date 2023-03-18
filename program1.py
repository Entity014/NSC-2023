import os
from tkinter  import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from tkinter import messagebox
import sys 
import shutil

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
    name = (path.split("/"))[-1]
    global detectedp
    detectedp = path_ofprogram+ "/runs/detect/exp/"+name
    print(detectedp)
    comand_d = f"py detect.py --weights nsc2.pt --conf 0.5 --img-size 640 --source {path} --view-img --no-trace --save-txt" 
    os.system(comand_d)
    global top
    top= Toplevel(mainmenu)
    top.geometry("750x250")
    top.title("Detected photo")

    im = Image.open(detectedp)
    img = im.resize((600,400))
    new_image= ImageTk.PhotoImage(img)
    myvar=Label(top,image = new_image)
    myvar.image = new_image
    myvar.pack()
    
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
    practice = Tk()#สำหรับแบบฝึกหัด
    practice.title("Practice your Circuit")
    Button(practice,text="Chapter 1",fg="Black",bg="Grey",font="150").pack()
    Button(practice,text="Chapter 2",fg="Black",bg="Grey",font="150").pack()
    Button(practice,text="Chapter 3",fg="Black",bg="Grey",font="150").pack()
    Button(practice,text="Chapter 4",fg="Black",bg="Grey",font="150").pack()
    #mainmenu.destroy()
    #Practice.geometry("800x600+100+50")

#กล่องโต้ตอบ
def ExitProgram():
    confirm = messagebox.askquestion("Exit","Are you sure about to exit?" )
    if confirm == "yes" :
        shutil.rmtree(path_ofprogram+ "/runs/detect/")
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
bt4=Button(text="Select picture",fg="White",bg="Black",command=select_files2d).pack()
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

