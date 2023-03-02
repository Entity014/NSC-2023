from tkinter  import *


#สร้างหน้าจอ ขึ้นมาเพื่อแสดงผล
root = Tk()
root.title("InspectCir Lite") #ชื่อของหน้าต่าง


#ใส่ข้อความในหน้าจอ
myLabel1 = Label(root,text="Hi There!",font=50).pack()


#Create Function
def showMessage1():
    Label(root,text="Coming Soon!",fg="red",bg="yellow",font=15).pack()
def showMessage2():
    Label(root,text="Coming Soon too!",fg="black",bg="yellow",font="50").pack()

#ใส่ปุ่มกด
bt1=Button(text="Circuit Sanbox",fg="White",bg="Black",command=showMessage1).pack()
bt2=Button(text="Circuit Practice",fg="White",bg="Black",command=showMessage2).pack()
bt3=Button(text="Exit",fg="White",bg="Black").pack()


root.geometry("1600x900+100+50") #กำหนดขนาดของหน้าจอเริ่มต้น
root.mainloop()

#กล่องข้อความ
#txt=StringVar()
#myLabel5=Label(root,text="Please insert your username : ").pack()
#mytext=Entry(root,textvariable=txt).pack()



