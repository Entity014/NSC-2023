import os
from tkinter  import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import sys 
import shutil


#สร้างหน้าจอ ขึ้นมาเพื่อแสดงผล
root = Tk()
root.title("InspectCir Lite") #ชื่อของหน้าต่าง
global path_ofprogram
path_ofprogram = sys.path[0] 
print(path_ofprogram)
pathf =None


#ใส่ข้อความในหน้าจอ
myLabel1 = Label(root,text="Hi There!",font=50).pack()


#Create Function
def showMessage1():
    Label(root,text="Coming Soon!",fg="red",bg="yellow",font=15).pack()
def showMessage2():
    Label(root,text="Coming Soon too!",fg="black",bg="yellow",font="50").pack()
def exit_x():
    shutil.rmtree(path_ofprogram+ "/runs/detect/")
    exit()
def select_files2d():
    path=fd.askopenfilename(filetypes=[("Image File",'.jpg')])
    name = (path.split("/"))[-1]
    global detectedp
    detectedp = path_ofprogram+ "/runs/detect/exp/"+name
    print(detectedp)
    comand_d = f"py detect.py --weights nsc2.pt --conf 0.5 --img-size 640 --source {path} --view-img --no-trace --save-txt" 
    os.system(comand_d)

    im = Image.open(detectedp)
    img = im.resize((600,400))
    new_image= ImageTk.PhotoImage(img)
    myvar=Label(top,image = new_image)
    myvar.image = new_image
    myvar.pack()
    # im = Image.open(detectedp)
    # img = im.resize((300,205))
    # new_image= ImageTk.PhotoImage(img)
    # myvar=Label(root,image = new_image)
    # myvar.image = new_image
    
    # myvar.pack()
    # global pathf 
    # pathf = path
    # print(type(name))

def open_popup():
   global top
   top= Toplevel(root)
   top.geometry("750x250")
   top.title("Detected photo")
   Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)
   Button(top,text="chose picture",fg="White",bg="Black",command=select_files2d).pack()


def detectpic():
    comand_d = f"py detect.py --weights nsc2.pt --conf 0.5 --img-size 640 --source {pathf} --view-img --no-trace --save-txt" 
    os.system(comand_d)

    



#ใส่ปุ่มกด
bt1=Button(text="Circuit Sanbox",fg="White",bg="Black",command=showMessage1).pack()
bt2=Button(text="Circuit Practice",fg="White",bg="Black",command=showMessage2).pack()
bt3=Button(text="New window",fg="White",bg="Black",command=open_popup).pack()
# bt4=Button(text="chose picture to",fg="White",bg="Black",command=select_files2d).pack()
# bt5=Button(text="detect picture",fg="White",bg="Black",command=detectpic).pack()
bt6=Button(text="Exit",fg="White",bg="Black",command=exit_x).pack()

root.geometry("1600x900+100+50") #กำหนดขนาดของหน้าจอเริ่มต้น
root.mainloop()

#กล่องข้อความ
#txt=StringVar()
#myLabel5=Label(root,text="Please insert your username : ").pack()
#mytext=Entry(root,textvariable=txt).pack()



