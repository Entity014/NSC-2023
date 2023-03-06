import os
from tkinter  import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from tkinter import messagebox


#สร้างหน้าจอ ขึ้นมาเพื่อแสดงผล
mainmenu = Tk()
mainmenu.title("InspectCir Lite") #ชื่อของหน้าต่าง

pathf =""


#ใส่ข้อความในหน้าจอ
myLabel1 = Label(mainmenu,text="Welcome to InspectCir Lite!",font=50).pack()
#Sandbox window
def Sandbox():
    SandboxCir = Tk() #สำหรับทำ Sandbox Circuit
    SandboxCir.title("Sandbox your Circuit")
    SandboxCir.geometry("1600x900+100+50")

#Practice window
def Practice():
    Practice = Tk()#สำหรับแบบฝึกหัด
    Practice.title("Practice your Circuit")
    Practice.geometry("1600x900+100+50")
    
    
#สร้างหน้าต่างหลัก
def Newwindow():
    newwindow = Tk()
    newwindow.title("InspectCir Lite")
    newwindow.geometry("800x600+100+50")
    newwindow.mainloop()

#กล่องโต้ตอบ
def ExitProgram():
    confirm = messagebox.askquestion("Exit","Are you sure about to exit?" )
    if confirm == "yes" :
        mainmenu.destroy()
 
#สร้างแถบเมนู
Mymenu = Menu()
mainmenu.config(menu=Mymenu)

#Add Sub-Menu bar
menuitem = Menu()
menuitem.add_command(label="New Window",command = Newwindow)
menuitem.add_command(label="Open File")
menuitem.add_command(label="Save File")
menuitem.add_command(label="Exit",command = ExitProgram)
  

#Add Menu bar
Mymenu.add_cascade(label="File",menu=menuitem)
Mymenu.add_cascade(label="Edit")
Mymenu.add_cascade(label="View")
Mymenu.add_cascade(label="Run")

def select_files2d():
    path=fd.askopenfilename(filetypes=[("Image File",'.jpg'),("Image File" , '.png')])
    im = Image.open(path)
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(mainmenu,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    comand_d = f"py detect.py --weights nsc2.pt --conf 0.5 --img-size 640 --source {path} --view-img --no-trace --save-txt" 
    os.system(comand_d)
    print(path)


#ใส่ปุ่มกด
bt1=Button(text="Circuit Sandbox",fg="White",bg="Black",command = Sandbox).pack()
bt2=Button(text="Circuit Practice",fg="White",bg="Black",command = Practice).pack()
bt3=Button(text="Exit",fg="White",bg="Black",command = ExitProgram).pack()
bt1=Button(text="chose picture",fg="White",bg="Black",command=select_files2d).pack()

mainmenu.geometry("1600x900+100+50") #กำหนดขนาดของหน้าจอเริ่มต้น
mainmenu.mainloop()



